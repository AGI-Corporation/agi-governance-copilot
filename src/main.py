"""AGI Governance Copilot - CLI Entrypoint"""

import click
import json
import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """AGI Governance Copilot - OpenClaw-powered DAO governance assistant"""
    pass


@cli.command()
@click.option("--proposal", "-p", required=True, help="Path to proposal JSON or Markdown file")
@click.option("--rules", "-r", default="config/example-dao-rules.md", help="Path to DAO rules file")
@click.option("--output", "-o", default=None, help="Output file path (JSON)")
def evaluate(proposal: str, rules: str, output: str):
    """Evaluate a governance proposal against DAO rules and fiduciary constraints"""
    from agent import GovernanceCopilot

    console.print(Panel(f"[bold blue]Evaluating proposal:[/bold blue] {proposal}", title="AGI Governance Copilot"))

    agent = GovernanceCopilot()
    result = agent.evaluate_proposal(proposal_path=proposal, rules_path=rules)

    # Display result
    table = Table(title="Evaluation Result")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="white")
    table.add_row("Verdict", f"[{'green' if result['verdict'] == 'Pass' else 'red'}]{result['verdict']}[/]")
    table.add_row("Score", str(result.get("score", "N/A")))
    table.add_row("Policy Refs", ", ".join(result.get("policy_references", [])))
    console.print(table)
    console.print(f"\n[bold]Reasoning:[/bold] {result.get('reasoning', '')}")

    if output:
        with open(output, "w") as f:
            json.dump(result, f, indent=2)
        console.print(f"\n[green]Saved to {output}[/green]")


@cli.command()
@click.option("--project", "-p", required=True, help="Path to project update JSON file")
@click.option("--output", "-o", default=None, help="Output file path (JSON)")
def impact(project: str, output: str):
    """Generate an impact snapshot for a funded project"""
    from agent import GovernanceCopilot

    console.print(Panel(f"[bold green]Generating impact snapshot:[/bold green] {project}", title="AGI Governance Copilot"))

    agent = GovernanceCopilot()
    result = agent.generate_impact_snapshot(project_path=project)

    console.print_json(json.dumps(result, indent=2))

    if output:
        with open(output, "w") as f:
            json.dump(result, f, indent=2)
        console.print(f"\n[green]Saved to {output}[/green]")


@cli.command()
@click.option("--since", default="7d", help="Time range for digest (e.g. 7d, 30d)")
@click.option("--post-github", is_flag=True, default=False, help="Post digest as GitHub issue comment")
def digest(since: str, post_github: bool):
    """Emit a governance digest summarizing pending proposals and project status"""
    from agent import GovernanceCopilot

    console.print(Panel(f"[bold yellow]Generating governance digest (last {since})[/bold yellow]", title="AGI Governance Copilot"))

    agent = GovernanceCopilot()
    result = agent.emit_governance_digest(since=since)

    console.print(result["markdown"])

    if post_github:
        agent.post_to_github(result["markdown"])
        console.print("[green]Posted to GitHub[/green]")


if __name__ == "__main__":
    cli()
