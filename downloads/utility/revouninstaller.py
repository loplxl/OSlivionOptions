from pathlib import Path
async def getURL(ssl_ctx):
    return "https://download.revouninstaller.com/download/revosetup.exe",(Path.home() / "Downloads" / "revosetup.exe")