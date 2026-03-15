import pandas as pd
from sklearn.linear_model import LinearRegression
from sqlalchemy import create_engine


# database engine
engine = create_engine("postgresql://sudhan@localhost/ai_radar")


def load_repo_history(repo_name):
    """
    Load star history for a single repository.
    """

    query = """
    SELECT s.stars, s.recorded_at
    FROM repo_stats s
    JOIN repositories r ON r.id = s.repo_id
    WHERE r.name = %(repo)s
    ORDER BY s.recorded_at
    """

    df = pd.read_sql(query, engine, params={"repo": repo_name})

    return df


def predict_growth(repo_name):
    """
    Predict next-day star growth for a repository.
    Returns predicted star increase.
    """

    df = load_repo_history(repo_name)

    # need at least two points to fit regression
    if len(df) < 2:
        return None

    df["recorded_at"] = pd.to_datetime(df["recorded_at"])

    # convert timestamps → days since first observation
    df["days"] = (
        df["recorded_at"] - df["recorded_at"].min()
    ).dt.days

    X = df[["days"]]
    y = df["stars"]

    model = LinearRegression()
    model.fit(X, y)

    # predict stars for next day
    next_day = pd.DataFrame({
        "days": [df["days"].max() + 1]
    })

    predicted_total = model.predict(next_day)[0]

    current_stars = df["stars"].iloc[-1]

    predicted_growth = predicted_total - current_stars

    return int(predicted_growth)