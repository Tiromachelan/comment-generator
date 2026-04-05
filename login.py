# Use this script to log into kononews.com if it's your first time
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://komonews.com/")
    page.pause() # Keeps the page open until you log in and continue 

    context.storage_state(path="auth.json") # Save auth state to file for later use in mcp_server.py
    browser.close()
