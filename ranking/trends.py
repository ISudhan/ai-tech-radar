from ranking.repos import get_trending_repos
from ranking.papers import get_trending_topics
from ranking.tools import get_popular_tools


def generate_trends():

    return {
        "repos": get_trending_repos(),
        "topics": get_trending_topics(),
        "tools": get_popular_tools()
    }
