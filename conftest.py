import os
import time
from playwright.sync_api import Playwright
import pytest

# PASSWORD = os.environ['PASSWORD']
# EMAIL = os.environ['EMAIL']


@pytest.fixture()
def set_up(page): #playwright: Playwright  --- po potrebi koristi
    # browser = playwright.chromium.launch(headless=False)  #slow_mo=500
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page


@pytest.fixture(scope='session') #This is not working
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    page.get_by_role("button", name="Log In").click()
    # page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill(EMAIL)
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    time.sleep(2)
    context.storage_state(path='state.json')

    yield context
    time.sleep(5)


@pytest.fixture() #This is not working
def login_set_up(context_creation, browser):
    context = browser.new_context(storage_state='state.json')
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.set_default_timeout(3000)

    yield page
    time.sleep(5)
    context.close()


@pytest.fixture()
def got_to_new_collection_page(page):  # playwright: Playwright  --- po potrebi koristi
    # browser = playwright.chromium.launch(headless=False)  #slow_mo=500
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("/new-collection")
    page.set_default_timeout(3000)

    yield page
