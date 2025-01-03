import os
import boto3
from datetime import datetime
from config import STORAGE_TYPE, S3_BUCKET, AWS_ACCESS_KEY, AWS_SECRET_KEY, UPLOADS_DIR

class StorageManager:
    def __init__(self):
        self.storage_type = STORAGE_TYPE
        if self.storage_type == 's3':
            self.s3_client = boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY,
                aws_secret_access_key=AWS_SECRET_KEY
            )
    
    def save_file(self, file, project_id):
        """Save uploaded file to either local storage or S3"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{project_id}_{timestamp}_{file.name}"
        
        if self.storage_type == 'local':
            filepath = os.path.join(UPLOADS_DIR, filename)
            with open(filepath, 'wb') as f:
                f.write(file.getbuffer())
            return filepath
        else:
            self.s3_client.upload_fileobj(file, S3_BUCKET, filename)
            return f"s3://{S3_BUCKET}/{filename}"
    
    def get_file_url(self, filepath):
        """Get URL for accessing the file"""
        if self.storage_type == 'local':
            return filepath
        else:
            return self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': S3_BUCKET, 'Key': filepath.split('/')[-1]},
                ExpiresIn=3600
            )