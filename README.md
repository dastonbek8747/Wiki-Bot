# Wiki Telegram Bot

A Telegram bot that answers questions with Wikipedia.

## What it does

- Send any word or question to the bot.
- The bot searches Wikipedia.
- It sends back a short summary with a link to the full article.
- Send `/start` to get a short help message.

## Tech stack

- Python
- aiogram (Telegram bot framework)
- wikipedia (Wikipedia API)
- python-dotenv

## Setup

1. Create a bot with [@BotFather](https://t.me/BotFather) and copy the token.
2. Copy the example env file and add your token:

   ```bash
   cp .env.example .env
   # then edit .env and set BOT_TOKEN
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the bot:

   ```bash
   python bot.py
   ```

## Environment variables

| Name | Description |
|---|---|
| `BOT_TOKEN` | Telegram bot token from @BotFather |

## Project structure

```
bot.py     # bot entry point and handlers
wiki.py    # Wikipedia search helper
config.py  # loads environment variables
```

## License

MIT
