from storage.db import get_connection


def save_news(news_items):

    conn = get_connection()
    cur = conn.cursor()

    for item in news_items:

        cur.execute(
            """
            INSERT INTO news (title, url, source, published_date)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (url) DO NOTHING
            """,
            (
                item["title"],
                item["url"],
                item["source"],
                item["published"]
            )
        )

    conn.commit()

    cur.close()
    conn.close()