from modules.news import get_news
from modules.database import connect

RSS_URL = "https://feeds.bbci.co.uk/news/world/rss.xml"

connection = connect()
cursor = connection.cursor()

articles = get_news(RSS_URL)

saved = 0

for article in articles:

    try:

        cursor.execute("""
        INSERT INTO news(title,link,published)
        VALUES(?,?,?)
        """,(
            article["title"],
            article["link"],
            ""
        ))

        saved += 1

    except:
        pass

connection.commit()
connection.close()

print(f"Downloaded : {len(articles)}")

print(f"Saved      : {saved}")
