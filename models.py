from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class Campaign(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    company: str
    product: str
    budget: int
    target_audience: str
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())

class Influencer(BaseModel):
    name: str
    platform: str
    followers: int
    rate: int

class Application(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    campaign_id: str
    influencer: Influencer
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
