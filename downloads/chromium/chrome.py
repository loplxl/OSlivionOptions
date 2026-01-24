from pathlib import Path
async def getURL(ssl_ctx):
    return "https://dl.google.com/chrome/install/ChromeStandaloneSetup64.exe",(Path.home() / "Downloads" / "ChromeStandaloneSetup64.exe")