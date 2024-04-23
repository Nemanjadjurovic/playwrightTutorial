from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
import pytest


@pytest.mark.integration
@pytest.mark.regression
def test_about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    home_page = HomePage(page)
    page.goto('https://symonstorozhenko.wixsite.com/website-1')
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()


@pytest.mark.skip(reason="not ready for testing yet")
def test_about_us_section_verbiage_2(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    home_page = HomePage(page)
    page.goto('https://symonstorozhenko.wixsite.com/website-1')
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()


# with sync_playwright() as playwright:
#     test_about_us_section_verbiage(playwright)