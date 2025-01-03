import streamlit as st
from datetime import datetime
import uuid
from services.project_service import ProjectService
from services.issue_service import IssueService
from storage import StorageManager

# Initialize services
project_service = ProjectService()
issue_service = IssueService()
storage_manager = StorageManager()

def init_session_state():
    if 'current_project' not in st.session_state:
        st.session_state.current_project = None
    if 'show_project_form' not in st.session_state:
        st.session_state.show_project_form = False

def render_project_selector():
    projects = project_service.get_all_projects()
    project_names = projects['project_name'].tolist()
    project_names.insert(0, "Create New Project")
    
    selected_project = st.selectbox("Select Project", project_names)
    
    if selected_project == "Create New Project":
        st.session_state.current_project = None
        st.session_state.show_project_form = True
    else:
        project_id = projects[projects['project_name'] == selected_project]['project_id'].iloc[0]
        st.session_state.current_project = project_id
        st.session_state.show_project_form = True
    
    return selected_project

def render_project_form():
    # Get existing project data if editing
    project_data = {}
    if st.session_state.current_project:
        project = project_service.get_project(st.session_state.current_project)
        if project:
            project_data = project.model_dump()

    with st.form("project_form"):
        project_name = st.text_input("Project Name", value=project_data.get('project_name', ''))
        
        st.subheader("Technical Architecture")
        tech_arch_file = st.file_uploader("Upload Technical Architecture Diagram", type=['png', 'jpg', 'pdf'])
        
        st.subheader("Project Details")
        delivery_plan = st.text_area("Weekly Delivery Plan", value=project_data.get('delivery_plan', ''))
        nfr = st.text_area("Non-Functional Requirements", value=project_data.get('nfr', ''))
        team = st.text_area("Development Team", value=project_data.get('team', ''))
        scope = st.text_area("High Level Scope", value=project_data.get('scope', ''))
        
        st.subheader("Links and Tools")
        ado_link = st.text_input("ADO Boards Link", value=project_data.get('ado_link', ''))
        infra_diagram = st.file_uploader("Infrastructure Diagram", type=['png', 'jpg', 'pdf'])
        cicd_pipelines = st.text_area("CICD Pipelines", value=project_data.get('cicd_pipelines', ''))
        formatting_tools = st.text_input("Formatting Tools", value=project_data.get('formatting_tools', ''))
        linting_tools = st.text_input("Linting Tools", value=project_data.get('linting_tools', ''))
        code_quality = st.text_area("Code Quality Checks in CICD", value=project_data.get('code_quality_checks', ''))
        
        submitted = st.form_submit_button("Save Project")
        
        if submitted:
            try:
                project_data = {
                    'project_id': st.session_state.current_project or str(uuid.uuid4()),
                    'project_name': project_name,
                    'tech_arch_diagram': storage_manager.save_file(tech_arch_file, project_name) if tech_arch_file else project_data.get('tech_arch_diagram', ''),
                    'delivery_plan': delivery_plan,
                    'nfr': nfr,
                    'team': team,
                    'scope': scope,
                    'ado_link': ado_link,
                    'infra_diagram': storage_manager.save_file(infra_diagram, project_name) if infra_diagram else project_data.get('infra_diagram', ''),
                    'cicd_pipelines': cicd_pipelines,
                    'formatting_tools': formatting_tools,
                    'linting_tools': linting_tools,
                    'code_quality_checks': code_quality,
                }
                
                project = project_service.create_or_update_project(project_data)
                if project:
                    st.success("Project saved successfully!")
                    st.session_state.current_project = str(project.project_id)
                    st.experimental_rerun()
                else:
                    st.error("Invalid project data. Please check all fields.")
            except Exception as e:
                st.error(f"Error saving project: {str(e)}")

def render_issues_section():
    if not st.session_state.current_project:
        return

    st.header("Issues and Improvements")
    
    issues = issue_service.get_project_issues(st.session_state.current_project)
    if issues:
        st.subheader("Existing Issues")
        for issue in issues:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(issue.description)
            with col2:
                new_status = st.selectbox(
                    "Status",
                    ["Pending", "Completed"],
                    key=f"status_{issue.issue_id}",
                    index=0 if issue.status == "Pending" else 1
                )
                if new_status != issue.status:
                    issue_service.update_issue_status(str(issue.issue_id), new_status)
    
    st.subheader("Add New Issue")
    with st.form("new_issue"):
        description = st.text_area("Issue Description")
        submitted = st.form_submit_button("Add Issue")
        
        if submitted and description:
            issue_data = {
                'issue_id': str(uuid.uuid4()),
                'project_id': st.session_state.current_project,
                'description': description,
                'status': "Pending",
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat()
            }
            
            issue = issue_service.create_issue(issue_data)
            if issue:
                st.success("Issue added successfully!")
                st.experimental_rerun()
            else:
                st.error("Invalid issue data. Please check the description.")

def main():
    st.title("Project Tracker")
    
    init_session_state()
    selected_project = render_project_selector()
    
    if st.session_state.show_project_form:
        render_project_form()
        if st.session_state.current_project:
            render_issues_section()

if __name__ == "__main__":
    main()