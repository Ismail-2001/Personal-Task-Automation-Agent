# 🤖 Personal Task Automation Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/AI-LangGraph-orange.svg)](https://github.com/langchain-ai/langgraph)

A sophisticated multi-agent system designed to handle the "Cognitive Tax" of daily digital life. This agent integrates with **Gmail**, **Google Calendar**, and **Notion** to autonomously process emails, manage schedules, and track tasks using state-of-the-art LLM orchestration. Built for developers and power users who want a centralized, AI-driven command center for their productivity.

---

## ✨ Key Features

- **🧠 Master Orchestrator**: An intelligent routing system that classifies user requests and delegates them to specialized sub-agents.
- **📧 Email Analysis Agent**: Autonomous reading, categorization, and summarization of unread emails using Google Gemini.
- **📅 Calendar Management Agent**: Smart event creation, conflict detection, and schedule updates via natural language.
- **✅ Task Management Agent**: Seamlessly syncs action items to Notion databases with priority and status tracking.
- **🔄 Multi-Step Workflows**: Predefined complex flows like the "Daily Briefing" which synthesizes data across all platforms.
- **🛡️ Resilience Engine**: Built-in exponential backoff and retry logic for all external API interactions to handle rate limits and transient errors.

---

## 🛠 Tech Stack

- **Core Logic**: [Python 3.10+](https://www.python.org/)
- **AI Orchestration**: [LangGraph](https://github.com/langchain-ai/langgraph) & [LangChain](https://github.com/langchain-ai/langchain)
- **Large Language Model**: [Google Gemini Pro](https://deepmind.google/technologies/gemini/)
- **APIs**: Gmail API, Google Calendar API, Notion API
- **Data Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **Configuration**: [Dotenv](https://pypi.org/project/python-dotenv/) & [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

---

## 🏗 Architecture

The system follows a modular "Service-Tool-Agent" pattern:

1.  **Service Layer**: Low-level wrappers for Google and Notion SDKs with integrated retry logic.
2.  **Tool Layer**: LangChain-compatible tools that provide standardized interfaces for agents.
3.  **Agent Layer**: Independent LangGraph-powered agents (Email, Calendar, Task) that manage state and tool execution.
4.  **Orchestration Layer**: The `MasterOrchestrator` which acts as the system's brain, routing requests via semantic reasoning.

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.10 or higher
- A Google Cloud Project with Gmail and Calendar APIs enabled
- A Notion Integration (Internal Integration Token)
- Google Gemini API Key

### 1. Local Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/personal-task-automation-agent.git
cd personal-task-automation-agent

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 2. Authentication

1.  **Google**: Download your `credentials.json` from the [Google Cloud Console](https://console.cloud.google.com/) and place it in the `credentials/` directory.
2.  **Notion**: Create a database in Notion and share it with your Integration. Copy the Database ID.

### 3. Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_CLIENT_ID=your_id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your_secret
NOTION_API_KEY=secret_notion_api_key
NOTION_DATABASE_ID=your_notion_db_id
GEMINI_API_KEY=your_gemini_api_key
LOG_LEVEL=INFO
```

---

## 💡 Usage

### Run the Orchestrator
The main entry point for interacting with the agent:
```bash
python -m src.main
```

### Running Manual Tests
Validate specific sub-agents independently:
```bash
# Test Email Summarization
python tests/test_email_agent_manual.py

# Test Calendar Scheduling
python tests/test_calendar_agent_manual.py

# Test Performance
python tests/test_performance.py
```

---

## 🎥 Demo / Screenshots

*(Placeholder: Add GIF or Screenshot of terminal interaction here)*

---

## 🗺 Roadmap

- [ ] **FastAPI Integration**: REST endpoints for mobile/web frontends.
- [ ] **Short-term Memory**: Thread management for context-aware multi-turn conversations.
- [ ] **Semantic Routing**: Speed up command processing using embeddings instead of LLM calls.
- [ ] **Proactive Monitoring**: Background workers that alert users of urgent emails or scheduling conflicts.
- [ ] **Slack/Discord Support**: Interface for mobile notifications and commands.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git pull origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
**Maintained by:** Ismail Sajid
