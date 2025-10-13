import asyncio
import sqlite3
from tools.jsonhandler import log
from keys.not_a_token import _token
from text_data.sm import dev_profile, scenario
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    Updater,
    filters,
)
import time


class tg_bot:
    def __init__(
        self,
        token_bot,
    ):
        self.token_bot = token_bot
        self.application = None

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        log.info("user want to see start menu")
        await update.message.reply_text(dev_profile)

    async def options(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        option = update.message.text.strip()[1:]
        log.info(scenario[option]["log"])
        await update.message.reply_text(scenario[option]["statment"])
        if "links" in scenario[option]:
            for name, link in scenario[option]["links"].items():
                await update.message.reply_text(link)

    async def show_log(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        strings = ""
        try:
            with open("logger/logger.txt") as file:
                c = 0
                for line in file:
                    strings += line
                    c += 1
                if c > 100:
                    open(file, "w")
                    await update.message.reply_text("File now is empty")
                    log.info("file is empty")
                    c = 0
            await update.message.reply_text(strings)
        except Exception as exc:
            log.error(exc)
        await update.message.reply_text(f"total line of logs is {c}")

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        log.info(f"{update.message.text}")
        await update.message.reply_text(update.message.text)

    async def post_init(self, application: Application):
        await application.bot.set_my_commands(
            [
                ("start", "Show main menu"),
                ("projects", "View my projects"),
                ("showskils", "See my skills"),
                ("contact", "Contact information"),
                ("help", "Show help menu"),
                ("show_logs", "Show last 100 lines of logs"),
                ("exit", "exit stupid as nigga"),
            ]
        )

    def main(self):
        self.application = Application.builder().token(self.token_bot).build()
        log.info("resive message")
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.post_init = self.post_init
        self.application.add_handler(CommandHandler("show_logs", self.show_log))
        self.application.add_handler(
            CommandHandler(
                ["help", "projects", "showskils", "contact", "exit"], self.options
            )
        )

        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo)
        )

        log.info("handling message")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)

    def run(self):
        try:
            self.main()
        except Exception as exc:
            log.error(exc)


first_et = tg_bot(token_bot=_token)
asyncio.run(first_et.run())
