import os
import time
from playwright.sync_api import sync_playwright


def test_nav_2(page):
    page.goto("http://playwright.dev")
    print(page.title())
    time.sleep(3)
    page.close()


def test_nav_mysite_2(page):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    print(page.title())
    page.locator("text=Home").click()
    # Click text=Shop Women
    page.locator("text=Shop >> nth=1").click()
    time.sleep(3)
    page.close()
