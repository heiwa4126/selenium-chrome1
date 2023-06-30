#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chromeでselemiumのテスト。
大本: https://qiita.com/sszzszsz/items/4182c2b4aa4bf8f5037b
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

ChromeDriver = "../chromedriver.exe"

# オプションを準備
options = Options()
options.add_argument("--headless")
# headありだと "Every renderer should have at least one task provided by a primary task provider." という警告が出る。
# headありだとデバッグに便利
options.add_argument("--disable-extensions")  # すべての拡張機能を無効にする。ユーザースクリプトも無効にする
options.add_argument("--incognito")  # シークレットモードで起動する

# ドライバー指定でChromeブラウザを開く
service = Service(verbose=True, executable_path=ChromeDriver)
driver = webdriver.Edge(service=service, options=options)

# URLを開きスクショとる
driver.get("https://www.google.com/chrome/browser/welcomeback.html")
driver.save_screenshot("tmp/chrome.png")

driver.quit()
