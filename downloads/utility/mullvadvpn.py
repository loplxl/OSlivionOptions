import aiohttp
from pathlib import Path
async def getURL(ssl_ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://github.com/mullvad/mullvadvpn-app/releases/latest", allow_redirects=True,ssl=ssl_ctx) as resp:
            resp.raise_for_status()
            redirecturl = str(resp.url)
    version = redirecturl.rsplit("/",1)[1]
    url = f"https://github.com/mullvad/mullvadvpn-app/releases/download/{version}/MullvadVPN-{version}_x64.exe"
    return url,(Path.home() / "Downloads" / f"MullvadVPN-{version}_x64.exe")