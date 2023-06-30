# selenium-chrome1

Selenium4 を Windows上のChrome とPython(v3.11)で試す。

## 準備

ドライバは親ディレクトリに置く。
[ChromeDriver - WebDriver for Chrome - Downloads](https://chromedriver.chromium.org/downloads)

venvも親ディレクトリに置く。

```powershell
python -m venv ../.venv
../.venv/Scripts/Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
```

## 実行1

```powershell
python ./test1.py
```

`tmp/chrome.png` に [chrome](https://www.google.com/chrome/browser/welcomeback.html)のスクリーンショットが取られる。

## 参考

- [The Selenium Browser Automation Project | Selenium](https://www.selenium.dev/documentation/)
- [ChromeDriver - WebDriver for Chrome - Downloads](https://chromedriver.chromium.org/downloads)
- [Chrome specific functionality | Selenium](https://www.selenium.dev/documentation/webdriver/browsers/chrome/)
