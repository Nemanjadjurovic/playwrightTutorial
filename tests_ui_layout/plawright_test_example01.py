import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)  #slow_mo=500
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000)
    time.sleep(2)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
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
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
