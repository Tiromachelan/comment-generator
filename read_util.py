from bs4 import BeautifulSoup
import requests


def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract text from all paragraphs in the article
    paragraphs = soup.find_all("p")
    article_text = "\n\n".join([p.get_text(strip=True) for p in paragraphs])
    return article_text

    # article_container = soup.find("div", class_="StoryText_storyText__mI_yD")
    # if article_container:
    #     paragraphs = article_container.find_all("p")
    #     article_text = "\n\n".join([p.get_text(strip=True) for p in paragraphs])
    #     return article_text
    # else:
    #     return "Error: Could not read article"
    
if __name__ == "__main__":
    url = "https://komonews.com/news/nation-world/all-hell-will-reign-down-trump-gives-iran-48-hour-ultimatum-over-strait-of-hormuz-oil-gas-gasoline-military-escalation-war-conflict-operation-epic-fury-attacks-strikes-united-states-israel-president-donald-trump-peace-talks"
    print(extract_text(url))