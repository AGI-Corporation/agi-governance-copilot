"""AGI Governance Copilot - OpenClaw Agent Core"""

import os
import json
import hashlib
from datetime import datetime, UTC
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

load_dotenv()


class GovernanceCopilot:
    """
    Core governance agent built on OpenClaw.
    Implements the AGI Future Foundation's Fiduciary Shield and Governance Engine
    as an advisory-only, policy-bound AI agent.

    SAFETY CONTRACT:
    - This agent NEVER transfers funds or modifies on-chain state.
    - All recommendations require explicit human sign-off before action.
    - Every tool call is logged to the Governance Ledger.
    """

    def __init__(self, config_path: str = "config/agent-config.yaml"):
        self.config = self._load_config(config_path)
        self.ledger_path = self.config.get("ledger", {}).get("path", "governance-ledger.jsonl")
        self.policies = self._load_policies()

    def _load_config(self, path: str) -> dict:
        import yaml
        config_file = Path(path)
        if not config_file.exists():
            # Fall back to example config for demos
            config_file = Path("config/agent-config.example.yaml")
        with open(config_file) as f:
            return yaml.safe_load(f)

    def _load_policies(self) -> str:
        """Load DAO rules and public goods principles into agent context"""
        policies = []
        for policy_key in ["dao_rules", "public_goods_principles"]:
            path = self.config.get("policies", {}).get(policy_key)
            if path and Path(path).exists():
                policies.append(Path(path).read_text())
        return "\n\n---\n\n".join(policies)

    def _call_llm(self, system_prompt: str, user_message: str) -> str:
        """Call the configured LLM provider via OpenClaw"""
        # OpenClaw integration point
        from openai import OpenAI
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model=self.config.get("llm", {}).get("model", "gpt-4o"),
            temperature=self.config.get("llm", {}).get("temperature", 0.2),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    def _log_to_ledger(self, action: str, input_data: Any, output_data: Any) -> str:
        """Append an entry to the Governance Ledger (audit log)"""
        entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "action": action,
            "input_hash": hashlib.sha256(json.dumps(input_data, default=str).encode()).hexdigest()[:16],
            "output_hash": hashlib.sha256(json.dumps(output_data, default=str).encode()).hexdigest()[:16],
            "input_preview": str(input_data)[:200],
        }
        with open(self.ledger_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
        return entry["input_hash"]

    def evaluate_proposal(self, proposal_path: str, rules_path: str = None) -> dict:
        """Evaluate a governance proposal. Returns verdict, score, reasoning, and policy refs."""
        from tools.evaluate_proposal import evaluate_proposal_tool
        proposal_text = Path(proposal_path).read_text()
        rules_text = Path(rules_path).read_text() if rules_path and Path(rules_path).exists() else ""
        result = evaluate_proposal_tool(
            proposal_text=proposal_text,
            rules_text=rules_text,
            policies=self.policies,
            llm_fn=self._call_llm,
        )
        self._log_to_ledger("evaluate_proposal", {"proposal": proposal_path}, result)
        return result

    def generate_impact_snapshot(self, project_path: str) -> dict:
        """Generate an impact snapshot for a funded project."""
        from tools.impact_snapshot import impact_snapshot_tool
        project_data = json.loads(Path(project_path).read_text())
        result = impact_snapshot_tool(
            project_data=project_data,
            policies=self.policies,
            llm_fn=self._call_llm,
        )
        self._log_to_ledger("generate_impact_snapshot", {"project": project_path}, result)
        return result

    def emit_governance_digest(self, since: str = "7d") -> dict:
        """Generate a governance digest for DAO stewards."""
        from tools.governance_digest import governance_digest_tool
        result = governance_digest_tool(
            since=since,
            config=self.config,
            llm_fn=self._call_llm,
        )
        self._log_to_ledger("emit_governance_digest", {"since": since}, result)
        return result

    def post_to_github(self, content: str, issue_number: int = None) -> None:
        """Post content to GitHub as an issue comment."""
        from github import Github
        g = Github(os.environ.get("GITHUB_TOKEN"))
        repo = g.get_repo(self.config.get("github", {}).get("repo", ""))
        if issue_number:
            issue = repo.get_issue(issue_number)
            issue.create_comment(content)
