from playwright.sync_api import Playwright
import pytest


@pytest.fixture()
def set_up(page): #playwright: Playwright  --- po potrebi koristi
    # browser = playwright.chromium.launch(headless=False)  #slow_mo=500
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page


@pytest.fixture()
def got_to_new_collection_page(page): #playwright: Playwright  --- po potrebi koristi
    # browser = playwright.chromium.launch(headless=False)  #slow_mo=500
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("/new-collection")
    page.set_default_timeout(3000)

    yield page
