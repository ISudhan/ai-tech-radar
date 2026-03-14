# 🤖 AI Tech Radar

> **Your automated AI intelligence briefing — delivered twice daily, straight to Telegram.**

AI Tech Radar is a fully automated intelligence pipeline that monitors the AI/ML landscape in real time. It collects the latest research papers from ArXiv, trending AI news from RSS feeds, and hot GitHub repositories — then uses **Gemini AI** to synthesize everything into a clean, structured daily digest delivered via **Telegram Bot**, orchestrated entirely by **GitHub Actions**.

---

## 📸 Example Telegram Output
```
📡 AI Tech Radar — Daily Brief
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📰 Top AI News
- OpenAI announces GPT-5 with enhanced reasoning capabilities
- Google DeepMind releases new reinforcement learning benchmark
- Meta open-sources next-gen image generation model

📄 Important ML Papers (ArXiv)
- "Scaling Laws for Reward Model Overoptimization" — Gao et al.
- "Efficient Long-Context Transformers via Sparse Attention" — MIT CSAIL
- "LLM-as-Judge: Aligning AI Evaluation with Human Preferences"

🔥 Trending GitHub Repositories
- huggingface/transformers ⭐ 128k
- facebookresearch/llama ⭐ 54k
- run-llama/llama_index ⭐ 33k

🕐 Generated: 2025-01-15 08:00 UTC
```

---

## 🏗️ Architecture
```
┌─────────────────────────────────────────┐
│           Data Sources                  │
│  📰 RSS Feeds   📄 ArXiv   🐙 GitHub API │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│             Collectors                  │
│  ai_news.py │ arxiv.py │ github_trending│
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│         Gemini AI Summarizer            │
│         summarizer.py                   │
│  • Filters noise                        │
│  • Ranks by relevance                   │
│  • Generates structured digest          │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│           Delivery Layer                │
│           telegram.py                   │
│  → Sends formatted brief to channel    │
│  → Saves digest to data/digests/        │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│         GitHub Actions (CRON)           │
│         radar.yml                       │
│  ⏰ Runs automatically — twice daily    │
└─────────────────────────────────────────┘
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔄 **Fully Automated** | Runs on a CRON schedule via GitHub Actions — zero manual effort |
| 🧠 **AI-Powered Summaries** | Gemini AI distills raw data into concise, human-readable briefings |
| 📄 **ArXiv Research Monitoring** | Tracks the latest ML/AI research papers as they drop |
| 📰 **AI News Aggregation** | Pulls from curated RSS feeds covering the AI industry |
| 🔥 **GitHub Trending Tracker** | Surfaces the hottest AI/ML repositories in real time |
| 📬 **Telegram Delivery** | Pushes formatted digests directly to your Telegram channel or group |
| 🗂️ **Historical Digest Archive** | Every briefing is saved as a dated Markdown file in the repo |
| 🔒 **Secrets-Safe CI/CD** | All credentials managed via GitHub Secrets — never hardcoded |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.11+ |
| **AI Summarization** | Google Gemini API |
| **Messaging** | Telegram Bot API |
| **Automation** | GitHub Actions |
| **Data Collection** | RSS Feeds, GitHub REST API |
| **Package Manager** | `uv` (ultra-fast Python package manager) |

---

## ⚙️ How It Works

1. **Collect** — Three independent collectors run in parallel:
   - `collectors/ai_news.py` fetches AI headlines from RSS feeds
   - `collectors/arxiv.py` pulls the latest ML papers from ArXiv
   - `collectors/github_trending.py` queries GitHub for trending AI repositories

2. **Summarize** — Raw collected data is passed to `ai/summarizer.py`, which calls the Gemini API to rank, filter, and synthesize content into a structured briefing

3. **Deliver** — `delivery/telegram.py` formats the digest and pushes it to your configured Telegram channel

4. **Archive** — The digest is saved to `data/digests/YYYY-MM-DD.md` and committed to the repository

5. **Automate** — `.github/workflows/radar.yml` triggers the entire pipeline twice daily via CRON

---

## 🚀 Installation

### Prerequisites

- Python 3.11+
- [`uv`](https://github.com/astral-sh/uv) package manager
- A [Gemini API key](https://aistudio.google.com/)
- A [Telegram Bot token](https://core.telegram.org/bots/tutorial) + channel/chat ID

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-tech-radar.git
cd ai-tech-radar
```

### 2. Install Dependencies
```bash
uv sync
```

### 3. Configure Environment Variables
```bash
cp .env.example .env
# Fill in your credentials (see section below)
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:
```env
# .env.example

# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# Telegram Bot
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_or_channel_id_here

# GitHub API (optional — increases rate limits)
GITHUB_TOKEN=your_github_personal_access_token_here
```

For GitHub Actions, add these as **Repository Secrets** under `Settings → Secrets and variables → Actions`.

---

## 🖥️ Running Locally
```bash
# Activate the virtual environment
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows

# Run the full pipeline
python main.py
```

The pipeline will collect data, generate a summary, send it to Telegram, and save the digest to `data/digests/`.

---

## ⏱️ Automation with GitHub Actions

The pipeline is defined in `.github/workflows/radar.yml` and runs automatically on a CRON schedule:
```yaml
on:
  schedule:
    - cron: '0 8 * * *'   # 08:00 UTC daily
    - cron: '0 20 * * *'  # 20:00 UTC daily
  workflow_dispatch:        # Manual trigger via GitHub UI
```

Each run:
1. Checks out the repository
2. Sets up Python with `uv`
3. Installs dependencies
4. Executes `main.py`
5. Commits and pushes the generated digest back to the repository

> You can also trigger a manual run anytime from the **Actions** tab in GitHub.

---

## 📁 Repository Structure
```
ai-tech-radar/
│
├── collectors/                  # Data collection modules
│   ├── arxiv.py                 # ArXiv RSS feed collector
│   ├── ai_news.py               # Tech news RSS collector
│   └── github_trending.py       # GitHub trending repo collector
│
├── ai/                          # AI processing layer
│   └── summarizer.py            # Gemini AI summarization engine
│
├── delivery/                    # Output delivery
│   └── telegram.py              # Telegram bot dispatcher
│
├── data/
│   └── digests/                 # 📂 Historical digest archive
│       ├── 2025-01-14.md
│       ├── 2025-01-15.md
│       └── ...
│
├── .github/
│   └── workflows/
│       └── radar.yml            # GitHub Actions CRON pipeline
│
├── main.py                      # Pipeline entry point
├── .env.example                 # Environment variable template
├── pyproject.toml               # Project dependencies (uv)
└── README.md
```

---

## 📋 Example Digest Output

Each digest is stored as a Markdown file in `data/digests/`:
```markdown
# AI Tech Radar — 2025-01-15

## 📰 Top AI News
- OpenAI announces GPT-5 with enhanced reasoning capabilities
- Google DeepMind releases new RL benchmark suite

## 📄 ML Research Papers (ArXiv)
- **Scaling Laws for Reward Model Overoptimization** — Gao et al.
- **Efficient Long-Context Transformers via Sparse Attention** — MIT CSAIL

## 🔥 Trending GitHub Repositories
| Repository | Stars | Description |
|---|---|---|
| huggingface/transformers | ⭐ 128k | State-of-the-art ML models |
| facebookresearch/llama | ⭐ 54k | LLaMA model inference |

---
*Generated at 2025-01-15 08:00 UTC by AI Tech Radar*
```

---

## 🔭 Future Improvements

- [ ] 🌐 **Web Dashboard** — A searchable frontend to browse all historical digests
- [ ] 🎯 **Topic Filtering** — Let users subscribe to specific AI subfields (NLP, CV, RL, etc.)
- [ ] 📊 **Trend Analytics** — Track keyword frequency and topic trends over time
- [ ] 🔔 **Alert System** — Notify on breakthrough papers or viral repos exceeding a threshold
- [ ] 🗣️ **Multi-language Support** — Deliver briefings in multiple languages via Gemini
- [ ] 📧 **Email Digest** — Add an optional email delivery channel alongside Telegram
- [ ] 🤝 **Discord Integration** — Extend delivery to Discord servers

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Built with ☕ and curiosity about the AI frontier.

**[⭐ Star this repo](https://github.com/ISudhan/ai-tech-radar)** if you find it useful!

</div>