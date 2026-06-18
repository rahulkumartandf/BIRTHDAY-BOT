import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]


class GoogleSheets:

    def __init__(self, credentials_file, sheet_id):

        creds = Credentials.from_service_account_file(
            credentials_file,
            scopes=SCOPES
        )

        client = gspread.authorize(creds)

        self.sheet = client.open_by_key(sheet_id).sheet1

    def get_records(self):

        return self.sheet.get_all_records()

    def update_status(self, row, status):

        self.sheet.update_cell(row, 5, status)