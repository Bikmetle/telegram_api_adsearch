import configparser
from telethon.sync import TelegramClient, events
from telethon.errors import MessageIdInvalidError

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']
username = config['Telegram']['username']


client = TelegramClient("aliev_mto", api_id, api_hash).start()
me = client.get_me()

try:
    @client.on(events.NewMessage(pattern='.*(?i)(квартир|риелтор).*'))
    async def handler(event):
        chat_id = event.chat_id
        message_id = event.id
        # sender = await event.get_sender()
        await client.forward_messages(me.id, message_id, chat_id)
        print(event.message.message, '\n### ### ### ### ###\n')
except MessageIdInvalidError:
    print('error occur\n### ### ### ### ###\n')

client.run_until_disconnected()
