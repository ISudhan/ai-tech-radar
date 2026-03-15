from storage.db import get_connection


def get_popular_tools(limit=10):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT name, MAX(stars) as stars
    FROM repo_stats s
    JOIN repositories r ON r.id = s.repo_id
    GROUP BY name
    ORDER BY stars DESC
    LIMIT %s
    """, (limit,))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows
