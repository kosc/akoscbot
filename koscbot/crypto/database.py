import os
import asyncpg


async def get_conn():
    conn = await asyncpg.connect(
        user=os.environ.get('POSTGRES_USER', 'koscbot'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        database=os.environ.get('POSTGRES_DATABASE', 'koscbot'),
        host=os.environ.get('POSTGRES_HOST', '127.0.0.1')
    )
    return conn


async def get_cryptos():
    conn = await get_conn()
    cryptos = await conn.fetch(
        "SELECT crypto_currency FROM crypto_currencies;"
    )
    cryptos = map(lambda x: x['crypto_currency'], cryptos)
    return list(cryptos)


async def get_currencies():
    conn = await get_conn()
    currencies = await conn.fetch("SELECT currency FROM currencies;")
    currencies = map(lambda x: x['currency'], currencies)
    return list(currencies)
