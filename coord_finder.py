from playwright.sync_api import sync_playwright
import time

def finder():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # Match your final script's viewport exactly
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()
        
        # Simple print function
        page.on("mousemove", lambda pos: print(f"COORD -> X: {int(pos['x'])} | Y: {int(pos['y'])}"))

        page.goto("https://komonews.com/news/nation-world/all-hell-will-reign-down-trump-gives-iran-48-hour-ultimatum-over-strait-of-hormuz-oil-gas-gasoline-military-escalation-war-conflict-operation-epic-fury-attacks-strikes-united-states-israel-president-donald-trump-peace-talks")
        
        print("--- SCRIPT ACTIVE ---")
        print("Move mouse over the page to see coordinates in terminal.")
        
        # Keep it alive
        while True:
            page.wait_for_timeout(100)

finder()