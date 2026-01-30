from pathlib import Path
async def getURL(ssl_ctx,continuation,progressbar,completeDownload):
    await continuation("https://absolllute.com/store/download?file=v8",(Path.home() / "Downloads" / "MegaHack_v8_installer.zip"))