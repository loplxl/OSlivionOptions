from pathlib import Path
async def getURL(ssl_ctx):
    return "https://downloads.malwarebytes.com/file/mb-windows",(Path.home() / "Downloads" / "MBSetup.exe")