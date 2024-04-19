import time

from playwright.sync_api import sync_playwright, expect


def search_playwright_docs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to google.com
        page.goto("https://www.google.com")

        # Type "playwright docs" into the search bar
        page.get_by_label("Тражи", exact=True).fill("python playwright docs")
        page.get_by_label("Google претрага").first.click()

        # Wait for search results to load
        page.get_by_role("link", name="Playwright Python Playwright https://playwright.dev › api").click()

        # Wait for the documentation page to load
        expect(page.get_by_role("heading", name="Playwright")).to_be_visible()
        time.sleep(2)

        # Print success message
        print("Successfully opened Playwright Python documentation.")

        # Close the browser
        context.close()
        browser.close()


# Run the search function
search_playwright_docs()