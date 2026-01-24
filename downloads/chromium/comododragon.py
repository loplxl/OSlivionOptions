from pathlib import Path
async def getURL(ssl_ctx):
    return "https://cdn.download.comodo.com/browser/release/dragon/x86/dragonsetup.exe",(Path.home() / "Downloads" / "dragonsetup.exe")