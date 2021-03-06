import json

import httpx

from .database import get_cryptos, get_currencies


async def get_crypto_rates():
    cryptos = await get_cryptos()
    currencies = await get_currencies()
    query = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={','.join(cryptos)}&tsyms={','.join(currencies)}"
    async with httpx.AsyncClient() as client:
        r = await client.get(query)
    message = "```\n"
    for crypto, rates in json.loads(r.content).items():
        message += crypto + ":\n"
        for currency, rate in rates.items():
            message += "    " + currency + ": " + (f"{rate:.2f}" if (currency in currencies) else rate) + "\n"
    message += "```"
    return message
