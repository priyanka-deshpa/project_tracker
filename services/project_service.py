from typing import Optional
from models.project import Project
from data_manager import DataManager
from utils.validators import validate_project_data

class ProjectService:
    def __init__(self):
        self.data_manager = DataManager()
    
    def create_or_update_project(self, project_data: dict) -> Optional[Project]:
        validated_data = validate_project_data(project_data)
        if validated_data:
            self.data_manager.save_project(validated_data.model_dump())
            return validated_data
        return None
    
    def get_project(self, project_id: str) -> Optional[Project]:
        project_data = self.data_manager.get_project(project_id)
        return validate_project_data(project_data) if project_data is not None else None
    
    def get_all_projects(self):
        return self.data_manager.get_projects()