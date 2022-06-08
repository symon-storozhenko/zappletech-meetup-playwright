from pom.home_page_elements import HomePage
from playwright.sync_api import Page, Playwright, sync_playwright, expect
import pytest


def test_about_us_section_verbiage_user2(login_set_up_user2) -> None:
    page = login_set_up_user2
    expect(page.locator("text=Celebrating Beauty and Style")).to_be_visible()
    # home_page = HomePage(page)
    # expect(home_page.celebrating_beauty_hdr).to_be_visible()


def test_about_us_section_verbiage_user2_2_not_visible(login_set_up_user2) -> None:
    page = login_set_up_user2
    page.locator('text=Shop Women').click()
    expect(page.locator("text=Celebrating Beauty and Style")).to_be_hidden()
