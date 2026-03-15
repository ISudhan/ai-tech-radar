from collectors.arxiv import get_papers
from storage.papers import save_papers


def ingest():

    papers = get_papers()

    save_papers(papers)

    print(f"Stored {len(papers)} papers")


if __name__ == "__main__":
    ingest()