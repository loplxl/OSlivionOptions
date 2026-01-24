pyinstaller --noconfirm --onedir --windowed --icon=icon.ico --add-data "about.png;." --add-data "options.png;." --add-data "icon.png;." --add-data "TimerResolution;TimerResolution" --add-data "downloads;downloads" --add-data "tools;tools" --add-data "dependencies;dependencies" --hidden-import bs4 --hidden-import win32com main.py --name OSO --noconfirm
timeout /t 1 /nobreak >nul
powershell -Command Compress-Archive -Path .\dist\OSO -DestinationPath .\dist\OSO.zip -Update

pause