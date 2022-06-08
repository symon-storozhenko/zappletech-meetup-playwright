import os
import time
import pytest

PASSWORD = os.environ['PASSWORD']
PASSWORD2 = os.environ['PASSWORD2']


@pytest.fixture(scope='session')
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    page.wait_for_selector("button:has-text(\"Log In\")", timeout=1000)
    login_issue = True
    while login_issue:
        if not page.locator("[data-testid=\"signUp.switchToSignUp\"]").is_visible():
            page.locator("button:has-text(\"Log In\")").click()
        else:
            login_issue = False
        time.sleep(0.1)
    page.locator("[data-testid=\"signUp.switchToSignUp\"]").click(timeout=2000)
    page.locator("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']").click()
    page.locator('input:below(:text("Email"))').first.fill("symon.storozhenko@gmail.com")
    page.locator("[data-testid='siteMembers.container'] >> input[type='email']").press("Tab")
    page.locator("input[type='password']").fill(PASSWORD)
    page.locator("[data-testid='submit'] >> [data-testid='buttonElement']").click()
    page.wait_for_load_state(timeout=10000)
    # Below two lines is for use with storage state functionality
    # time.sleep(2) # Pause required to load the state first
    # context.storage_state(path='state.json')
    yield context
    time.sleep(3)


@pytest.fixture()
def login_set_up(context_creation, playwright):
    # Below three lines is for use with storage state functionality
    # browser = playwright.chromium.launch(headless=False, slow_mo=200)
    # context = browser.new_context(storage_state='state.json')
    # page = context.new_page()
    page = context_creation.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    assert not page.is_visible("text=Log In")
    yield page
    page.close()
    # browser.close()


@pytest.fixture(scope='session')
def context_creation_user2(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    page.wait_for_selector("button:has-text(\"Log In\")", timeout=1000)
    login_issue = True
    while login_issue:
        if not page.locator("[data-testid=\"signUp.switchToSignUp\"]").is_visible():
            page.locator("button:has-text(\"Log In\")").click()
        else:
            login_issue = False
        time.sleep(0.1)
    page.locator("[data-testid=\"signUp.switchToSignUp\"]").click(timeout=2000)
    page.locator("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']").click()
    page.locator('input:below(:text("Email"))').first.fill("stosimon@gmail.com")
    page.locator("[data-testid='siteMembers.container'] >> input[type='email']").press("Tab")
    page.locator("input[type='password']").fill(PASSWORD2)
    page.locator("[data-testid='submit'] >> [data-testid='buttonElement']").click()
    page.wait_for_load_state(timeout=10000)
    time.sleep(2)
    # context.storage_state(path='state.json')
    yield context
    time.sleep(3)


@pytest.fixture()
def login_set_up_user2(context_creation_user2, playwright):
    # browser = playwright.chromium.launch(headless=False, slow_mo=200)
    # context = browser.new_context(storage_state='state.json')
    # page = context.new_page()
    page = context_creation_user2.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    assert not page.is_visible("text=Log In")
    yield page
    page.close()
    # browser.close()
