import os
import time

import pytest
from playwright.sync_api import sync_playwright


def test_nav(page):
    page.goto("http://playwright.dev")
    print(page.title())
    time.sleep(3)
    page.close()


def test_nav_mysite(page):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    print(page.title())
    time.sleep(3)
    page.close()


