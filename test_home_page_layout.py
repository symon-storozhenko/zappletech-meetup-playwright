from pom.home_page_elements import HomePage
from playwright.sync_api import Page, Playwright, sync_playwright, expect
import pytest


@pytest.mark.integration
def test_about_us_section_verbiage_user1(login_set_up) -> None:
    # Assess - Given
    page = login_set_up
    expect(page.locator("text=Celebrating Beauty and Style")).to_be_visible()
    # home_page = HomePage(page)
    # expect(home_page.celebrating_beauty_hdr).to_be_visible()


@pytest.mark.integration
def test_about_us_section_verbiage_users1_2(login_set_up) -> None:
    # Assess - Given
    page = login_set_up
    page.locator('text=Shop Women').click()
    expect(page.locator("text=Celebrating Beauty and Style")).to_be_visible()

