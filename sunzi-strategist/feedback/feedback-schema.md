# 反馈数据结构

每次重大诊断（影响真金白银/职业走向的）结束后，邀请用户留下反馈；用户也可在行动有结果后回填。一条反馈一个 JSON，存入用户自己的 `feedback/cases/` 目录（匿名，不进 git 公开仓库除非用户同意）。

```json
{
  "case_id": "2026-06-11-price-war-01",
  "scenario": "竞品降价30%是否跟进",
  "user_goal": "保住核心客户与毛利",
  "strategy_used": "不跟明降；锁定Top客户做不明降留客；侦察对手降价动因",
  "frameworks_applied": ["避实击虚", "致人而不致于人", "怒而兴师(反)"],
  "user_rating": 4,
  "outcome": "partial",
  "what_worked": "不跟价的判断对了，对手两个月后撤回价",
  "what_failed": "低估了渠道商趁机压价的二阶反应",
  "missing_context": "诊断时没问渠道结构",
  "next_improvement": "对渠道型生意要默认追问渠道商会怎么动",
  "created_at": "2026-08-15"
}
```

字段说明：`outcome` ∈ success / partial / failed / unknown；`user_rating` 1–5；`frameworks_applied` 用 framework-ledger.md 的原始命名，便于聚合统计"哪个透镜常被误用"。

隐私：示例、案例沉淀一律去除公司名、人名、可识别金额；用户拒绝沉淀则只留 rating + outcome 两个字段。
