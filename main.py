import logging
import re
from os import environ
from typing import Optional, Union

from telegram import Update, Message
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from telegram.ext._utils.types import FilterDataDict
from telegram.ext.filters import MessageFilter


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.WARN
)


PIZDA_RE = re.compile(".*[Дд][Аа]\W*")


class PizdaFilter(MessageFilter):
    def filter(self, message: Message) -> Optional[Union[bool, FilterDataDict]]:
        if message.text is None:
            return False
        return PIZDA_RE.match(message.text)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Привет, это я, Филипп Киркоров!')


async def pizda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        update.effective_chat.id,
        'Пизда!',
        reply_to_message_id=update.message.message_id
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token(environ['BOT_TOKEN']).build()

    start_handler = CommandHandler('start', start, block=False)
    pizda_handler = MessageHandler(PizdaFilter(), pizda, block=False)

    application.add_handler(pizda_handler)
    application.add_handler(start_handler)

    application.run_polling()
