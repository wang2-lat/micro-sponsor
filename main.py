import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from models import Campaign, Influencer, Application
from storage import Storage

app = typer.Typer(help="Connect SaaS companies with micro-influencers")
console = Console()
storage = Storage()

@app.command()
def create_campaign(
    company: str = typer.Option(..., help="Company name"),
    product: str = typer.Option(..., help="Product name"),
    budget: int = typer.Option(..., help="Budget in USD"),
    audience: str = typer.Option(..., help="Target audience description"),
):
    """Create a new promotion campaign (for companies)"""
    campaign = Campaign(
        company=company,
        product=product,
        budget=budget,
        target_audience=audience
    )
    storage.add_campaign(campaign)
    console.print(f"[green]Campaign created successfully! ID: {campaign.id}[/green]")

@app.command()
def list_campaigns():
    """List all available campaigns (for influencers)"""
    campaigns = storage.get_campaigns()
    if not campaigns:
        console.print("[yellow]No campaigns available[/yellow]")
        return
    
    table = Table(title="Available Campaigns")
    table.add_column("ID", style="cyan")
    table.add_column("Company", style="magenta")
    table.add_column("Product", style="green")
    table.add_column("Budget", style="yellow")
    table.add_column("Target Audience")
    
    for campaign in campaigns:
        table.add_row(
            campaign.id,
            campaign.company,
            campaign.product,
            f"${campaign.budget}",
            campaign.target_audience
        )
    
    console.print(table)

@app.command()
def apply(
    campaign_id: str = typer.Option(..., help="Campaign ID to apply for"),
    name: str = typer.Option(..., help="Your name"),
    platform: str = typer.Option(..., help="Platform (e.g., Twitter, YouTube)"),
    followers: int = typer.Option(..., help="Number of followers"),
    rate: int = typer.Option(..., help="Your rate in USD"),
):
    """Apply for a campaign (for influencers)"""
    campaign = storage.get_campaign(campaign_id)
    if not campaign:
        console.print(f"[red]Campaign {campaign_id} not found[/red]")
        raise typer.Exit(1)
    
    influencer = Influencer(
        name=name,
        platform=platform,
        followers=followers,
        rate=rate
    )
    
    application = Application(
        campaign_id=campaign_id,
        influencer=influencer
    )
    
    storage.add_application(application)
    console.print(f"[green]Application submitted successfully! ID: {application.id}[/green]")

@app.command()
def list_applications(campaign_id: str = typer.Option(..., help="Campaign ID")):
    """List all applications for a campaign (for companies)"""
    applications = storage.get_applications_by_campaign(campaign_id)
    if not applications:
        console.print(f"[yellow]No applications for campaign {campaign_id}[/yellow]")
        return
    
    table = Table(title=f"Applications for Campaign {campaign_id}")
    table.add_column("ID", style="cyan")
    table.add_column("Influencer", style="magenta")
    table.add_column("Platform", style="green")
    table.add_column("Followers", style="yellow")
    table.add_column("Rate", style="red")
    
    for app in applications:
        table.add_row(
            app.id,
            app.influencer.name,
            app.influencer.platform,
            str(app.influencer.followers),
            f"${app.influencer.rate}"
        )
    
    console.print(table)

@app.command()
def show_campaign(campaign_id: str = typer.Argument(..., help="Campaign ID")):
    """Show detailed information about a campaign"""
    campaign = storage.get_campaign(campaign_id)
    if not campaign:
        console.print(f"[red]Campaign {campaign_id} not found[/red]")
        raise typer.Exit(1)
    
    panel = Panel(
        f"[bold]Company:[/bold] {campaign.company}\n"
        f"[bold]Product:[/bold] {campaign.product}\n"
        f"[bold]Budget:[/bold] ${campaign.budget}\n"
        f"[bold]Target Audience:[/bold] {campaign.target_audience}\n"
        f"[bold]Created:[/bold] {campaign.created_at}",
        title=f"Campaign {campaign.id}",
        border_style="green"
    )
    console.print(panel)

if __name__ == "__main__":
    app()
