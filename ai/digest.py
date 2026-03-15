from ranking.trends import generate_trends
from storage.db import get_connection


def get_latest_news(limit=5):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT title
        FROM news
        ORDER BY published_date DESC
        LIMIT %s
    """, (limit,))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [r[0] for r in rows]


def build_digest():

    trends = generate_trends()

    news = get_latest_news()

    message = "🚀 AI Tech Radar — Daily Intelligence Brief\n\n"

    message += "🔥 Fastest Growing AI Repositories\n"
    for repo, growth in trends["repos"]:
        message += f"• {repo} (+{growth} stars)\n"

    message += "\n📚 Top Research Topics\n"
    for topic, count in trends["topics"]:
        message += f"• {topic} ({count} papers)\n"

    message += "\n🧠 Popular AI Tools\n"
    for tool, stars in trends["tools"]:
        message += f"• {tool} ({stars} stars)\n"

    message += "\n📰 Important AI News\n"
    for article in news:
        message += f"• {article}\n"

    return message
