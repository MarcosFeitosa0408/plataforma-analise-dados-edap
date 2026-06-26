class Cleaner:

    @staticmethod
    def clean(df):

        df = df.drop_duplicates()

        for col in df.select_dtypes(include=["number"]).columns:
            df[col] = df[col].fillna(df[col].median())

        for col in df.select_dtypes(include=["object"]).columns:
            df[col] = df[col].fillna("UNKNOWN")

        return df
