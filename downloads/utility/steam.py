from pathlib import Path
async def getURL(ssl_ctx):
    return "https://cdn.fastly.steamstatic.com/client/installer/SteamSetup.exe",(Path.home() / "Downloads" / "SteamSetup.exe")