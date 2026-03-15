# AI Tech Radar

**AI Tech Radar** is an automated intelligence pipeline that monitors the global AI ecosystem by collecting data from research papers, technology news, and GitHub repositories.

The system analyzes this data to detect emerging trends and automatically generates daily AI intelligence briefings.

The goal of this project is to demonstrate how a modern **data pipeline + analytics + AI summarization system** can be built using Python.

---

# Overview

AI Tech Radar continuously tracks:

* Latest AI research papers
* Important AI news articles
* Trending AI GitHub repositories
* Repository growth and popularity

The system processes these signals to produce a **daily intelligence report** that highlights the most important developments in AI.

---

# System Architecture

```
Data Sources
│
├── arXiv API (AI research papers)
├── AI News RSS feeds
└── GitHub API (AI repositories)
        │
        ▼
Collectors Layer
│
├── collectors/arxiv.py
├── collectors/news.py
└── collectors/github_repos.py
        │
        ▼
Storage Layer
(PostgreSQL database)
│
├── papers
├── news
├── repositories
├── repo_stats
└── digests
        │
        ▼
Trend Analysis Engine
│
├── ranking/repos.py
├── ranking/papers.py
├── ranking/tools.py
└── ranking/trends.py
        │
        ▼
Digest Generator
│
└── ai/digest.py
        │
        ▼
Delivery System
│
└── Telegram Bot
```

The entire system runs automatically using **GitHub Actions**.

---

# Features

### Automated Data Collection

The system collects AI ecosystem signals from multiple sources:

* **arXiv API** – Latest AI and machine learning papers
* **AI News RSS** – Technology news related to AI
* **GitHub API** – Trending AI repositories

---

### Historical Data Tracking

All collected data is stored in PostgreSQL.

This enables:

* Repository star growth tracking
* Research activity monitoring
* Long-term trend analysis

---

### Trend Detection

The trend engine analyzes stored data to detect:

* Fastest growing AI repositories
* Most active research fields
* Popular AI tools

---

### Daily Intelligence Briefing

The system generates a structured intelligence report containing:

* Fastest growing AI repositories
* Top research topics
* Most popular AI tools
* Important AI news

Example output:

```
AI Tech Radar — Daily Intelligence Brief

Fastest Growing AI Repositories
• huggingface/transformers (+520 stars)
• microsoft/DeepSpeed (+410)

Top Research Topics
• cs.LG (machine learning)
• cs.CL (natural language processing)

Popular AI Tools
• transformers
• langchain

Important AI News
• OpenAI releases new multimodal model
• Google announces Gemini update
```

---

# Project Structure

```
ai-tech-radar

collectors/
    arxiv.py
    news.py
    github_repos.py

ranking/
    repos.py
    papers.py
    tools.py
    trends.py

ai/
    digest.py

storage/
    db.py
    ingest_arxiv.py
    ingest_news.py
    ingest_repos.py
    generate_digest.py

delivery/
    telegram.py

data/
    digests/

main.py
README.md
```

---

# Tech Stack

* **Python**
* **PostgreSQL**
* **GitHub Actions**
* **Telegram Bot API**
* **arXiv API**
* **GitHub API**

Libraries used:

* requests
* feedparser
* psycopg2
* python-telegram-bot

---

# Setup

### Clone Repository

```
git clone https://github.com/yourusername/ai-tech-radar.git
cd ai-tech-radar
```

---

### Create Environment

Using **uv**:

```
uv venv
source .venv/bin/activate
uv sync
```

---

### Configure Environment Variables

Create a `.env` file:

```
GEMINI_API_KEY=your_key
TELEGRAM_TOKEN=your_token
CHAT_ID=your_chat_id
DATABASE_URL=postgresql://localhost/ai_radar
```

---

### Initialize Database

```
uv run python -m storage.init_db
```

---

# Running the System

Run the full pipeline:

```
uv run python main.py
```

Pipeline steps:

1. Collect research papers
2. Collect AI news
3. Collect GitHub repositories
4. Store data in PostgreSQL
5. Analyze trends
6. Generate intelligence digest
7. Send Telegram notification

---

# Automation

The system runs automatically using **GitHub Actions**.

Scheduled runs:

* **8:00 AM IST**
* **6:00 PM IST**

This ensures the AI intelligence report stays up to date.

---

# Future Improvements

Planned enhancements:

* AI-powered summarization
* Trend scoring algorithms
* Visualization dashboard
* Weekly AI trend reports
* Startup and funding tracking

---

# Why This Project Matters

AI Tech Radar demonstrates how to build a **modern data intelligence pipeline** combining:

* data engineering
* analytics
* automation
* AI summarization

It showcases practical skills used in:

* data platforms
* AI infrastructure
* research monitoring systems
* technology intelligence tools

---

# License

MIT License
