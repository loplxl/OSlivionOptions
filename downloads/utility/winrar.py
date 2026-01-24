import aiohttp
from bs4 import BeautifulSoup
from pathlib import Path
async def getURL(ssl_ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.win-rar.com/postdownload.html",ssl=ssl_ctx) as resp:
            resp.raise_for_status()
            html = await resp.text()
    soup = BeautifulSoup(html,"html.parser")
    url = soup.find("a",class_="postdownloadlink")['href']
    download_path = Path.home() / "Downloads" / url.rsplit("/",1)[1]
    return "https://www.win-rar.com" + url,download_path