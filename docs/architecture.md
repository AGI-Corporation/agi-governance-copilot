# Architecture: Conceptual to Technical

This document maps the AGI Future Foundation PBC's conceptual governance frameworks to the concrete OpenClaw technical implementation in this project.

---

## Framework Mapping

| AGI Future Foundation Concept | This Implementation |
|---|---|
| **Institutional AGI Framework** | `GovernanceCopilot` class in `src/agent.py` — scoped role, bounded tools, policy context |
| **Fiduciary Shield** | Hard-coded constraints: no wallet tools, `human_signoff_required: true` on all outputs |
| **Institutional Grid** | 6-dimension weighted scoring in `evaluate_proposal_tool` |
| **Governance Engine** | End-to-end pipeline: intake → evaluate → snapshot → digest |
| **AGI Institutional Ledger** | `governance-ledger.jsonl` — append-only JSONL with input/output hashes |
| **Agentic Web Architecture** | Multi-channel: GitHub Issues, Telegram, Discord, CLI |
| **Corporate Governance Framework** | `config/public-goods-principles.md` — loaded as policy context |
| **AGI Fiduciary Ecosystem** | `config/example-dao-rules.md` + principle files = agent's rule base |

---

## Data Flow

```
Proposal (JSON/MD)
       |
       v
  GovernanceCopilot.evaluate_proposal()
       |
       +--> load_policies() → DAO rules + Public Goods Principles
       |
       +--> evaluate_proposal_tool(proposal, rules, policies, llm_fn)
       |         |
       |         +--> LLM (GPT-4o via OpenAI API)
       |         |    System: policy context + institutional grid
       |         |    User: proposal text
       |         |
       |         +--> Parse JSON response
       |              verdict + scores + reasoning + policy refs
       |
       +--> _log_to_ledger(action, input_hash, output_hash)
       |         |
       |         +--> governance-ledger.jsonl (append)
       |
       v
  Result dict → CLI display OR GitHub comment OR Telegram message
```

---

## Safety Layer

The safety model is inspired by the AGI Future Foundation's "Mathematical Cages" concept from the Fiduciary Architecture framework:

1. **No execution tools**: The agent has no access to wallets, smart contracts, or any state-modifying tools.
2. **Advisory outputs only**: Every output includes `human_signoff_required: true`.
3. **Policy grounding**: The LLM system prompt always includes the full policy context, forcing outputs to be policy-referenced.
4. **Audit log**: Every tool call is logged before the result is returned.
5. **Fail-safe default**: Parse errors return `verdict: Revise` (never auto-approve).

---

## OpenClaw Integration Points

The agent is designed to be plugged into OpenClaw's skill/tool system:

- `evaluate_proposal` → OpenClaw tool with `proposal_text` and `rules_path` inputs
- `generate_impact_snapshot` → OpenClaw tool with `project_data` input
- `emit_governance_digest` → OpenClaw scheduled tool with `since` parameter
- Channel connectors: GitHub, Telegram, Discord via OpenClaw's built-in channel adapters

---

## Extending the Agent

To add a new DAO:
1. Create a `config/<dao-name>-rules.md` file with governance rules
2. Update `agent-config.yaml` → `policies.dao_rules` to point to the new file
3. Optionally add custom scoring weights in `config/agent-config.yaml`

To add a new evaluation dimension:
1. Add the dimension to the system prompt in `src/tools/evaluate_proposal.py`
2. Update the scoring weight table in `config/public-goods-principles.md`
3. Update the `dimension_scores` schema in `src/schemas/impact_card.py`
