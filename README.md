# Project Tracker

A Streamlit application for tracking project details, requirements, and issues.

## Features

- Project management with detailed information capture
- Technical architecture and infrastructure diagram storage
- Issue tracking with status updates
- Support for both local and S3 storage
- Comprehensive project metadata tracking

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure storage:
   - Copy `.env.example` to `.env`
   - Update the environment variables as needed
   - For S3 storage, set `STORAGE_TYPE=s3` and provide AWS credentials

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Project Structure

```
├── app.py                 # Main Streamlit application
├── config.py             # Configuration management
├── data_manager.py       # Data operations and storage
├── storage.py            # File storage management (local/S3)
├── models/               # Pydantic models
│   ├── project.py       # Project data model
│   └── issue.py         # Issue tracking model
├── services/            # Business logic layer
│   ├── project_service.py  # Project operations
│   └── issue_service.py    # Issue management
├── utils/               # Utility functions
│   └── validators.py    # Data validation utilities
├── data/               # Local storage directory
│   ├── projects.csv    # Project data
│   ├── issues.csv      # Issue tracking data
│   └── uploads/        # Uploaded files directory
└── requirements.txt    # Python dependencies
```

## Components

### Models
- `Project`: Validates project data with fields for architecture, requirements, and team details
- `Issue`: Handles issue tracking with status management

### Services
- `ProjectService`: Manages project operations and data persistence
- `IssueService`: Handles issue creation, updates, and retrieval

### Storage
- Local Storage: Files stored in `data/uploads`
- S3 Storage: Remote storage in configured AWS S3 bucket

### Validation
- Pydantic models ensure data integrity
- Field-level validation for all inputs
- Type checking and data consistency

## Usage

1. Select or create a new project
2. Fill in project details:
   - Technical architecture diagram
   - Weekly delivery plan
   - Non-functional requirements
   - Team composition
   - Project scope
   - Infrastructure details
   - CI/CD configuration
   - Code quality tools
3. Track issues and improvements
4. Update issue status as needed