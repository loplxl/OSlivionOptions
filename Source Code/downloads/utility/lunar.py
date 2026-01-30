from pathlib import Path
async def getURL(ssl_ctx,continuation,progressbar,completeDownload):
    await continuation("https://download.overwolf.com/install/Download?ExtensionId=jilehohlakeokncafogkgnicgndeecdiengddbcc",(Path.home() / "Downloads" / "Lunar Client - Installer.exe"))