import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataIngestionconfig)

## component-Data ingestion
class DataIngestion:
    def __init__(self, config:DataIngestionconfig):
        self.config = config

    # Method: Downloading the zip file
    def download_file(self):
        os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)

        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            print(f"{filename} downloaded! with following info: \n{headers}")
        else:
            print("File already exists")

    # Method: Extract the zip file
    def extract_zip_file(self):
        os.makedirs(self.config.unzip_dir, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        print(f"Extracted files to {self.config.unzip_dir}")