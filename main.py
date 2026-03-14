import os
from datetime import datetime

from collectors.github_trending import get_repos
from collectors.arxiv import get_papers
from collectors.ai_news import get_news

from ai.summarizer import summarize
from delivery.telegram import send_message


def save_digest(text):
    today = datetime.utcnow().strftime("%Y-%m-%d")

    os.makedirs("data/digests", exist_ok=True)

    file_path = f"data/digests/{today}.md"

    with open(file_path, "w") as f:
        f.write(text)


def run():

    data = {
        "news": get_news(),
        "papers": get_papers(),
        "repos": get_repos()
    }

    try:
        summary = summarize(data)
    except Exception as e:
        print("Gemini failed, using fallback summary")

        summary = f"""
AI Tech Radar

News:
{data['news']}

Papers:
{data['papers']}

Repos:
{data['repos']}
"""

    save_digest(summary)

    try:
        send_message(summary)
    except Exception as e:
        print("Telegram send failed")


if __name__ == "__main__":
    run()