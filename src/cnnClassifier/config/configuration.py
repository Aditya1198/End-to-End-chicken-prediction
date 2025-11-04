from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
import os
from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig

# Get the project root directory - this should point to the root of the project
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = os.path.join(PROJECT_ROOT, CONFIG_FILE_PATH),
        params_filepath = os.path.join(PROJECT_ROOT, PARAMS_FILE_PATH)):

        # Convert string paths to Path objects
        self.config = read_yaml(Path(config_filepath))
        self.params = read_yaml(Path(params_filepath))
        
        # Create artifacts directory at project root level
        self.artifacts_dir = os.path.join(PROJECT_ROOT, self.config.artifacts_root)
        create_directories([self.artifacts_dir])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        # Use absolute paths based on project root
        root_dir = os.path.join(PROJECT_ROOT, config.root_dir)
        local_data_file = os.path.join(PROJECT_ROOT, config.local_data_file)
        unzip_dir = os.path.join(PROJECT_ROOT, config.unzip_dir)
        
        create_directories([root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(local_data_file),
            unzip_dir=Path(unzip_dir)
        )

        return data_ingestion_config