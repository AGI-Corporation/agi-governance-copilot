# AGI Future Foundation Public Goods Principles

This document encodes the public-benefit constraints from the AGI Future Foundation PBC's
Fiduciary Shield and Institutional Grid frameworks. These rules are loaded into the
Governance Copilot agent as binding policy overlays.

---

## Core Fiduciary Obligations

### 1. Public Benefit Priority
- All funded activities must primarily serve a broad public benefit, not private interests
- Proposals that concentrate benefit in fewer than 3 entities require additional scrutiny
- Funded work must produce open-source artifacts, public documentation, or accessible services

### 2. No Self-Dealing
- Proposal reviewers cannot evaluate proposals in which they have a financial interest
- Agent must flag any proposal where the requester also holds governance voting power > 10%
- Board members and advisors of the funding organization are ineligible as primary grantees

### 3. Transparency Requirements
- All funded grants must publish quarterly progress reports
- Budget breakdowns must be itemized at the task level
- Any scope changes exceeding 20% of budget require a formal amendment review

### 4. Open-Source Commitment
- Software deliverables must be released under OSI-approved licenses
- Research outputs must be published under Creative Commons or equivalent open licenses
- Datasets must be made publicly accessible within 90 days of project completion

---

## Fiduciary Shield Constraints

Derived from: AGI Future Foundation PBC - The AGI Fiduciary Shield (2024)

### F-1: Harm Prevention
- Projects must not create systems that could cause irreversible harm at scale
- AI/ML projects must include a documented risk assessment and mitigation plan
- Projects involving personal data must comply with GDPR/CCPA and include a privacy impact assessment

### F-2: Concentration of Power
- No single entity may receive more than 30% of total annual grant disbursements
- Projects that could create monopolistic control over critical digital infrastructure are ineligible
- Multi-stakeholder governance structures are preferred and scored higher in evaluation

### F-3: Reversibility
- Funded systems should be designed for graceful shutdown and data portability
- Irreversible decisions (e.g., token burns, permanent data deletion) require board ratification
- All smart contracts must include upgrade paths or sunset mechanisms

### F-4: Accountability
- All funded projects must designate a named accountability lead
- Projects with budgets > $10,000 require a mid-term review
- Projects with budgets > $50,000 require an independent third-party audit

---

## Institutional Grid: Evaluation Dimensions

Derived from: AGI Future Foundation PBC - The AGI Fiduciary Ecosystem Architecture (2024)

| Dimension | Weight | Description |
|---|---|---|
| Public Benefit Breadth | 25% | How many people benefit? How directly? |
| Open-Source Contribution | 20% | Quality and accessibility of open artifacts |
| Mission Alignment | 20% | Alignment with AGI safety and digital commons goals |
| Team Credibility | 15% | Track record, transparency, accountability structure |
| Technical Feasibility | 10% | Realistic milestones and resource planning |
| Risk Profile | 10% | Identification and mitigation of potential harms |

**Scoring:** Each dimension scored 1-5. Weighted total out of 5.0.
- 4.0-5.0: Strong recommendation to fund
- 3.0-3.9: Fund with conditions / milestones
- 2.0-2.9: Revise and resubmit
- Below 2.0: Decline

---

## Safety Principles for Agentic Systems

Derived from: AGI Future Foundation PBC - Blueprint for Responsible AI Governance (2024)

1. **Human oversight is non-negotiable**: The agent recommends; humans decide.
2. **Transparency by default**: Every output cites its sources and reasoning.
3. **Minimal footprint**: Agent requests only permissions needed for the current task.
4. **Fail safe**: When uncertain, the agent escalates to human review rather than proceeding.
5. **Auditability**: All agent actions are logged and human-readable.
