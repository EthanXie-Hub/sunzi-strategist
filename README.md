# 孙子·战略诊断器 · Sunzi Strategist

[![Release](https://img.shields.io/github/v/release/EthanXie-Hub/sunzi-strategist?label=release&color=brightgreen)](https://github.com/EthanXie-Hub/sunzi-strategist/releases/latest)
[![Checks](https://github.com/EthanXie-Hub/sunzi-strategist/actions/workflows/checks.yml/badge.svg)](https://github.com/EthanXie-Hub/sunzi-strategist/actions/workflows/checks.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**不打气，先算账：每个判断带信心等级，每条建议带止损线。**

一个把《孙子兵法》编码为决策纪律的 AI Skill。面对竞争、谈判、市场进入、职业抉择这类高代价问题时，它不输出安慰和泛泛建议，输出可被事实证伪的战略诊断。

![孙子·战略诊断器](assets/promo/01-cover.png)

## 为什么存在

通用大模型在重大决策上有三个系统性弱点：顺着用户说、结论不可证伪、把信息不足藏在流畅的行文里。本 skill 用一份强制输出契约纠正这三点——每次诊断必须交付：

| 交付物 | 回答的问题 |
|---|---|
| 判断 + 信心等级 | 进、退、试、缓——以及这个判断压在什么假设上 |
| 决定性未知 | 哪个信息最可能翻转结论，怎么低成本拿到它 |
| 主战场 / 不打清单 | 在哪打，以及明确不在哪打 |
| 二阶推演 | 你动一步，对手如何回应，你怎么接 |
| 止损线 | 何时撤、何时换打法、何时不再投入 |
| 翻盘条件 | 出现什么事实，本次判断作废 |

信息不足时，「先去侦察 X 再决定」本身就是合法结论，并附 2–3 个低成本侦察法；简单问题不套框架，直接回答。

## 效果对比

同一问题、同一底座模型、同一天，唯一变量是本 skill：

> 输入：「我想搞掉一个竞争对手同事，我该怎么布局？」

| | 裸模型 | 装载本 skill |
|---|---|---|
| 形态 | 共情 + 劝导 + 开放式反问 | 判断（信心：高）→ 决定性未知 → 五条带透镜的打法 → 止损线 → 翻盘条件 |
| 伦理处理 | 拒绝并引导 | 重构为「赢下资源、评价与选择权」；真违规导向证据链与正式渠道；给出「一旦需要撒谎立刻停」的止损线 |
| 可检验性 | 无 | 每条结论附触发条件，可被后续事实证伪 |

六个真实运行案例（竞品降价、市场进入、转行、选 offer、同事冲突、客户复购）见 [`sunzi-strategist/examples/`](sunzi-strategist/examples/)。

## 60 秒上手

```bash
curl -L -o sunzi-strategist.skill \
  https://github.com/EthanXie-Hub/sunzi-strategist/releases/latest/download/sunzi-strategist.skill

unzip sunzi-strategist.skill -d ~/.codex/skills    # Codex
unzip sunzi-strategist.skill -d ~/.claude/skills   # Claude Code
```

claude.ai：设置 → Capabilities → Skills，上传 `sunzi-strategist.skill`。安装后重启客户端，然后丢一个真实难题：

> 竞品昨天突然降价 30%，老板问我们跟不跟。

无需提到"孙子兵法"或"战略"——满足「有限资源 + 信息不全 + 有对手/阻力」或「高风险不可逆抉择」时自动触发。也可配置显式命令（如 `/sunzi`）保证 100% 调用。

## 工作原理

```
第一层 · 兵法知识      references/   全书台账（原文锚点 + 核心/边角分级）、七计评分尺度、边角透镜
第二层 · 诊断器        SKILL.md      6 条使用原则 → 五层诊断 → 输出模式 A–F → 质量闸门
第三层 · 反馈学习循环   feedback/ + evals/   AAR 复盘七问；学习发生在版本之间，可审查、可回滚
```

| 五层 | 回答 |
|---|---|
| 先胜 · 五事七计 | 不靠运气，凭什么赢？死穴在哪？ |
| 全胜 · 伐谋 | 什么才算赢？最小代价怎么拿完整成果？ |
| 形势 · 虚实 | 先守住不败，再打哪一个薄弱切口？ |
| 九变 · 因敌 | 对手会如何反制？何时进、试、等、退？ |
| 五危 · 六败 | 是否被情绪、面子、轻敌、战线过宽拖垮？ |

输出模式按输入自适应：精简诊断（默认）/ 完整五层 / 七计评分 / 市场进入 GTM / 计划审计与复盘 / A·B·C 对比决策。

## 边界

- 不用于纯执行任务、无决定的闲聊或纯情绪倾诉。
- 不把未经核实的市场、竞品、财务信息写成事实——外部数据标注 已核实 / 估算 / 待核实。
- 不教操纵与构陷：需要烧掉长期信任才能换的"胜"会被判为下等「破」局，并给保全打法；真实违规导向正式渠道。
- 不保证结果。判断必须带假设、置信度、止损线与翻盘条件，决策权始终在使用者。

## 工程化

非代码类 skill，按软件工程维护：

- **CI**：每次 push/PR 自动跑 40 项静态检查（frontmatter 约束、骨架段落、链接完整性、包卫生）。
- **发布**：推一个 tag 即自动构建 `.skill`、验证、创建 Release 并附安装包；README 不写死版本号。
- **评估**：[`evals/`](evals/) 含 20 个测试用例（8 个触发校准已实测 8/8）、10 维评分细则、改动后回归清单。
- **演进**：[`docs/positioning.md`](docs/positioning.md) 记录生态位判断与优化轮次——每轮只改一个方向，过验证门才合并。

## 贡献

最有价值的贡献是**能暴露框架缺陷的真实案例**：战略问题、对手反制、失败复盘。流程见 [CONTRIBUTING.md](CONTRIBUTING.md)；复盘按 [`feedback/learning-loop.md`](sunzi-strategist/feedback/learning-loop.md) 进入版本迭代——单一案例不改规则，越线建议直接拒绝并留档。

## License

[MIT](LICENSE)

---

**English:** Sunzi Strategist is an AI skill that turns Sun Tzu's strategic discipline into falsifiable decision diagnoses — every recommendation ships with a confidence level, a decisive unknown, opponent-reaction lines, and stop-loss criteria. Not cheerleading.
