from modules.news import get_news

RSS_URL = "https://feeds.bbci.co.uk/news/world/rss.xml"

print("=" * 40)
print("AutoMoneyMachine")
print("=" * 40)

articles = get_news(RSS_URL)

print(f"Found {len(articles)} articles")

for article in articles[:10]:
    print("-" * 40)
    print("Title:", article["title"])
    print("Link :", article["link"])
