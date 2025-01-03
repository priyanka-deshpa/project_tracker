from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal
from uuid import UUID, uuid4

class Issue(BaseModel):
    issue_id: UUID = Field(default_factory=uuid4)
    project_id: UUID
    description: str = Field(..., min_length=1)
    status: Literal["Pending", "Completed"] = "Pending"
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)