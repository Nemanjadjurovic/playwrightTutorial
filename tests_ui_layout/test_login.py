import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.mark.smoke
def test_login(set_up) -> None:
    page = set_up
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_visible()
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("test123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    # page.wait_for_load_state("networkidle")
    # expect(page.get_by_role("button", name="Log In")).to_be_hidden()

    all_links = page.get_by_role("link").all()
    for link in all_links:
        if '$85' in link.text_content():
            print("all good")
            assert 'Socks' not in link.text_content()

    print("Wohooo!")

    # ---------------------
    # context.close()
    # browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
