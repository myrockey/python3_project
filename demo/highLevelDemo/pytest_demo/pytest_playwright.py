#!/usr/bin/python3

# 自动化测试工具
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.baidu.com")
    print(page.title())          # 🎉 一行代码就能跑
    browser.close()