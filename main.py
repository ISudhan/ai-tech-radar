from ai.digest import build_digest
from delivery.telegram import send_message

from storage.ingest_arxiv import ingest as ingest_arxiv
from storage.ingest_news import ingest as ingest_news
from storage.ingest_repos import ingest as ingest_repos


def run():

    # collect data
    ingest_arxiv()
    ingest_news()
    ingest_repos()

    # generate intelligence digest
    digest = build_digest()

    # send message
    send_message(digest)


if __name__ == "__main__":
    run()