from tools.bot import *
from keys.tools.ask_your_token import ask_your_token
from keys.token import token
import asyncio

ask_your_token()
first_et = tg_bot(token_bot=token)
asyncio.run(first_et.run())