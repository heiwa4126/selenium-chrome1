# selenium-edge1

Selenium4 を Windows上のEdge とPython(v3.11)で試す。

## 準備

ドライバは親ディレクトリに置く。
[Microsoft Edge WebDriver - Microsoft Edge Developer](https://developer.microsoft.com/ja-jp/microsoft-edge/tools/webdriver/)

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

`tmp/google.png` に googleのスクリーンショットが取られる。

## 参考

- [The Selenium Browser Automation Project | Selenium](https://www.selenium.dev/documentation/)
- [Microsoft Edge WebDriver - Microsoft Edge Developer](https://developer.microsoft.com/ja-jp/microsoft-edge/tools/webdriver/)
