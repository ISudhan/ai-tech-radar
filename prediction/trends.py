from prediction.repos import predict_growth
from storage.db import get_connection


def get_repos():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM repositories")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [r[0] for r in rows]


def predict_trending(limit=5):

    repos = get_repos()

    predictions = []

    for repo in repos:

        prediction = predict_growth(repo)

        if prediction:
            predictions.append((repo, prediction))

    predictions.sort(key=lambda x: x[1], reverse=True)

    return predictions[:limit]
