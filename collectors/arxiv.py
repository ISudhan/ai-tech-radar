import feedparser

FEEDS = [
    "https://export.arxiv.org/rss/cs.AI",
    "https://export.arxiv.org/rss/cs.LG",
    "https://export.arxiv.org/rss/cs.CL",
    "https://export.arxiv.org/rss/stat.ML",
]

def get_papers():

    papers = []

    for url in FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries[:3]:
            papers.append(entry.title)

    return papers[:5]