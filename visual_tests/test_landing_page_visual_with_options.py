from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


def test_visual_landing_with_masks(page, assert_snapshot) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    homepage = HomePage(page)
    # expect(homepage.celebrating_beauty_hdr).to_be_visible()
    assert_snapshot(page.screenshot(mask=[homepage.cart_icon, homepage.shop_women]), )
