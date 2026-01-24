from pathlib import Path
async def getURL(ssl_ctx):
    return "https://github.com/zen-browser/desktop/releases/latest/download/zen.installer.exe",(Path.home() / "Downloads" / "zen.installer.exe")