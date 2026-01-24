from pathlib import Path
async def getURL(ssl_ctx):
    return "https://cdn.epicbrowser.com/winsetup/EpicSetup.exe",(Path.home() / "Downloads" / "EpicSetup.exe")