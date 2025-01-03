import pandas as pd
import os
from config import PROJECTS_FILE, ISSUES_FILE

class DataManager:
    def __init__(self):
        self.init_data_files()
    
    def init_data_files(self):
        """Initialize data files if they don't exist"""
        if not os.path.exists(PROJECTS_FILE):
            pd.DataFrame({
                'project_id': [],
                'project_name': [],
                'tech_arch_diagram': [],
                'delivery_plan': [],
                'nfr': [],
                'team': [],
                'scope': [],
                'ado_link': [],
                'infra_diagram': [],
                'cicd_pipelines': [],
                'formatting_tools': [],
                'linting_tools': [],
                'code_quality_checks': [],
                'created_at': []
            }).to_csv(PROJECTS_FILE, index=False)
        
        if not os.path.exists(ISSUES_FILE):
            pd.DataFrame({
                'issue_id': [],
                'project_id': [],
                'description': [],
                'status': [],
                'created_at': [],
                'updated_at': []
            }).to_csv(ISSUES_FILE, index=False)
    
    def get_projects(self):
        """Get all projects"""
        return pd.read_csv(PROJECTS_FILE)
    
    def get_project(self, project_id):
        """Get specific project details"""
        projects = pd.read_csv(PROJECTS_FILE)
        return projects[projects['project_id'] == project_id].iloc[0]
    
    def save_project(self, project_data):
        """Save or update project data"""
        projects = pd.read_csv(PROJECTS_FILE)
        if project_data['project_id'] in projects['project_id'].values:
            projects.loc[projects['project_id'] == project_data['project_id']] = project_data
        else:
            projects = pd.concat([projects, pd.DataFrame([project_data])], ignore_index=True)
        projects.to_csv(PROJECTS_FILE, index=False)
    
    def get_issues(self, project_id):
        """Get issues for a specific project"""
        issues = pd.read_csv(ISSUES_FILE)
        return issues[issues['project_id'] == project_id]
    
    def save_issue(self, issue_data):
        """Save or update issue"""
        issues = pd.read_csv(ISSUES_FILE)
        if issue_data['issue_id'] in issues['issue_id'].values:
            issues.loc[issues['issue_id'] == issue_data['issue_id']] = issue_data
        else:
            issues = pd.concat([issues, pd.DataFrame([issue_data])], ignore_index=True)
        issues.to_csv(ISSUES_FILE, index=False)
    
    def update_issue_status(self, issue_id, status):
        """Update issue status"""
        issues = pd.read_csv(ISSUES_FILE)
        issues.loc[issues['issue_id'] == issue_id, 'status'] = status
        issues.loc[issues['issue_id'] == issue_id, 'updated_at'] = pd.Timestamp.now()
        issues.to_csv(ISSUES_FILE, index=False)