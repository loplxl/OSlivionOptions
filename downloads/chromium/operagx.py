from pathlib import Path
async def getURL(ssl_ctx):
    return "https://net.geo.opera.com/opera_gx/stable/windows",(Path.home() / "Downloads" / "OperaGXSetup.exe")