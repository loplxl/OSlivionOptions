from pathlib import Path
async def getURL(ssl_ctx):
    return "https://app.prntscr.com/build/setup-lightshot.exe",(Path.home() / "Downloads" / "setup-lightshot.exe")