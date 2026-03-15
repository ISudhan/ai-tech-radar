import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px


def get_connection():
    return psycopg2.connect("dbname=ai_radar user=sudhan")

def load_news():

    conn = get_connection()

    query = """
    SELECT DATE(published_date) as day, COUNT(*) as articles
    FROM news
    GROUP BY day
    ORDER BY day
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df


st.header("AI News Activity")

news = load_news()

fig3 = px.line(news, x="day", y="articles")

st.plotly_chart(fig3)

def load_repo_growth():

    conn = get_connection()

    query = """
    SELECT r.name,
           s.stars,
           s.recorded_at
    FROM repo_stats s
    JOIN repositories r ON r.id = s.repo_id
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df


def load_paper_trends():

    conn = get_connection()

    query = """
    SELECT category, COUNT(*) as papers
    FROM papers
    GROUP BY category
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df


st.title("AI Tech Radar Dashboard")

st.header("Repository Growth")

repos = load_repo_growth()

fig = px.line(
    repos,
    x="recorded_at",
    y="stars",
    color="name"
)

st.plotly_chart(fig)


st.header("Research Activity")

papers = load_paper_trends()

fig2 = px.bar(
    papers,
    x="category",
    y="papers"
)

st.plotly_chart(fig2)
