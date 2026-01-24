from pathlib import Path
async def getURL(ssl_ctx):
    return "https://net.geo.opera.com/opera/stable/windows",(Path.home() / "Downloads" / "OperaSetup.exe")