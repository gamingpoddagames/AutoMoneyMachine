import feedparser


def get_news(url):

    feed = feedparser.parse(url)

    news = []

    for item in feed.entries:

        news.append({

            "title": item.title,

            "link": item.link,

            "published": getattr(item, "published", "")

        })

    return news
