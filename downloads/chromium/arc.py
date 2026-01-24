from pathlib import Path
async def getURL(ssl_ctx):
    return "https://releases.arc.net/windows/ArcInstaller.exe",(Path.home() / "Downloads" / "ArcInstaller.exe")