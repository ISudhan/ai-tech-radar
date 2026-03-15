import logging

from ai.digest import build_digest
from delivery.telegram import send_message

from storage.ingest_arxiv import ingest as ingest_arxiv
from storage.ingest_news import ingest as ingest_news
from storage.ingest_repos import ingest as ingest_repos


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def run():

    logging.info("AI Tech Radar pipeline started")

    try:

        logging.info("Collecting arXiv papers...")
        ingest_arxiv()

        logging.info("Collecting AI news...")
        ingest_news()

        logging.info("Collecting GitHub repositories...")
        ingest_repos()

        logging.info("Generating intelligence digest...")
        digest = build_digest()

        logging.info("Sending Telegram message...")
        send_message(digest)

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error("Pipeline failed")
        logging.exception(e)


if __name__ == "__main__":
    run()