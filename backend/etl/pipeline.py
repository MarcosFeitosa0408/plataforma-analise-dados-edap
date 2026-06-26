from backend.etl.extractor import Extractor
from backend.etl.validator import Validator
from backend.etl.cleaner import Cleaner
from backend.etl.transformer import Transformer
from backend.etl.logger import ETLLogger


class ETLPipeline:

    def __init__(self):
        self.logger = ETLLogger()

    def run(self, file_path):

        self.logger.log("INICIO_ETL")

        data = Extractor.extract(file_path)
        self.logger.log("EXTRACTION_OK")

        Validator.validate(data)
        self.logger.log("VALIDATION_OK")

        data = Cleaner.clean(data)
        self.logger.log("CLEANING_OK")

        data = Transformer.transform(data)
        self.logger.log("TRANSFORM_OK")

        self.logger.log("ETL_FINISHED")

        return data
