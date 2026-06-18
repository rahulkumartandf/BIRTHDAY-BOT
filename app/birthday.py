from datetime import datetime

from sheets import GoogleSheets
from templates import generate

from logger import get_logger

logger = get_logger()


class BirthdayService:

    def __init__(self, config):

        self.config = config

        self.sheet = GoogleSheets(
            "config/google-service-account.json",
            config["env"]["sheet_id"]
        )

    def run(self):

        today = datetime.now().strftime("%d-%m")

        rows = self.sheet.get_records()

        for row in rows:

            if row["Birthday"] != today:
                continue

            message = generate(row["Name"])

            logger.info(message)

            # Provider selection would go here.
            # Example:
            # provider.send(row["Phone"], message)

            logger.info(f"Birthday processed for {row['Name']}")