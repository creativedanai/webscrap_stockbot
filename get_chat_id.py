import time
import telepot
from telepot.loop import MessageLoop

def action(msg):
    chat_id = msg['chat']['id']
    print("Chat ID:", chat_id)
    
telegram_bot = telepot.Bot('6263893805:AAG_kwV3T3p5Fv_PxsrczwX5jBXv_kWsias')
MessageLoop(telegram_bot, action).run_as_thread()
print ('[INFO] telegram bot sedang berjalan')    
while 1:
    time.sleep(1)
