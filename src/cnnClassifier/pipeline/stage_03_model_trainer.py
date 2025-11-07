from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Training
from cnnClassifier import logger

STAGE_NAME = "Training"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()

        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        model_trainer = Training(config=training_config)
        model_trainer.get_base_model()
        model_trainer.train_valid_generator()
        model_trainer.train()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  