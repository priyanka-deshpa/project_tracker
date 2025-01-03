from typing import Optional
from pydantic import ValidationError
from models.project import Project
from models.issue import Issue

def validate_project_data(data: dict) -> Optional[Project]:
    try:
        return Project(**data)
    except ValidationError as e:
        return None

def validate_issue_data(data: dict) -> Optional[Issue]:
    try:
        return Issue(**data)
    except ValidationError as e:
        return None