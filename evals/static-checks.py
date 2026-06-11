#!/usr/bin/env python3
"""sunzi-strategist 静态回归检查。

自动化 regression-checklist.md 里"跑不动模型也能查"的部分：
frontmatter 约束、必备段落、链接完整性、必备文件、.skill 包卫生、安装副本同步。
模型行为探针（伦理/诚实/右尺寸）仍需按 regression-checklist.md 手测。

用法: python3 evals/static-checks.py
退出码: 0 全过 / 1 有失败
"""
import re
import sys
import filecmp
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
failures = []


def check(name, ok, detail=""):
    print(("✅" if ok else "❌"), name, (f"— {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(name)


# 1. SKILL.md 与 frontmatter（大写文件名是加载器硬性要求）
skill = REPO / "SKILL.md"
check("SKILL.md 存在（必须大写）", skill.exists())
text = skill.read_text(encoding="utf-8") if skill.exists() else ""
m = re.match(r"^---\n(.*?)\n---", text, re.S)
check("frontmatter 存在", bool(m))
if m:
    fm = m.group(1)
    nm = re.search(r"^name:\s*(\S+)", fm, re.M)
    check("name == sunzi-strategist", bool(nm) and nm.group(1) == "sunzi-strategist")
    dm = re.search(r"^description:\s*>\s*\n((?:[ ]{2}.*\n?)+)", fm, re.M)
    desc = " ".join(l.strip() for l in dm.group(1).splitlines()) if dm else ""
    check("description 非空且 ≤1024 字符", 0 < len(desc) <= 1024, f"len={len(desc)}")
    check("description 无尖括号", "<" not in desc and ">" not in desc)

# 2. 必备段落（三层架构的第二层：诊断器骨架没被改丢）
for sec in ["使用原则", "五层诊断", "输出模式", "质量闸门",
            "决定性未知", "止损", "翻盘条件", "对比决策", "伐谋", "反模式"]:
    check(f"SKILL.md 含「{sec}」", sec in text)

# 3. SKILL.md 相对链接全部存在
links = re.findall(r"\]\(((?:references|feedback|examples)/[^)]+)\)", text)
for link in sorted(set(links)):
    check(f"链接存在: {link}", (REPO / link).exists())

# 4. 三层结构必备文件
required = [
    "README.md", "CHANGELOG.md", "LICENSE",
    # 第一层：兵法知识
    "references/framework-ledger.md", "references/scorecards-and-gates.md",
    "references/edge-lenses.md",
    # 第三层：反馈学习循环
    "feedback/feedback-schema.md", "feedback/after-action-review.md",
    "feedback/learning-loop.md", "feedback/improvement-suggestions-template.md",
    "evals/test-cases.md", "evals/scoring-rubric.md", "evals/regression-checklist.md",
]
for f in required:
    check(f"文件存在: {f}", (REPO / f).exists())
examples = list((REPO / "examples").glob("*.md")) if (REPO / "examples").exists() else []
check("examples ≥5 篇", len(examples) >= 5, f"found {len(examples)}")

# 5. .skill 包卫生（若已打包）
pkg = REPO.parent / "sunzi-strategist.skill"
if pkg.exists():
    out = subprocess.run(["unzip", "-l", str(pkg)], capture_output=True, text=True).stdout
    check(".skill 不含 .git", "/.git/" not in out)
    check(".skill 不含 evals/", "evals/" not in out)
    check(".skill 含最新 SKILL.md 路径", "sunzi-strategist/SKILL.md" in out)
else:
    print("ℹ️  未找到 ../sunzi-strategist.skill，跳过包检查")

# 6. 安装副本同步（存在才查）
for dest in [Path.home() / ".codex/skills/sunzi-strategist",
             Path.home() / ".claude/skills/sunzi-strategist"]:
    if (dest / "SKILL.md").exists():
        check(f"副本同步: {dest}", filecmp.cmp(skill, dest / "SKILL.md", shallow=False))

print()
if failures:
    print(f"❌ {len(failures)} 项未通过；按 git diff 定位最近改动，回滚该节重试")
    sys.exit(1)
print("✅ 静态检查全过（模型行为探针请按 regression-checklist.md 第 1–2 节手测）")
