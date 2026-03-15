from collectors.github_repos import get_repositories
from storage.repos import save_repositories


def ingest():

    repos = get_repositories()

    save_repositories(repos)

    print(f"Stored {len(repos)} repositories")


if __name__ == "__main__":
    ingest()
