from pydantic import BaseModel, Field, HttpUrl, field_validator
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

class Project(BaseModel):
    project_id: UUID = Field(default_factory=uuid4)
    project_name: str = Field(..., min_length=1, max_length=100)
    tech_arch_diagram: Optional[str] = Field(default="")
    delivery_plan: str = Field(..., min_length=1)
    non_functional_requirement: str = Field(..., min_length=1)
    team: str = Field(..., min_length=1)
    scope: str = Field(..., min_length=1)
    ado_link: HttpUrl
    infra_diagram: Optional[str] = Field(default="")
    cicd_pipelines: str = Field(..., min_length=1)
    formatting_tools: str = Field(..., min_length=1)
    linting_tools: str = Field(..., min_length=1)
    code_quality_checks: str = Field(..., min_length=1)
    created_at: datetime = Field(default_factory=datetime.now)

    @field_validator('project_name')
    def name_must_be_valid(cls, v):
        if not v.strip():
            raise ValueError('Project name cannot be empty')
        return v.strip()