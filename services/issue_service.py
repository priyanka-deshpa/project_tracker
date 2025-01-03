from typing import Optional, List
from models.issue import Issue
from data_manager import DataManager
from utils.validators import validate_issue_data

class IssueService:
    def __init__(self):
        self.data_manager = DataManager()
    
    def create_issue(self, issue_data: dict) -> Optional[Issue]:
        validated_data = validate_issue_data(issue_data)
        if validated_data:
            self.data_manager.save_issue(validated_data.model_dump())
            return validated_data
        return None
    
    def update_issue_status(self, issue_id: str, status: str) -> bool:
        return self.data_manager.update_issue_status(issue_id, status)
    
    def get_project_issues(self, project_id: str) -> List[Issue]:
        issues = self.data_manager.get_issues(project_id)
        return [validate_issue_data(issue) for issue in issues.to_dict('records') if validate_issue_data(issue)]