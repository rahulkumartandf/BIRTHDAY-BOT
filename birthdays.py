from datetime import datetime
print("Birthday job started")
today=datetime.now().strftime("%d-%m")
print("Today's date:",today)
# TODO: Read Google Sheet, find matching birthdays,
# generate message, send using supported API, update status.
