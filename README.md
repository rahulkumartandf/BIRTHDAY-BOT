# 🎂 Birthday Automation

A Python-based birthday reminder and messaging system.

## Features

- Google Sheets integration
- Daily birthday detection
- Random message templates
- Logging
- Duplicate prevention
- Docker support
- GitHub Actions scheduling
- Pluggable messaging providers

---

## Project Structure

```
birthday-bot/
├── app/
├── config/
├── logs/
├── tests/
├── requirements.txt
└── README.md
```

---

## Google Sheet

| Name | Birthday | Phone | Group | Status |
|------|----------|--------|--------|--------|
| Rahul | 18-06 | +91XXXXXXXXXX | Cricket | Pending |

Birthday format:

```
DD-MM
```

---

## Installation

```bash
git clone https://github.com/yourname/birthday-bot.git

cd birthday-bot

python -m venv venv

source venv/bin/activate
# Windows:
# venv\\Scripts\\activate

pip install -r requirements.txt
```

---

## Configuration

Copy:

```
.env.example
```

to

```
.env
```

Fill in:

- Google Sheet ID
- Service Account JSON
- Timezone
- Messaging provider credentials (for supported providers)

---

## Running

```bash
python app/main.py
```

or

```bash
python app/scheduler.py
```

---

## Deployment

### GitHub Actions

The included workflow runs daily at **08:00 IST**.

### Docker

```bash
docker compose up -d
```

---

## Extending

Messaging providers implement a common interface, making it straightforward to add support for additional **officially supported** services without changing the core birthday logic.

---

## Logging

Logs are written to:

```
logs/birthday.log
```

Each successful run records the processed birthdays to help prevent duplicate notifications.

---

## License

MIT License