import feedparser


def get_news(feed_url):

    feed = feedparser.parse(feed_url)

    news = []

    for article in feed.entries:

        news.append({

            "title": article.title,

            "link": article.link,

            "published": getattr(article, "published", "")

        })

    return news
