import feedparser

NEWS_FEEDS = [
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://venturebeat.com/category/ai/feed/",
]

def get_news():

    news = []

    for url in NEWS_FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:3]:
            news.append(entry.title)

    return news[:5]
