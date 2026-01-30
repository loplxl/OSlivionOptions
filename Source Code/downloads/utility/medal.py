from pathlib import Path
async def getURL(ssl_ctx,continuation,progressbar,completeDownload):
    await continuation("https://install.medal.tv/",(Path.home() / "Downloads" / "MedalSetup.exe"))