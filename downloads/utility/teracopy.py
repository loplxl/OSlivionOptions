from pathlib import Path
async def getURL(ssl_ctx):
    return "https://www.codesector.com/files/teracopy.exe",(Path.home() / "Downloads" / "teracopy.exe")