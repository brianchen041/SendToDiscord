# SendToDiscord


#### Run

```cmd
py main.py DISCORD_BOT_TOKEN CHANNEL_ID "Hi Test"
```

#### Run with .exe

```cmd
SendToDiscord.exe DISCORD_BOT_TOKEN CHANNEL_ID "Hi Test"
```

#### Build with venv (Windows, CMD)

```cmd
py -m venv venvName
```

```cmd
.\venvName\Scripts\activate.bat
```

```cmd
pip3 install -r requirements.txt
```

```cmd
pyinstaller --paths venvName\Lib\site-packages main.py --onefile
```

#### Build with venv (Ubuntu)

```bash
python3 -m venv venvName
```

```bash
source venvName/bin/activate
```

```bash
pip3 install -r requirements.txt
```

```bash
pyinstaller --paths venvName/lib/python3.x/site-packages main.py --onefile
```
