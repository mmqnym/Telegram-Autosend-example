# Telegram auto send message
Display how to auto send message in telegram bot

## Reference

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [schedule.py](https://schedule.readthedocs.io/en/stable/)

## How to get telegram chat_id

> First, You need to find telegram chat_id for auto send message to a group or channel.
1. Add the bot to the channel or group you want.
2. Send a message on the channel or group you choosed.
3. Enter `https://api.telegram.org/<Your bot token>/getUpdates` in your browser and you will see that the json file on the page contains the record of the message you just sent.
4. Find `id` in the `chat` block, which is the chat_id we are looking for.

> Paste the chat_id to complete the auto send function.
``` python
bot.sendMessage( chat_id = <You found chat_id>, text = msg, parse_mode = 'markdown' )
```

## License
[MIT License](https://github.com/0xmimiQ/telegram_autosend/blob/main/LICENSE)
