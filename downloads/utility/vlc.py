import aiohttp
from bs4 import BeautifulSoup
from pathlib import Path
async def getURL(ssl_ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.videolan.org/vlc/download-windows.html",ssl=ssl_ctx) as resp:
            resp.raise_for_status()
            html = await resp.text()
    soup = BeautifulSoup(html,"html.parser")
    url = soup.find("a", href=lambda href: href and "win64.exe" in href.lower())['href']
    filename = url.rsplit("/",1)[1]
    download_path = Path.home() / "Downloads" / filename
    return "https:" + url,download_path