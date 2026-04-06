# For manually changing settings on the website or whatever.
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
            storage_state="auth.json", # Load saved login state
            viewport={'width': 1280, 'height': 800}
        )
    page = context.new_page()

    page.goto("https://komonews.com/")
    page.pause()
    
    context.storage_state(path="auth.json")
    browser.close()
