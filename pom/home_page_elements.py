import pytest
from pytest_playwright.pytest_playwright import page


class HomePage:
    celebrating_beauty_header = "text=Celebrating Beauty and Style"

    def __init__(self, page):
        self.celebrating_beauty_hdr = page.locator("text=Celebrating Beauty and Style")
        self.page = page
        self.profile_arrow = page.locator('._1hHt1')
        self.profile_icon = page.locator('#defaultAvatar-comp-kqx7o7qv')
        self.cart_icon = page.locator('.bQgup')
        self.my_orders = page.locator('text=My Orders')
        self.my_orders_profile_box = page.locator('#SOSP_CONTAINER_CUSTOM_ID >> :nth-match(div, 4)')
        self.shop_women = page.locator('text=Shop Women')
