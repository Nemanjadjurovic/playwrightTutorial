from playwright.sync_api import Playwright, sync_playwright
import pytest
import time
from pom.contact_us_page import ContactUsPage


@pytest.mark.smoke
def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Nemanja", "ulica 123", "email@email.com", "123-321-333", "test subject", "poruka ide")


# with sync_playwright() as playwright:
#     test_submit_form(playwright)