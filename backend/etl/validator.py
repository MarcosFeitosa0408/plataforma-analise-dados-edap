class Validator:

    @staticmethod
    def validate(df):

        if df is None:
            raise ValueError("EMPTY_DATASET")

        if df.shape[0] == 0:
            raise ValueError("NO_ROWS")

        if df.shape[1] == 0:
            raise ValueError("NO_COLUMNS")

        null_columns = df.columns[df.isnull().all()]

        if len(null_columns) > 0:
            print("NULL_COLUMNS_DETECTED", list(null_columns))

        return True
