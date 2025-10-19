from tools.bot import *
from keys.tools.ask_your_token import ask_your_token
from keys._token import _token
import asyncio

ask_your_token()
first_et = tg_bot(token_bot=_token)
asyncio.run(first_et.run())