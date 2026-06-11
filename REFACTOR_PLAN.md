# 重构方案与路线图

## 新定位（不变量）
- 名称：**sunzi-strategist**（保留，已通过召回验证）；中文名：孙子·战略诊断器。
- 一句话：输入你的现实难题，用《孙子兵法》的核心框架帮你判断局势、胜算、风险与下一步行动。
- 五不：不占卜、不玄学、不鸡汤、不教算计、不鼓励攻击。目标：**减少误判、降低消耗、提高胜率。**

## 新文件结构

```
sunzi-strategist/
├── SKILL.md                      # 唯一主 Prompt（单一事实源，进 .skill 包）
├── README.md                     # 给人看的：是什么/怎么装/怎么问/边界
├── CHANGELOG.md                  # 版本史
├── AUDIT_REPORT.md               # 本次审查报告（仓库文档，不进运行时逻辑）
├── REFACTOR_PLAN.md              # 本文件
├── references/                   # 运行时按需加载（进 .skill 包）
│   ├── framework-ledger.md       # 全书五类台账+原文锚点（知识底座，单一来源）
│   ├── scorecards-and-gates.md   # 七计评分/市场五关/90天验证/对手反制
│   └── edge-lenses.md            # 边角透镜
├── examples/                     # 真实诊断范例（进包；模型可按需读来校准深度与腔调）
│   ├── price-war.md / new-cafe.md / career-choice.md / team-conflict.md / client-retention.md
├── feedback/                     # 反馈与学习闭环（进包；模式 E 复盘时读 AAR）
│   ├── feedback-schema.md / after-action-review.md / learning-loop.md / improvement-suggestions-template.md
└── evals/                        # 测试与回归（不进包：打包脚本自动排除 evals/）
    ├── test-cases.md / scoring-rubric.md / regression-checklist.md
```

设计原则：**SKILL.md 是唯一调度中枢**——按需引用 references/examples/feedback，绝不复制内容到第二处；evals 永不进包。

## 架构要点
- **Prompt 架构**：frontmatter description（召回）→ 6 使用原则（判断纪律）→ 五层主流程（诊断逻辑）→ 输出模式 A–F（场景调度）→ 质量闸门（出厂检验）→ 声音（腔调）→ 参考文件（按需装载）。
- **知识库架构**：framework-ledger 是底座（含核心/边角分级与原文锚点）；scorecards 是量化工具；edge-lenses 是情境工具。三者互不重叠。
- **反馈学习机制**（可控、可审查、可回滚）：对话内邀请反馈 → 用户按 feedback-schema 记录 → 积累后人工跑 learning-loop → 生成 improvement-suggestions → 人工 review → 改 SKILL.md → 升版本号 + CHANGELOG → 跑 evals/regression-checklist 防退化。**skill 不自动改自己的 Prompt。**
- **评估机制**：evals/test-cases.md 20 用例（8 触发校准 + 12 质量场景）；scoring-rubric 10 维 0–2 分；regression-checklist 是每次改动后的最低门槛。

## 打包

> 2026-06-11 起本仓库收敛为单一事实源（GitHub 仓布局）：skill 本体在 `sunzi-strategist/` 子目录，**只含运行时文件**，构建无需排除项：

```bash
cd ~/sunzi-strategist && rm -f dist/sunzi-strategist.skill && \
zip -rq dist/sunzi-strategist.skill sunzi-strategist -x "*.DS_Store" && \
python3 evals/static-checks.py
```

改完源文件 → 上面一条命令完成 构建+验证 → 同步安装副本（`cp -r sunzi-strategist/* ~/.codex/skills/sunzi-strategist/`）→ commit + push。
仍然注意：**不要**用 skill-creator 的 package_skill.py 对仓库根打包（它不排除 .git）。

## 发布流程（tag 驱动，自动化）

1. CHANGELOG 加新版本段 → commit 推 main → 等 `checks` 工作流绿灯。
2. 打 tag 并推送：`git tag -a vX.Y.Z -m "一句话摘要" && git push origin vX.Y.Z`。**一次只推一个 tag**——GitHub 对单次推送超过 3 个 tag 不产生任何 push 事件（v0.4.0 首发时实测踩坑），批量推 tag 会静默不触发发布。
3. `release` 工作流自动接手：构建 .skill → 跑 static-checks（不过不发布）→ 创建 GitHub Release 并附安装包 + 自动生成 release notes。

约定：README **不写死版本号**（徽章自动显示 latest release）；安装直链固定为 `releases/latest/download/sunzi-strategist.skill`，永远指向最新包——避免再次出现"Releases 停在旧版、关注者看不到升级"。

## 路线图
- **v0.3.0（本次）**：开源工程化——git/README/CHANGELOG/evals/examples/feedback/ledger/模式 F。
- **v0.4**：回归清单脚本化（结构断言自动跑）；英文 README + 双语 description；LICENSE 确认后推 GitHub。
- **v0.5**：真实反馈案例 ≥10 个后第一轮 learning-loop 迭代；案例库扩充（谈判/管理各 2 篇）。
- **长期**：触发召回的量化测试（仅当重新依赖自动召回时做）；多模型适配说明（豆包/Kimi/DeepSeek 路径）。
