## Features

Download your songs and playlist from Spotify using [yt-dlp](https://github.com/yt-dlp/yt-dlp "yt-dlp")

### How to use

You can download the latest executable version [here](https://github.com/CoffeSiberian/Download-Spotify-Music-with-YouTubeDL/releases "here") to use but just remember to **set your Spotify API KEY and set your PlayList to public**

---

Install the following dependencies if you want to run from source code

```bash
pip install -r requirements.txt
```

You can also use

```bash
pip install PySide6 yt-dlp requests
```

To transform .ui files to python classes use

```bash
pyside6-uic window.ui > window.py
```

So you can compile your own executable with pyinstaller. More details at https://pyinstaller.org/en/stable/usage.html

-   Just remember to first install `pyinstaller` and `Pillow` (This is to be able to add the .ico).

```bash
pyinstaller --onefile --clean --windowed --name Download-Spotify-Music-with-YouTubeDL --icon assets/icons/img.ico --add-data "assets/icons:assets/icons" app.py
```

Remember to have the dependencies installed first. You can read more here: [https://doc.qt.io/qtforpython/tutorials/](https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html "https://doc.qt.io/qtforpython/tutorials/")

### Get your Spotify API KEY

**Go to https://developer.spotify.com/dashboard to get your _client_id_ and _client_secret_**

[Imgur step by step images](https://imgur.com/a/v8MLpWb "Imgur Step by Step")
