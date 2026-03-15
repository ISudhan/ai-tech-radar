from storage.db import get_connection


def init_db():

    conn = get_connection()
    cur = conn.cursor()

    with open("storage/schema.sql") as f:
        cur.execute(f.read())

    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    init_db()
