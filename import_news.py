import sqlite3
from modules.news import get_news

connection = sqlite3.connect("data/database.db")
cursor = connection.cursor()

feed = "https://feeds.bbci.co.uk/news/world/rss.xml"

articles = get_news(feed)

for article in articles:

    cursor.execute("""

    INSERT INTO news(title,link,published)

    VALUES(?,?,?)

    """,(

        article["title"],

        article["link"],

        article["published"]

    ))

connection.commit()

connection.close()

print("News Imported Successfully")
