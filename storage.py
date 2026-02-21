import json
from pathlib import Path
from typing import List, Optional
from models import Campaign, Application

class Storage:
    def __init__(self, data_dir: str = ".micro-sponsor"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.campaigns_file = self.data_dir / "campaigns.json"
        self.applications_file = self.data_dir / "applications.json"
        self._init_files()
    
    def _init_files(self):
        if not self.campaigns_file.exists():
            self.campaigns_file.write_text("[]")
        if not self.applications_file.exists():
            self.applications_file.write_text("[]")
    
    def add_campaign(self, campaign: Campaign):
        campaigns = self.get_campaigns()
        campaigns.append(campaign)
        self.campaigns_file.write_text(
            json.dumps([c.model_dump() for c in campaigns], indent=2)
        )
    
    def get_campaigns(self) -> List[Campaign]:
        data = json.loads(self.campaigns_file.read_text())
        return [Campaign(**c) for c in data]
    
    def get_campaign(self, campaign_id: str) -> Optional[Campaign]:
        campaigns = self.get_campaigns()
        for campaign in campaigns:
            if campaign.id == campaign_id:
                return campaign
        return None
    
    def add_application(self, application: Application):
        applications = self.get_applications()
        applications.append(application)
        self.applications_file.write_text(
            json.dumps([a.model_dump() for a in applications], indent=2)
        )
    
    def get_applications(self) -> List[Application]:
        data = json.loads(self.applications_file.read_text())
        return [Application(**a) for a in data]
    
    def get_applications_by_campaign(self, campaign_id: str) -> List[Application]:
        applications = self.get_applications()
        return [a for a in applications if a.campaign_id == campaign_id]
