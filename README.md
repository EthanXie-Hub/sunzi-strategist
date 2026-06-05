# 孙子·战略诊断器

![孙子·战略诊断器](assets/promo/01-cover.png)

一个把《孙子兵法》转成现代决策算账框架的 AI Skill。

它不负责给普通建议套古文，也不鼓励逞强、硬刚或操纵。它处理的是：

- 有限资源、信息不全、有对手或现实阻力的对抗局
- 高风险、不易撤回、代价很高的重大选择
- 商业竞争、市场进入、谈判、组织僵局与项目取舍
- 已有计划的反制推演、失败复盘和止损审计

> 先算能不能赢，再定什么算赢；先立于不败，再寻找可胜；先选战场，再谈打法。

## 它交付什么

每次战略诊断必须落到：

1. **判断**：进、退、缩小试、暂缓，还是先侦察。
2. **决定性未知**：哪个信息最可能翻转结论，如何低成本拿到。
3. **赢的定义**：什么结果才算赢，哪些代价不能付。
4. **主战场**：在哪打、避开什么、只集中突破哪一处。
5. **行动打法**：你动一步，对手如何回应，你再怎么接。
6. **止损线**：何时撤、何时换打法、何时不再投入。
7. **翻盘条件**：什么事实会推翻当前判断。

## 五层诊断

![五层战略诊断](assets/promo/02-framework.png)

| 层 | 现实问题 |
| --- | --- |
| 先胜 · 五事七计 | 不靠运气，凭什么能赢？死穴在哪里？ |
| 全胜 · 伐谋 | 什么才算赢？怎样用最小代价拿完整成果？ |
| 形势 · 虚实 | 如何先守住不败，再只打一个薄弱切口？ |
| 九变 · 因敌 | 对手会如何反制？何时进、试、等、退？ |
| 五危 · 六败 | 是否被情绪、面子、轻敌或战线过宽拖垮？ |

七计评分、市场进入五关、90 天验证计划和对手反制清单位于 `references/scorecards-and-gates.md`。

## 它与普通战略建议的区别

- 不用“信息不足”逃避判断，而是锁定一个决定性未知并给侦察法。
- 不只给总分，而是指出最该补的 1 至 3 项和补分动作。
- 不把正面冲突当勇敢，优先伐谋、伐交、避实击虚。
- 不把短期胜利当胜利，主动保护现金流、声誉、组织能力和退路。
- 不把兵法变成操纵术；欺骗信任关系、报复与违法不是战略。

![真实战略问题](assets/promo/03-real-case.png)

## 安装

### 下载安装包

从 [Releases](https://github.com/EthanXie-Hub/sunzi-strategist/releases) 下载 `sunzi-strategist.skill`，解压到 Codex Skills 目录：

```bash
unzip sunzi-strategist.skill -d ~/.codex/skills
```

安装后重启 Codex。

### 从 GitHub 安装到 Codex

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo EthanXie-Hub/sunzi-strategist \
  --path sunzi-strategist
```

### 其他支持 Skill 的平台

核心能力采用可迁移的 Markdown 结构，位于 `sunzi-strategist/SKILL.md` 与 `references/`。将整个 `sunzi-strategist/` 文件夹复制到平台要求的 Skill 目录即可。

不同平台的发现目录、元数据与自动触发机制可能不同；`agents/openai.yaml` 是 OpenAI/Codex 的可选界面元数据。

![安装与结构](assets/promo/04-install.png)

## 使用

```text
$sunzi-strategist
我们资源明显少于竞品，但想进入他们占优的市场。该不该正面打？
请给我决定性未知、主战场、对手反制和止损线。
```

也可以直接描述一个真实僵局、重大选择或竞争问题。Skill 会先判断这是否真是战略问题，简单问题不会硬套五层框架。

## 仓库结构

```text
.
├── sunzi-strategist/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── edge-lenses.md
│       └── scorecards-and-gates.md
├── dist/sunzi-strategist.skill
├── docs/open-source-launch.zh-CN.md
├── examples/real-world-strategy-diagnoses.md
└── assets/promo/
```

## 边界

- 不用于纯执行任务、无决定的闲聊或纯情绪倾诉。
- 不把未经核实的市场、政策、竞品与财务信息写成事实。
- 不鼓励欺骗、报复、威胁、违法或破坏长期信任。
- 不保证结果；评分与判断必须带假设、置信度、止损线和翻盘条件。

## 验证

当前 Skill 已通过 Codex `skill-creator` 的基础结构校验：

```text
Skill is valid!
```

这证明结构有效，不代表每次战略判断天然正确。真实决策仍需事实验证、现实反馈与及时止损。

## 贡献

欢迎提交能暴露框架缺陷的真实战略问题、对手反制、评分修正、失败复盘与平台适配。参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

[MIT](LICENSE)

---

**English summary:** Sunzi Strategist turns Sun Tzu's layered strategic lenses into evidence-aware modern decision diagnoses with a decisive unknown, battlefield choice, opponent reactions, action thresholds, and stop-loss criteria.
