from os import getcwd,path,remove
import customtkinter as ctk
import aiohttp
import asyncio
import threading
import ssl
from utils import resource_path
import zipfile
ssl_ctx = ssl.create_default_context(cafile=resource_path("dependencies/cacert.pem"))
async def getURL(self,btn):
    appFrame = btn.master
    btn.destroy()
    progressbar = ctk.CTkProgressBar(appFrame,width=75)
    progressbar.set(0)
    progressbar.grid(row=0,column=1,padx=(0,5),sticky="e")
    async def uiUpdate(progressbar,frac):
        self.after(0,progressbar.set,frac)
    async def async_download(url,DLpath,progressbar):
        lastUpdateFrac = 0
        async with aiohttp.ClientSession() as session:
            async with session.get(url,ssl=ssl_ctx) as resp:
                resp.raise_for_status()
                total = resp.content_length or 0
                downloaded = 0
                with open(DLpath, "wb") as f:
                    async for chunk in resp.content.iter_chunked(8192):
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total:
                            frac = downloaded/total
                            if frac-lastUpdateFrac >= 0.01: #only update ui every 1% downloaded
                                threading.Thread(target=lambda: asyncio.run(uiUpdate(progressbar,frac)), daemon=True).start()
                                lastUpdateFrac = frac
        completeLabel = ctk.CTkLabel(appFrame, text="Complete", text_color="#00ff00", font=ctk.CTkFont(size=20))
        progressbar.destroy()
        completeLabel.grid(row=0,column=1,padx=(0,8))
        with zipfile.ZipFile(DLpath, 'r') as zip_ref:
            outputloc = path.dirname(DLpath)
            zip_ref.extractall(outputloc)
        remove(DLpath)
    threading.Thread(target=lambda: asyncio.run(async_download("https://github.com/valleyofdoom/AutoGpuAffinity/releases/latest/download/AutoGpuAffinity.zip",path.join(getcwd()[:2],"\\OSlivion","OSO","quickaccess","AutoGpuAffinity.zip"),progressbar)), daemon=True).start() #asynchronous download
