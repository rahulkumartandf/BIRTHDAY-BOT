# Birthday Bot

Uses Google Sheets + GitHub Actions.

## Setup
1. Create a Google Sheet with columns:
   Name | Birthday (DD-MM) | Phone | Facebook | Status
2. Create a Google Cloud service account and enable Sheets API.
3. Store credentials in GitHub Secrets:
   - GOOGLE_CREDENTIALS
   - SHEET_ID
   - WHATSAPP_TOKEN
4. Push this repository to GitHub.
