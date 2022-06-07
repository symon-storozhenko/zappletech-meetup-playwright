import os
import time
from playwright.sync_api import sync_playwright, expect


PASSWORD = os.environ['METAMASK_PASSWORD']
KEY = os.environ['METAMASK_KEY']

# Inside .env file the above passwords should look like the lines below:
# NOTE: Make sure .env file is part of your .gitignore!
# METAMASK_PASSWORD=your_password
# METAMASK_KEY=your metamask key here (no quotes)

path_to_extension = "./metamask-chrome-10.14.0"
user_data_dir = "/tmp/test-user-data-dir"


def test_run_first_time(playwright):
    context = playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        args=[
            f"--disable-extensions-except={path_to_extension}",
            f"--load-extension={path_to_extension}",
        ],
    )
    context.set_default_timeout(5000)
    page = context.wait_for_event("page")
    print(page.title())
    key = KEY.split()
    if not page.locator('button:has-text("Unlock")').is_visible():
        page.locator('.MuiInputBase-input >> nth=0').fill(PASSWORD)
        page.locator('button:has-text("Unlock")').click()
    else:
        page.locator('button:has-text("Get Started")').click()
        page.locator('button:has-text("Import Wallet")').click()
        page.locator('button:has-text("I Agree")').click()
        page.locator(f'input >> nth=0').click()
        for enum in range(12):
            page.locator(f'.MuiInputBase-root >> input >> nth={enum}').fill(key[enum])

        page.locator('id=password').click()
        page.locator('id=password').fill(PASSWORD)
        page.locator('id=confirm-password').fill(PASSWORD)
        page.locator('.check-box').click()
        page.locator('button:has-text("Import")').click()
        time.sleep(10000)
        page.locator('button:has-text("All Done")').click()
        page.locator('data-testid="popover-close"').click()

    page2 = context.new_page()
    page2.set_default_timeout(7000)
    page2.goto("https://opensea.io/assets/matic/0xb50a99d16539018d9950365b85403f9e3d959ce2/1778")
    # NOTE! When running for the first time after successful login, use time.sleep(60) to pause, connect the wallet
    # manually from OpenSea and sign the transaction
    # time.sleep(60)
    # time.sleep(43)
    expect(page2.locator("button:has-text('Buy now')")).to_be_disabled()
    page2.reload()
    time.sleep(3)
    page2.locator("button:has-text('Cancel listing')").click()
    # Return to metamask page and sign the transaction
    # page.locator("text=Signature Request").click()
    # page.locator("data-testid=request-signature__sign").click()
    time.sleep(1200000)
