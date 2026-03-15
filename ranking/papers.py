from storage.db import get_connection


def get_trending_topics(limit=10):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT category, COUNT(*) as paper_count
    FROM papers
    GROUP BY category
    ORDER BY paper_count DESC
    LIMIT %s
    """, (limit,))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows
