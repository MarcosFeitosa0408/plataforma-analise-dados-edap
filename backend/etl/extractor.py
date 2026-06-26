import pandas as pd


class Extractor:

    @staticmethod
    def extract(file_path):

        if file_path.endswith(".csv"):
            return pd.read_csv(file_path)

        if file_path.endswith(".xlsx"):
            return pd.read_excel(file_path)

        if file_path.endswith(".json"):
            return pd.read_json(file_path)

        raise ValueError("FORMAT_NOT_SUPPORTED")
