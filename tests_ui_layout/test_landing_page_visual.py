from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


def test_visual_landing(page, assert_snapshot):
    url = "https://symonstorozhenko.wixsite.com/website-1/shop"
    page.goto(url)
    homepage = HomePage(page)
    expect(homepage.celebrating_beauty_hdr).to_be_visible()
    assert_snapshot(page.screenshot())
    expect(page).to_have_url(url)
    url_name = expect(page).to_have_url(f"{url}")
    print(url_name)
    print(url)
