from storage.db import get_connection


def save_repositories(repos):

    conn = get_connection()
    cur = conn.cursor()

    for repo in repos:

        cur.execute(
            """
            INSERT INTO repositories (name, url, description, language)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (name) DO NOTHING
            RETURNING id
            """,
            (
                repo["name"],
                repo["url"],
                repo["description"],
                repo["language"]
            )
        )

        result = cur.fetchone()

        if result:
            repo_id = result[0]
        else:
            cur.execute(
                "SELECT id FROM repositories WHERE name=%s",
                (repo["name"],)
            )
            repo_id = cur.fetchone()[0]

        cur.execute(
            """
            INSERT INTO repo_stats (repo_id, stars, forks)
            VALUES (%s, %s, %s)
            """,
            (
                repo_id,
                repo["stars"],
                repo["forks"]
            )
        )

    conn.commit()

    cur.close()
    conn.close()
