import os
import logging
from logging.handlers import RotatingFileHandler

from aiogram import Bot, Dispatcher, executor, types

from .crypto.rates import get_crypto_rates
from .quotes.ibash import random_ibash_quote
from .quotes.loglist import random_loglist_quote
from .switch import switch

API_TOKEN = os.environ.get('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        RotatingFileHandler('akoscbot.log', 'a', 50000, 5)
    ]
)


@dp.message_handler(commands=['start', 'help'])
async def send_message(message: types.Message):
    await message.reply(
        "Hello! This bot writen in Python as a pet project. "\
        "Source code: https://github.com/kosc/akoscbot"\
    )


@dp.message_handler(commands=['ibash'])
async def ibash_quote(message: types.Message):
    quote = await random_ibash_quote()
    await message.reply(quote, disable_web_page_preview=True)


@dp.message_handler(commands=['loglist'])
async def loglist_quote(message: types.Message):
    quote = await random_loglist_quote()
    await message.reply(quote, disable_web_page_preview=True)


@dp.message_handler(commands=['crypto'])
async def crypto_rates(message: types.Message):
    rates = await get_crypto_rates()
    await message.reply(rates, parse_mode='Markdown')

@dp.message_handler(commands=['switch'])
async def switch_layout(message: types.Message):
    if message.reply_to_message is None:
        await message.reply("Should be used as a reply only!")
    else:
        switched_message = switch(message.reply_to_message.text)
        await message.reply(switched_message)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
