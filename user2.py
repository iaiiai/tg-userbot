import telethon
from telethon import TelegramClient, sync, events
from telethon import types
import functools
import logging

from telethon.tl import custom

logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=logging.ERROR, filename=u'bug.log')

api_id = 874359
api_hash = '809c5b27a33313cf907f5295922b9dfc'

client = TelegramClient('saa', api_id, api_hash).start()
def is_offline(fun):
    @functools.wraps(fun)
    async def wrapper(event: custom.Message):
        me: types.User = await client.get_entity('zmey_g')  # username for your second account we're checking

        if isinstance(me, types.User) and not isinstance(me.status, types.UserStatusOnline):
            await fun(event)

    return wrapper


@client.on(events.NewMessage(func=lambda message: message.is_private))
@is_offline
async def replier(event: custom.Message):
    await event.reply("Приветствую, я **Альфред - дворецкий**. Босс занят, скорее всего он спасает город. Оставьте ваше сообщение или напишите позже.")


client.run_until_disconnected()


