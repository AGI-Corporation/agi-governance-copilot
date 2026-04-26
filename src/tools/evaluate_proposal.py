"""Tool: evaluate_proposal - Evaluates a DAO governance proposal against fiduciary rules"""

import json
from typing import Callable


SYSTEM_PROMPT = """
You are a rigorous governance advisor for decentralized organizations.
You evaluate grant proposals and governance motions against the following policy framework:

{policies}

Your evaluation must:
1. Assess alignment with public-benefit and fiduciary principles
2. Score each Institutional Grid dimension (1-5): Public Benefit Breadth, Open-Source Contribution,
   Mission Alignment, Team Credibility, Technical Feasibility, Risk Profile
3. Return a verdict: Pass | Revise | Reject
4. Cite specific policy clauses (e.g. F-1, F-2, Fiduciary Obligation #3)
5. Be concise, specific, and honest

IMPORTANT: You are advisory only. Do not authorize or commit any funds.
All recommendations require human sign-off before any action.

Respond ONLY with valid JSON in this exact schema:
{{
  "verdict": "Pass|Revise|Reject",
  "score": <weighted_average_float 1.0-5.0>,
  "dimension_scores": {{
    "public_benefit_breadth": <1-5>,
    "open_source_contribution": <1-5>,
    "mission_alignment": <1-5>,
    "team_credibility": <1-5>,
    "technical_feasibility": <1-5>,
    "risk_profile": <1-5>
  }},
  "reasoning": "<2-4 sentence explanation>",
  "policy_references": ["<clause_id>", ...],
  "conditions": ["<condition if Revise verdict>"],
  "risk_flags": ["<any flags if applicable>"]
}}
"""


def evaluate_proposal_tool(
    proposal_text: str,
    rules_text: str,
    policies: str,
    llm_fn: Callable[[str, str], str],
) -> dict:
    """
    Evaluate a governance proposal.

    Args:
        proposal_text: The full text of the proposal (Markdown or plain text)
        rules_text: DAO-specific rules text
        policies: Loaded policy context (public goods principles + fiduciary shield)
        llm_fn: Callable that accepts (system_prompt, user_message) -> str

    Returns:
        dict with verdict, score, dimension_scores, reasoning, policy_references
    """
    combined_policies = policies
    if rules_text:
        combined_policies = f"DAO-SPECIFIC RULES:\n{rules_text}\n\n---\n\n{policies}"

    system_prompt = SYSTEM_PROMPT.format(policies=combined_policies)
    user_message = f"Please evaluate the following proposal:\n\n{proposal_text}"

    raw_response = llm_fn(system_prompt, user_message)

    # Parse JSON response, with fallback
    try:
        # Strip markdown code fences if present
        clean = raw_response.strip()
        if clean.startswith("```"):
            clean = clean.split("```")[1]
            if clean.startswith("json"):
                clean = clean[4:]
        result = json.loads(clean.strip())
    except (json.JSONDecodeError, IndexError):
        result = {
            "verdict": "Revise",
            "score": 0.0,
            "reasoning": "Evaluation failed to parse. Raw response: " + raw_response[:500],
            "policy_references": [],
            "error": "parse_error",
        }

    return result
