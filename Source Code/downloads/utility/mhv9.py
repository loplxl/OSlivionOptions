from pathlib import Path
async def getURL(ssl_ctx,continuation,progressbar,completeDownload):
    await continuation("https://absolllute.com/store/download?file=v9",(Path.home() / "Downloads" / "Mega_Hack_Installer_Installer.exe"))