from storage.db import get_connection


def get_trending_repos(limit=10):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT r.name,
           MAX(s.stars) - MIN(s.stars) AS star_growth
    FROM repo_stats s
    JOIN repositories r ON r.id = s.repo_id
    GROUP BY r.name
    ORDER BY star_growth DESC
    LIMIT %s
    """, (limit,))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows
