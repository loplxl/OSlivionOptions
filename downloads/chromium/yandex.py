from pathlib import Path
async def getURL(ssl_ctx):
    return "https://browser.yandex.com/download?os=win&bitness=64",(Path.home() / "Downloads" / "Yandex.exe")