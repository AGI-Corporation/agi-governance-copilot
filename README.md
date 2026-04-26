<p align="center">
  <img src="https://raw.githubusercontent.com/AGI-Corporation/agi-governance-copilot/main/assets/header-wiki.svg" width="100%" alt="AGI Governance Copilot Header">
</p>

# AGI Governance Copilot 🛡️🏛️

> **An OpenClaw-powered agentic governance assistant for DAOs and public-goods funds — built on the AGI Future Foundation's Institutional AGI, Fiduciary Shield, and Governance Engine frameworks.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Built with OpenClaw](https://img.shields.io/badge/Built%20with-OpenClaw-purple)](https://github.com/gcc-foundation/openclaw)
[![GCC Agentic Public Goods Track](https://img.shields.io/badge/GCC-Agentic%20Public%20Goods-green)](https://www.gccofficial.org/en)
[![Documentation](https://img.shields.io/badge/docs-Wiki-blue)](https://github.com/AGI-Corporation/agi-governance-copilot/wiki)

---

## 🌐 Overview

The **AGI Governance Copilot** is the first reference implementation of the [AGI Future Foundation PBC](https://www.agifuturefoundation.org)'s **Institutional AGI** governance architecture. By leveraging the [OpenClaw](https://github.com/gcc-foundation/openclaw) framework, it provides a transparent, auditable, and safe way for decentralized organizations to:

*   **Triage Proposals**: Automatically evaluate governance requests against complex fiduciary and public-benefit rules.
*   **Allocate Grants**: Structure milestone-based funding pipelines with AI-generated decision memos.
*   **Track Impact**: Monitor project progress via **Impact Snapshots** and verifiable performance scoring.
*   **Audit Everything**: Maintain a tamper-evident **Governance Ledger** for every agent action.

---

## 🏗️ System Architecture

```mermaid
graph TD
    subgraph Interface ["🌐 Interface Layer"]
        TG["Telegram / Discord"]
        GH["GitHub Issues"]
        CLI["CLI Tool"]
    end

    subgraph Brain ["🧠 Governance Brain (OpenClaw)"]
        AGENT["AGI Copilot Agent"]
        RULES["AGI Future Foundation Rules"]
        CHARTER["DAO Charter / Policy"]
        
        AGENT -->|Consults| RULES
        AGENT -->|Consults| CHARTER
    end

    subgraph Tools ["🛠️ Execution Tools"]
        EVAL["evaluate_proposal"]
        IMPACT["generate_impact_snapshot"]
        DIGEST["emit_governance_digest"]
        LEDGER["ledger_logger"]
    end

    subgraph Safety ["🔒 Safety & Audit Layer"]
        GL["Governance Ledger (JSONL)"]
        FS["Fiduciary Shield (Constraints)"]
        HUMAN["Human Sign-off (M-of-N)"]
    end

    Interface -->|Input| AGENT
    AGENT -->|Triggers| Tools
    Tools -->|Logs| GL
    Tools -->|Outputs| Interface
    GL -->|Verifies| FS
    FS -->|Requires| HUMAN
```

### 🔄 Proposal Decision Flow
```mermaid
sequenceDiagram
    participant User as 👤 DAO Steward
    participant Agent as 🧠 AGI Copilot (OpenClaw)
    participant FS as 🛡️ Fiduciary Shield
    participant Tools as 🛠️ Governance Tools
    participant Ledger as 📜 Governance Ledger

    User->>Agent: Submit Proposal (GitHub/TG)
    Agent->>FS: Validate Request Safety
    FS-->>Agent: Check OK
    Agent->>Tools: evaluate_proposal(data)
    Tools->>Tools: Align with Public Benefit rules
    Tools-->>Agent: Evaluation Result + Citations
    Agent->>Ledger: Log Decision (Hash + Policy Ref)
    Agent-->>User: Return Decision Memo (Draft)
    Note over User: Human Review & Final Sign-off
```

---

## 🏆 GCC Agentic Public Goods Track

Built for the **GCC Agentic Public Goods** hackathon, focusing on transparent grant workflows and fiduciary AI safety.

| Feature | Implementation | Goal |
| :--- | :--- | :--- |
| **DAO Governance** | Automated proposal ingestion & rule compliance checks. | Efficiency |
| **Fund Allocation** | Tranche-based grant recommendations + milestone gates. | Accountability |
| **Impact Evaluation** | AI-generated **Impact Snapshots** with progress scoring. | Transparency |
| **Safety & Trust** | Advisory-only mode + tamper-evident Governance Ledger. | Trust |

---

## 🧠 Core Frameworks

This project operationalizes the [AGI Future Foundation](https://www.agifuturefoundation.org) concepts:

*   **Fiduciary Shield**: Hard-coded constraints ensuring the agent never unilaterally moves funds.
*   **Institutional Grid**: A structured repository of public-benefit obligations cited in every decision.
*   **M.I.K.E. Framework**: Master Intelligence & Knowledge Executive — orchestrating specialized AI personas.
*   **Governance Ledger**: A cryptographically hashed log of all AI reasoning steps.

---

## 🚀 Getting Started

### 📋 Prerequisites
*   Python 3.11+
*   OpenClaw (`pip install openclaw`)
*   OpenAI / Anthropic API Key

### 🛠️ Installation
```bash
git clone https://github.com/AGI-Corporation/agi-governance-copilot.git
cd agi-governance-copilot
pip install -r requirements.txt
```

---

## 📊 Usage Examples

### 1. Evaluate a Grant Proposal
```bash
python src/main.py evaluate --proposal examples/sample-proposal.json
```

**Example Agent Output (Impact Card):**
```markdown
### 🟢 Proposal Evaluation: Project 'Solar-Mesh'
- **Status**: RECOMMEND PASS
- **Alignment Score**: 9.2/10
- **Fiduciary Check**: Valid (No direct transfer requested)
- **Policy Citation**: Institutional Grid Clause 4.2.1 (Open Source Mandate)
- **Recommended Tranches**: 
  1. $5k on GitHub Repo Initialization
  2. $10k on MVP release
```

### 2. Generate Impact Snapshot
```bash
python src/main.py impact --project examples/sample-project-update.json
```

---

## 🔒 Safety & Trust Design

| Layer | Mechanism | Safety Purpose |
| :--- | :--- | :--- |
| **Constraint** | Advisory-Only | Prevent unauthorized fund movement. |
| **Audit** | Governance Ledger | Tamper-evident record of all AI logic. |
| **Policy** | Rule Grounding | Every output must cite the Institutional Grid. |
| **Human** | Human-in-the-loop | Final decision-making power rests with stewards. |

---

## 📈 Roadmap

```mermaid
timeline
    title AGI Governance Copilot Roadmap
    2025 Q2 : MVP Launch : GitHub Integration : Basic Proposal Evaluation
    2025 Q3 : M.I.K.E. Persona Orchestration : Multi-agent review pipeline
    2025 Q4 : OpenClaw-to-Chain : On-chain milestone verification
    2026 : Institutional Deployment : Global Public Goods Infrastructure
```

---

## 🤝 Contributing

We welcome contributions! Please see our [Wiki](https://github.com/AGI-Corporation/agi-governance-copilot/wiki) for deep technical specs.

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🔗 Links

*   **GCC Foundation**: [gccofficial.org](https://www.gccofficial.org/en)
*   **OpenClaw**: [github.com/gcc-foundation/openclaw](https://github.com/gcc-foundation/openclaw)
*   **AGI Future Foundation**: [agifuturefoundation.org](https://www.agifuturefoundation.org)
