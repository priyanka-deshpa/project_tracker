import os
from dotenv import load_dotenv

load_dotenv()

# Storage configuration
STORAGE_TYPE = os.getenv('STORAGE_TYPE', 'local')  # 'local', 's3'
S3_BUCKET = os.getenv('S3_BUCKET', '')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY', '')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY', '')

# Data storage paths
DATA_DIR = 'data'
PROJECTS_FILE = f'{DATA_DIR}/projects.csv'
ISSUES_FILE = f'{DATA_DIR}/issues.csv'
UPLOADS_DIR = f'{DATA_DIR}/uploads'

# Ensure required directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(UPLOADS_DIR, exist_ok=True)