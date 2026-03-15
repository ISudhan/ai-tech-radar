from storage.db import get_connection


def save_papers(papers):

    conn = get_connection()
    cur = conn.cursor()

    for paper in papers:

        cur.execute(
            """
            INSERT INTO papers (title, url, published_date, category)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (url) DO NOTHING
            """,
            (
                paper["title"],
                paper["url"],
                paper["published"],
                paper["category"]
            )
        )

    conn.commit()

    cur.close()
    conn.close()
