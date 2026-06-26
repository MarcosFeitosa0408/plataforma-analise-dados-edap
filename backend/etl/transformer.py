class Transformer:

    @staticmethod
    def transform(df):

        df.columns = [
            c.strip().lower().replace(" ", "_")
            for c in df.columns
        ]

        return df
