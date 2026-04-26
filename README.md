<p align="center">
  <img src="https://raw.githubusercontent.com/AGI-Corporation/agi-governance-copilot/main/assets/header-wiki.svg" width="100%" alt="AGI Governance Copilot Header">
</p>

# AGI Governance Copilot 🛡️🏛️

**An OpenClaw-powered agentic governance assistant for DAOs and public-goods funds — built on the AGI Future Foundation's Institutional AGI, Fiduciary Shield, and Governance Engine frameworks.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Built with OpenClaw](https://img.shields.io/badge/Built%20with-OpenClaw-purple)](https://github.com/gcc-foundation/openclaw)
[![GCC Agentic Public Goods Track](https://img.shields.io/badge/GCC-Agentic%20Public%20Goods-green)](https://www.gccofficial.org/en)
[![Documentation](https://img.shields.io/badge/docs-Wiki-blue)](https://github.com/AGI-Corporation/agi-governance-copilot/wiki)

---

## Overview
This project is the **first reference implementation** of the [AGI Future Foundation PBC](https://www.agifuturefoundation.org)'s Institutional AGI governance architecture, translated into a working agentic stack using OpenClaw and Bodhi. It helps decentralized organizations:

- Evaluate and triage governance proposals against fiduciary and public-benefit rules
- Allocate grants with structured, auditable decision memos
- Track funded project impact via periodic AI-generated Impact Snapshots
- Maintain a verifiable Governance Ledger — every agent action is logged and traceable
- Receive weekly governance digests in Telegram / Discord / GitHub / Voice (via Bodhi)

**The agent is advisory, never autonomous with funds.** It drafts. Humans decide.

---

## Track: GCC Agentic Public Goods — Special Prize $1k–$5k

| Track Requirement | Implementation |
|---|---|
| DAO Governance | Proposal ingestion, compliance check against DAO charter + fiduciary rules |
| Fund Allocation | Structured grant pipeline: triage → eligibility → alignment score → tranche plan |
| Impact Evaluation | AI-generated Impact Snapshots with progress-vs-milestone scoring |
| Workflow Optimization | End-to-end workflow: intake → risk screen → decision memo → follow-up |
| AI Safety & Trust | Advisory-only mode, full governance ledger, no on-chain write access |

---

## Architecture
```
┌─────────────────────────────────────────────────────────┐
│                    Interface Layer                      │
│   Bodhi (Voice) · Telegram · Discord · GitHub · CLI     │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│            Governance Brain (OpenClaw Agent)            │
│    LLM + DAO Charter + AGI Future Foundation Rules      │
│   Fiduciary Shield · Institutional Grid · Public Benefit│
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                   Execution Tools                       │
│     evaluate_proposal · generate_impact_snapshot        │
│      emit_governance_digest · fetch_proposal            │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                Safety & Audit Layer                     │
│    Governance Ledger (JSONL) · No wallet/on-chain writes│
│    Policy references in every output · Human sign-off   │
└─────────────────────────────────────────────────────────┘
```

---

## Features

### 1. Proposal Ingestion & Evaluation
- Accepts Markdown or JSON proposals (title, requester, amount, milestones, links)
- Normalizes into a structured **Impact Card** schema
- Evaluates against DAO rules + AGI Future Foundation fiduciary constraints
- Returns: `Pass / Revise / Reject` + reasoning with clause references

### 2. Fund Allocation Pipeline
- Scores alignment with public-goods objectives
- Recommends funding tranches and milestone gates
- Generates decision memos ready for human review

### 3. Impact Evaluation Loop
- Reads periodic project updates (GitHub issues, forms, status posts)
- Produces compact **Impact Snapshots**: progress, risks, open-source contribution score
- Posts results back to GitHub as issue comments

### 4. Governance Digest
- Weekly or on-demand summary for DAO stewards
- Highlights: new proposals pending review, stale projects, risk alerts
- Delivered to Telegram, Discord, GitHub, and Voice (via Bodhi)

### 5. Governance Ledger
- Every agent recommendation logged to `governance-ledger.jsonl`
- Each entry includes: timestamp, input hash, output hash, policy references
- Provides a tamper-evident audit trail — the "AGI Institutional Ledger" made real

---

## Quick Start

### Prerequisites
- Python 3.11+
- OpenClaw installed (`pip install openclaw`)
- OpenAI or Anthropic API key

### Install
```bash
git clone https://github.com/AGI-Corporation/agi-governance-copilot.git
cd agi-governance-copilot<p align=\"center\">
  <img src=\"https://raw.githubusercontent.com/AGI-Corporation/agi-governance-copilot/main/assets/header-wiki.svg\" width=\"100%\" alt=\"AGI Governance Copilot Header\">
</p>

# AGI Governance Copilot 🛡️🏛️

**An OpenClaw-powered agentic governance assistant for DAOs and public-goods funds — built on the AGI Future Foundation's Institutional AGI, Fiduciary Shield, and Governance Engine frameworks.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Built with OpenClaw](https://img.shields.io/badge/Built%20with-OpenClaw-purple)](https://github.com/gcc-foundation/openclaw)
[![GCC Agentic Public Goods Track](https://img.shields.io/badge/GCC-Agentic%20Public%20Goods-green)](https://www.gccofficial.org/en)
[![Documentation](https://img.shields.io/badge/docs-Wiki-blue)](https://github.com/AGI-Corporation/agi-governance-copilot/wiki)

## 🎯 Overview

This project is the **first reference implementation** of the [AGI Future Foundation PBC](https://www.agifuturefoundation.org/)'s Institutional AGI governance architecture. It translates complex fiduciary and public-benefit obligations into a working agentic stack.

Now featuring **Deep Bodhi Realtime Voice Integration**, allowing human supervisors to interact with the governance engine naturally while parallel async sub-agents handle complex audits and evaluations in the background.

### Key Capabilities:
- **Triage & Evaluate:** Automatically evaluate governance proposals against fiduciary and public-benefit rules.
- **Grant Allocation:** Recommend tranches and milestone gates based on alignment scores.
- **Impact Snapshots:** Track project progress via AI-generated reports and GitHub status tracking.
- **Governance Ledger:** Maintain a verifiable, hashed audit trail of every agent action.
- **Voice Interface:** High-assurance oversight and natural language digests via the **Bodhi Realtime Agent**.

---

## 🎙️ Bodhi Realtime Integration

The AGI Governance Copilot now leverages the [Bodhi Realtime Agent](https://github.com/AGI-Corporation/bodhi_realtime_agent) as its primary interactive layer.

- **Natural Oversight:** \"Bodhi, summarize the pending grant proposals for this week.\"
- **Parallel Execution:** While you converse with Bodhi, background sub-agents perform real-time cross-model audits and compliance checks.
- **Voice-Auth:** High-impact fiduciary decisions require voice-biometric confirmation, ensuring human-in-the-loop safety.

---

## 🏗️ Architecture

```mermaid
graph TD
    User((👤 User)) -- \"Voice/Text\" --> Bodhi[\"🎙️ Bodhi Realtime Agent\"]
    Bodhi -- \"Orchestration\" --> MIKE[\"🧠 M.I.K.E. Engine\"]
    
    MIKE -- \"Evaluation\" --> GovEngine[\"⚖️ Governance Engine\"]
    GovEngine -- \"Audit\" --> Ledger[\"📜 Governance Ledger\"]
    
    MIKE -- \"Parallel Audit\" --> SubAgents[\"🤖 Sub-Agents\"]
    SubAgents -- \"Cross-Model Verification\" --> MIKE
    
    MIKE -- \"External Delivery\" --> Out[\"📱 Telegram / Discord / GitHub\"]
```

---

## 🛠️ Conceptual Foundation

This project operationalizes the following AGI Future Foundation PBC frameworks:

| Framework | Implementation |
|-----------|----------------|
| **Institutional AGI** | Agent role definition, tool boundaries, and policy overlays. |
| **Fiduciary Shield** | Hard constraints: no autonomous fund transfers, human sign-off required. |
| **Institutional Grid** | Ruleset structure encoding public-benefit obligations. |
| **Governance Engine** | Proposal → evaluation → decision → follow-up pipeline. |
| **Bodhi Voice Stack** | Real-time, non-blocking interface for human-agent collaboration. |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- [OpenClaw](https://github.com/gcc-foundation/openclaw) installed: `pip install openclaw`
- [Bodhi Realtime Agent](https://github.com/AGI-Corporation/bodhi_realtime_agent) for voice capabilities.

### Installation
```bash
git clone https://github.com/AGI-Corporation/agi-governance-copilot.git
cd agi-governance-copilot
pip install -r requirements.txt
```

### Configuration
1. Copy the example config: `cp config/agent-config.example.yaml config/agent-config.yaml`
2. Edit `config/agent-config.yaml` with your API keys and DAO rules path.

---

## 🛠 Builders & Investors

We are actively seeking contributors to expand the **Institutional Grid**.

* **Builders:** Help us build specialized MCP servers and cognitive sub-agents. See the [MIKE-OGI-Framework](https://github.com/AGI-Corporation/agi-governance-copilot/wiki/MIKE-OGI-Framework) to get started.
* **Investors:** Align with the OGI model. For partnership inquiries, please contact us.

## 📧 Contact & Support
* **General:** [contact@agicorp.network](mailto:contact@agicorp.network)
* **Technical (M.I.K.E.):** [mike@agicorp.network](mailto:mike@agicorp.network)
* **Support:** [hello@maxhealth.tech](mailto:hello@maxhealth.tech)
* **Website:** [www.agicorp.network](https://www.agicorp.network)
* **Social:** [LinkedIn](https://www.linkedin.com/in/infogurus) | [X (Twitter)](https://x.com/idescidude)

---

### Links
- **Bodhi Realtime Agent:** [GitHub](https://github.com/AGI-Corporation/bodhi_realtime_agent)
- **AGI Future Foundation:** [agifuturefoundation.org](https://www.agifuturefoundation.org)
- **GCC Foundation:** [gccofficial.org](https://www.gccofficial.org/en)

---
*Built for the GCC Agentic Public Goods Track.*

pip install -r requirements.txt
```

### Configure
```bash
cp config/agent-config.example.yaml config/agent-config.yaml
# Edit config/agent-config.yaml with your API keys and DAO rules path
```

### Run
```bash
# Evaluate a proposal
python src/main.py evaluate --proposal examples/sample-proposal.json

# Generate impact snapshot for a funded project
python src/main.py impact --project examples/sample-project-update.json

# Emit governance digest
python src/main.py digest
```

---

## Repository Structure
```
agi-governance-copilot/
├── README.md
├── LICENSE
├── requirements.txt
├── config/
│   ├── agent-config.example.yaml   # OpenClaw agent config template
│   ├── example-dao-rules.md        # Sample DAO charter / governance rules
│   └── public-goods-principles.md  # AGI Future Foundation public-benefit constraints
├── docs/
│   ├── architecture.md             # Conceptual → technical architecture mapping
│   ├── governance-model.md         # Fiduciary shield + institutional grid explanation
│   └── safety-and-audit.md         # Limitations, ledger design, safety constraints
├── src/
│   ├── main.py                     # CLI entrypoint
│   ├── agent.py                    # OpenClaw agent initialization
│   ├── tools/
│   │   ├── evaluate_proposal.py    # Proposal evaluation tool
│   │   ├── impact_snapshot.py      # Impact evaluation tool
│   │   ├── governance_digest.py    # Digest generation tool
│   │   └── ledger.py               # Governance ledger logging
│   └── schemas/
│       ├── impact_card.py          # Impact Card schema
│       └── risk_card.py            # Risk Card schema
└── examples/
    ├── sample-proposal.json        # Example grant proposal
    ├── sample-project-update.json  # Example funded project update
    ├── sample-impact-snapshot.json # Example agent output
    └── sample-governance-ledger.jsonl # Example audit log
```

---

## Conceptual Foundation
This project operationalizes the following AGI Future Foundation PBC frameworks:

| Framework | Implementation |
|---|---|
| **Institutional AGI Framework** | Agent role definition, tool boundaries, policy overlays |
| **Fiduciary Shield** | Hard constraints: no fund transfers, human sign-off required |
| **Institutional Grid** | Ruleset structure encoding public-benefit obligations |
| **Governance Engine** | Proposal → evaluation → decision → follow-up pipeline |
| **AGI Institutional Ledger** | Governance Ledger (JSONL) with hashed, auditable entries |
| **Bodhi Realtime Agent** | Voice Interface Layer with non-blocking background sub-agents |
| **Agentic Web Architecture** | Multi-channel delivery: GitHub, Telegram, Discord, Voice |

---

## 🛠 Builders & Investors
We are actively seeking contributors and strategic partners to expand the Institutional Grid.

* **Builders**: Join our ecosystem to build the next generation of agentic governance tools. Check out the [MIKE-OGI-Framework](https://github.com/AGI-Corporation/agi-governance-copilot/wiki/MIKE-OGI-Framework) to start building sub-agents.
* **Investors**: Align with the OGI model. For partnership inquiries and strategic collaboration, please reach out via the contact info below.

---

## 📧 Contact & Support

* **General Inquiries**: [contact@agicorp.network](mailto:contact@agicorp.network)
* **Technical (M.I.K.E.)**: [mike@agicorp.network](mailto:mike@agicorp.network)
* **Support**: [hello@maxhealth.tech](mailto:hello@maxhealth.tech)
* **Website**: [www.agicorp.network](https://www.agicorp.network)
* **Social**: [LinkedIn](https://www.linkedin.com/in/infogurus) | [X (Twitter)](https://x.com/idescidude)

---

## Safety & Trust Design
- **Advisory only**: the agent never holds or moves funds; all outputs are drafts for human review
- **Policy-grounded outputs**: every evaluation cites specific rule clauses
- **Auditable ledger**: all tool calls logged with timestamps and content hashes
- **No credential storage**: API keys loaded from environment variables only
- **Open-source**: full source available for inspection and audit

---

## License
MIT License — see [LICENSE](LICENSE)

---

## Contributing
PRs welcome. See [docs/architecture.md](docs/architecture.md) to understand the design. All contributions must maintain the advisory-only safety model and open governance ledger.

---

## Links
- GCC Foundation: https://www.gccofficial.org/en
- GCC OpenClaw Grants: https://github.com/gcc-foundation/gcc-openclaw-grants
- Bodhi Realtime Agent: https://github.com/AGI-Corporation/bodhi_realtime_agent
- AGI Corporation: https://www.agicorp.network
- AGI Future Foundation: https://www.agicorp.network
- AGI Future Foundationyou tube : (https://www.youtube.com/@AGI-Corp)
