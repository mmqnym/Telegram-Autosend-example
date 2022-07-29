import schedule
import time
import telegram

TOKEN = 'Your Token'
bot = telegram.Bot( token = TOKEN )

def job():
    msg = ''

    # Fill your chat_id here.
    bot.sendMessage( chat_id = 0, text = msg, parse_mode = 'markdown' )

    print( 'DONE this time' )
# job()

schedule.every( 10 ).hours.do( job )

while True:
    schedule.run_pending()
    time.sleep( 1 )
# while
