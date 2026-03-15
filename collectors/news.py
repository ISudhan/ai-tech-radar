import feedparser

FEEDS = [
    "https://techcrunch.com/tag/artificial-intelligence/feed/",
    "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
]


def get_news():

    articles = []

    for url in FEEDS:

        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:

            articles.append({
                "title": entry.title,
                "url": entry.link,
                "source": url,
                "published": entry.get("published", None)
            })

    # remove duplicates
    unique = {a["url"]: a for a in articles}

    return list(unique.values())