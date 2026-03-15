from ai.digest import build_digest
from storage.digests import save_digest


def run():

    digest = build_digest()

    print(digest)

    save_digest(digest)


if __name__ == "__main__":
    run()
