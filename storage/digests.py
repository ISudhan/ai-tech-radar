from storage.db import get_connection
from datetime import date


def save_digest(summary):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO digests (digest_date, summary)
        VALUES (%s, %s)
        ON CONFLICT (digest_date) DO NOTHING
        """,
        (date.today(), summary)
    )

    conn.commit()

    cur.close()
    conn.close()
