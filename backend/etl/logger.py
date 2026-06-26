from datetime import datetime


class ETLLogger:

    def log(self, message):
        print(f"[ETL] {datetime.now().isoformat()} | {message}")
