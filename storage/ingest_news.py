from collectors.news import get_news
from storage.news import save_news


def ingest():

    news_items = get_news()

    save_news(news_items)

    print(f"Stored {len(news_items)} news articles")


if __name__ == "__main__":
    ingest()