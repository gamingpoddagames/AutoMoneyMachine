import json
import os

from modules.news import get_news

RSS_URL = "https://feeds.bbci.co.uk/news/world/rss.xml"

JSON_FILE = "data/articles.json"


def load_articles():
    if not os.path.exists(JSON_FILE):
        return []

    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def save_articles(data):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


print("=" * 40)
print("AutoMoneyMachine")
print("=" * 40)

existing_articles = load_articles()

existing_links = {article["link"] for article in existing_articles}

rss_articles = get_news(RSS_URL)

new_articles = 0

for article in rss_articles:

    if article["link"] not in existing_links:

        existing_articles.append(article)

        existing_links.add(article["link"])

        new_articles += 1

save_articles(existing_articles)

print(f"Downloaded : {len(rss_articles)}")

print(f"New Articles : {new_articles}")

print(f"Total Saved : {len(existing_articles)}")
