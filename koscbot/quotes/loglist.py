import json
import httpx


async def random_loglist_quote():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://loglist.xyz/api/quote/random")
        quote_id = json.loads(r.content)['id']
        quote_body = json.loads(r.content)['content']
        quote = quote_body + "\n\n © https://loglist.xyz/quote/" + quote_id
        return quote
