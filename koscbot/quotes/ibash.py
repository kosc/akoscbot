import httpx
from bs4 import BeautifulSoup


async def random_ibash_quote():
    async with httpx.AsyncClient() as client:
        r = await client.get("http://ibash.org.ru/random.php")
        soup = BeautifulSoup(r.content)
        quote_id = soup.find("div", "quothead").find("b").get_text()[1:]
        quote_body = soup.find("div", "quotbody").get_text("\n")
        quote = quote_body + "\n\n © http://ibash.org.ru/quote.php?id=" + quote_id
        return quote
