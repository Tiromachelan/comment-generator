import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


# Post the comment to the site using Playwright
def upload_comment(comment):
    with sync_playwright() as p:
        links = get_article_links()
        if not links:
            return "Error: No article links found"
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()
        page.goto("https://komonews.com/news/nation-world")
        input("Press enter to continue...") # Keep the page open until user input
        # page.fill("#comment-input", comment)
        # page.click("#submit-button")
        # browser.close()

# Get article links from the site
def get_article_links():
    url = "https://komonews.com/news/nation-world"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article_links = []
    for a in soup.select('a[href*="/news/nation-world/"]'):
        href = a['href']
        if href.startswith("/news/nation-world/"):
            article_links.append("https://komonews.com" + href)
    return article_links

if __name__ == "__main__":
    upload_comment("This is a test comment.")
    #get_article_links()

# #section-main-page > div.PageColumn_pageColumn__21k88 > div > div.StickyTwoColumn_leftColumn__EmK0K > div > div.SectionHeroTeasers_panel__MBG0R.Panel_panel__wT2cw > div > div.SectionHeroTeasers_heroTeaser__R9w3d > div > a > div.TeaserLink_teaserText__g1DQc > div:nth-child(2)
# all-hell-will-reign-down-trump-gives-iran-48-hour-ultimatum-over-strait-of-hormuz-oil-gas-gasoline-military-escalation-war-conflict-operation-epic-fury-attacks-strikes-united-states-israel-president-donald-trump-peace-talks
