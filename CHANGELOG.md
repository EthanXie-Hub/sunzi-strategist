# Changelog

## v0.4.0 — 2026-06-11（发布工程）
- 新增 GitHub Actions：`checks`（push/PR 自动跑 40 项静态检查）、`release`（推 tag 自动构建 .skill、验证、创建 Release 并附安装包）。
- README 专业化：徽章行（release/CI/license，版本徽章自动跟随最新 Release）；安装改为 `releases/latest/download` 固定直链；补 Claude Code 与 claude.ai 安装路径；不再硬编码版本号。
- 补历史 tag：v0.2.0（初始发布内容）、v0.3.1、v0.3.2。
- REFACTOR_PLAN 新增 tag 驱动发布流程。

## v0.3.2 — 2026-06-11（审查遗留项清零）
- AUDIT_REPORT 第二人称表述中性化；LICENSE 项标记已解决。
- LICENSE 复制到 `sunzi-strategist/LICENSE`，随 dist 包分发（开源分发惯例）。
- static-checks 新增 2 项守卫：skill 目录含 LICENSE、.skill 包含 LICENSE（共 40 项）。
- 仓库收敛为单一事实源：本地即 GitHub clone，旧开发历史存档于分支 `archive/local-dev-history`；打包命令适配新布局。

## v0.3.1 — 2026-06-11（发布准备）
- 新增 LICENSE（MIT）。
- 新增 evals/static-checks.py：自动化静态回归（frontmatter 约束/必备段落/链接完整/必备文件/.skill 包卫生/安装副本同步）。
- README 明示三层架构（兵法知识 / 诊断器 / 反馈学习循环）的文件映射。
- 仓库推送 GitHub（初始为 private，公开与否由所有者决定）。

## v0.3.0 — 2026-06-11（开源工程化重构）
- 初始化 git 仓库（基线 = v0.2.0 快照）。
- 新增 README.md（定位/安装/输入示例/伦理边界/贡献方式）。
- 新增 references/framework-ledger.md：全书五类台账（框架/原则/技法/反模式/声音）+ 原文精确锚点 + 核心/边角分级——知识底座从开发对话沉淀进仓库。
- 新增 evals/：20 个测试用例（8 触发校准 + 12 质量场景）、10 维评分细则、改动后回归清单。**evals/ 不进 .skill 包。**
- 新增 examples/：5 个诊断范例（价格战、新开咖啡店、选 offer、同事冲突伦理、客户复购）。
- 新增 feedback/：反馈 JSON schema、AAR 复盘七问、可控学习循环（人工 review + 版本化，禁止 Prompt 自改）、改进建议模板。
- SKILL.md：新增输出模式 F（对比决策 A/B/C）；模式 E 接入 AAR 七问；质量闸门补"邀请回流复盘"项；参考文件清单补 ledger/examples/feedback。
- 新增 AUDIT_REPORT.md / REFACTOR_PLAN.md；明确打包须排除 .git（脚本 gotcha）。

## v0.2.0 — 2026-06-02（合并强化版）
- 合并 Codex 强化分支：止损线/kill criteria、行动门槛、七计 10 分评分表（scorecards-and-gates.md）、市场进入五关、90 天验证计划、对手反制清单、质量闸门、输出模式 A–E。
- 回补三项被丢的设计：中文高召回 description（8/8 验证）、伦理护栏（全胜价值观：诡道≠烧关系）、决定性未知+低成本侦察。

## v0.1.0 — 2026-06-02（初版）
- 五层诊断主流程（先胜→全胜→形势虚实→九变→反模式）+ 精简/完整双档输出 + references/edge-lenses.md。
- description 高召回设计与触发校准（8 句样例全部符合预期）。
