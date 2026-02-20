<div align="center">

# 🤖 Personal Task Automation Agent
### An AI-Powered Productivity System for Gmail, Google Calendar & Notion

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-LLM_Core-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev)
[![Gmail API](https://img.shields.io/badge/Gmail_API-Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](https://developers.google.com/gmail)
[![Google Calendar](https://img.shields.io/badge/Google_Calendar-Scheduling-4285F4?style=for-the-badge&logo=google-calendar&logoColor=white)](https://developers.google.com/calendar)
[![Notion API](https://img.shields.io/badge/Notion_API-Task_Management-000000?style=for-the-badge&logo=notion&logoColor=white)](https://developers.notion.com)
[![Pydantic](https://img.shields.io/badge/Pydantic_v2-Validation-E92063?style=for-the-badge)](https://docs.pydantic.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

<br/>

> *"Stop managing your tools. Let your tools manage themselves."*

A sophisticated **multi-agent productivity system** that eliminates the "Cognitive Tax" of daily digital work. This agent integrates with Gmail, Google Calendar, and Notion to autonomously process emails, manage your schedule, and track tasks — all through a single natural language interface powered by Google Gemini.

[**✨ Features**](#-key-features) · [**🏗️ Architecture**](#-architecture) · [**🚀 Setup**](#-installation--setup) · [**💡 Usage**](#-usage)

---

</div>

## 📌 The Cognitive Tax Problem

Every knowledge worker faces an invisible daily cost:

- **Inbox overload** — reading, triaging, and responding to emails consumes 2+ hours a day
- **Calendar fragmentation** — scheduling, rescheduling, and conflict checking requires constant context switching
- **Task scatter** — action items from emails, meetings, and messages end up in different systems, or nowhere at all
- **The "Daily Setup" ritual** — pulling together what needs to happen today from 3 different apps every morning

**This agent automates all of it using a coordinated fleet of specialized AI sub-agents.**

---

## ✨ Key Features

### 🧠 Master Orchestrator
The brain of the system. Routes every natural language request to the right specialist:
- **Semantic Routing**: Uses Gemini Pro to classify intent (`EMAIL`, `CALENDAR`, `TASK`) before dispatching
- **Predefined Workflows**: Executes complex, multi-step flows like the **Daily Briefing** that synthesizes data from all three platforms in a single run
- **Extensible**: New agents can be registered into the orchestrator with a single method call

### 📧 Email Analysis Agent
Your autonomous inbox manager:
- **Autonomous Reading**: Fetches and processes unread Gmail messages without manual intervention
- **LLM-Powered Summarization**: Gemini reads raw email content and produces clean, actionable summaries
- **Priority Flagging**: Identifies the most critical messages from your inbox and surfaces them first
- **Natural Language Queries**: Ask *"Summarize my top 5 unread emails"* in plain English

### 📅 Calendar Management Agent
Your AI scheduling assistant:
- **Event Creation**: Create calendar events from natural language — *"Schedule a meeting with the team tomorrow at 3 PM for one hour"*
- **Schedule Inspection**: Query your calendar naturally — *"What's on my calendar for today?"*
- **Event Updates**: Modify existing events by describing the change in plain English
- **Conflict-Aware**: Surfaces upcoming events to help humans catch scheduling conflicts before they happen

### ✅ Task Management Agent (Notion)
Transforms action items into tracked tasks automatically:
- **Instant Task Creation**: Creates structured Notion database entries with title, status, and priority in one command
- **Priority-Based Listing**: Query *"List my high priority tasks"* to surface what matters most
- **Status Tracking**: Update task status (`Not Started` → `In Progress` → `Done`) via natural language
- **Pydantic-Validated**: All Notion API calls are schema-validated before execution, preventing malformed requests

### 🔔 Notification Agent
Background monitoring and alerting:
- **Scheduled Checks**: Runs on a configurable schedule using the `schedule` library
- **Proactive Alerts**: Surfaces urgent emails and upcoming calendar events without being asked
- **Silent Background Operation**: Designed to run as a background worker alongside the main orchestrator

### 🔄 Daily Briefing Workflow
A one-command morning briefing that synthesizes your entire day:
1. Fetches today's **calendar events**
2. Retrieves **high-priority Notion tasks**
3. Summarizes your **top unread emails**
4. Passes all data to Gemini for a **cohesive, encouraging daily briefing**

### 🛡️ Resilience Engine
Built-in reliability for all external API calls:
- **Exponential Backoff**: Automatically retries failed API calls with increasing wait times
- **Error Isolation**: Each service layer catches and logs exceptions independently — one failing service doesn't crash the whole system
- **Structured Logging**: Python's `logging` module with configurable `LOG_LEVEL` for full observability

---

## 🛠️ Tech Stack

| Category | Library | Purpose |
|---|---|---|
| **Core Language** | Python `3.10+` | Primary runtime |
| **LLM Framework** | LangChain + LangChain-Community | Agent construction, tool binding, prompt templating |
| **LLM Provider** | `langchain-google-genai` / Gemini Pro | Natural language understanding and generation |
| **Orchestration** | LangChain AgentExecutor | Sub-agent execution and tool loop management |
| **Google APIs** | `google-api-python-client` | Gmail and Google Calendar REST API client |
| **Google Auth** | `google-auth-oauthlib`, `google-auth-httplib2` | OAuth 2.0 flow and credential management |
| **Notion** | `notion-client` | Notion database read/write via official SDK |
| **Data Validation** | Pydantic v2 + Pydantic Settings | Schema validation for all tool inputs and config |
| **Scheduling** | `schedule` | Background task scheduling for the Notification Agent |
| **Config** | `python-dotenv` | `.env` file loading for secrets management |

---

## 🏗️ Architecture

The system is built on a clean **4-layer Service-Tool-Agent-Orchestrator** separation. No layer has knowledge of the layers above it.

```
┌─────────────────────────────────────────────────────────────────┐
│                        User / CLI Input                         │
└───────────────────────────────┬─────────────────────────────────┘
                                │ Natural Language Request
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Layer 4: Orchestration                        │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                  MasterOrchestrator                     │   │
│   │  • Classifies intent: EMAIL | CALENDAR | TASK | GENERAL │   │
│   │  • Routes to the correct sub-agent                      │   │
│   │  • Runs predefined workflows (e.g., Daily Briefing)     │   │
│   └─────────────┬───────────────┬──────────────┬────────────┘   │
└─────────────────┼───────────────┼──────────────┼────────────────┘
                  ▼               ▼              ▼
┌──────────────────────────────────────────────────────────────────┐
│                     Layer 3: Agent Fleet                         │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │  EmailAgent  │  │CalendarAgent │  │     TaskAgent        │   │
│  │              │  │              │  │                      │   │
│  │ LangChain    │  │ LangChain    │  │ LangChain            │   │
│  │ AgentExec-   │  │ AgentExec-   │  │ AgentExecutor        │   │
│  │ utor with    │  │ utor with    │  │ with Notion Tools    │   │
│  │ Gmail Tools  │  │ Cal. Tools   │  │                      │   │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘   │
└─────────┼─────────────────┼────────────────────┼────────────────┘
          ▼                 ▼                    ▼
┌──────────────────────────────────────────────────────────────────┐
│                     Layer 2: Tool Layer                          │
│                                                                  │
│  gmail_tools.py        calendar_tools.py     notion_tools.py     │
│  • ReadEmailTool       • CalendarCreateTool  • NotionCreateTask  │
│  • SummarizeEmailTool  • CalendarListTool    • NotionListTasks   │
│                        • CalendarUpdateTool  • NotionUpdateTask  │
│                                                                  │
│  All tools extend LangChain BaseTool with Pydantic arg schemas   │
└──────────┬─────────────────┬────────────────────┬───────────────┘
           ▼                 ▼                    ▼
┌──────────────────────────────────────────────────────────────────┐
│                    Layer 1: Service Layer                        │
│                                                                  │
│  gmail_service.py      calendar_service.py   notion_service.py  │
│  auth_service.py                                                 │
│                                                                  │
│  Low-level API wrappers with integrated retry/backoff logic      │
└──────────────────────────────────────────────────────────────────┘
```

### Layer Responsibilities

| Layer | Files | Responsibility |
|---|---|---|
| **Service Layer** | `gmail_service.py`, `calendar_service.py`, `notion_service.py`, `auth_service.py` | Raw API communication, OAuth token management, retry/backoff logic |
| **Tool Layer** | `gmail_tools.py`, `calendar_tools.py`, `notion_tools.py` | LangChain `BaseTool` wrappers with Pydantic v2 input schemas that standardize how agents interact with services |
| **Agent Layer** | `email_agent.py`, `calendar_agent.py`, `task_agent.py`, `notification_agent.py` | Independent LangChain AgentExecutors, each equipped with the relevant tools for their domain |
| **Orchestration Layer** | `orchestrator.py` | `MasterOrchestrator` class — semantic intent routing, workflow execution, and agent coordination |

---

## 🚀 Installation & Setup

### Prerequisites

Before you start, you'll need:

- **Python** `3.10+`
- A **Google Cloud Project** with **Gmail API** and **Google Calendar API** enabled
- A **Google Gemini API Key** (free at [ai.google.dev](https://ai.google.dev))
- A **Notion Internal Integration** with access to a task database

---

### Step 1 — Clone & Install

```bash
# Clone the repository
git clone https://github.com/Ismail-2001/Personal-Task-Automation-Agent.git
cd Personal-Task-Automation-Agent

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate          # macOS / Linux
# venv\Scripts\Activate.ps1      # Windows (PowerShell)

# Install all dependencies
pip install -r requirements.txt
```

---

### Step 2 — Google OAuth Authentication

The Gmail and Calendar agents use **OAuth 2.0** (not a service account), so your credentials are personal to your Google account.

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project → Enable **Gmail API** and **Google Calendar API**
3. Go to **Credentials** → **Create Credentials** → **OAuth 2.0 Client ID**
4. Application type: **Desktop App**
5. Download the JSON file and rename it to `credentials.json`
6. Place it in the `credentials/` directory at the project root:
   ```
   Personal-Task-Automation-Agent/
   └── credentials/
       └── credentials.json   ← here
   ```
7. On first run, a browser window will open for you to authorize access. A `token.json` file will be created automatically for subsequent runs.

---

### Step 3 — Notion Integration

1. Go to [Notion Integrations](https://www.notion.so/my-integrations) → **"+ New Integration"**
2. Give it a name (e.g., `TaskAgent`) and associate it with your workspace
3. Copy the **Internal Integration Token** — this is your `NOTION_API_KEY`
4. Open the Notion database you want to use for tasks
5. Click **"Share"** → **"Invite"** → select your integration
6. Copy the **Database ID** from the database URL:
   ```
   https://www.notion.so/{workspace}/{DATABASE_ID}?v=...
   ```

---

### Step 4 — Environment Variables

Copy the example file and populate it:

```bash
cp .env.example .env
```

Edit `.env`:

```env
# Google OAuth Credentials (from Google Cloud Console)
GOOGLE_CLIENT_ID=your_client_id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your_client_secret

# Notion Integration
NOTION_API_KEY=secret_your_notion_api_key
NOTION_DATABASE_ID=your_notion_database_id

# Google Gemini LLM
GEMINI_API_KEY=your_gemini_api_key

# Logging verbosity: DEBUG | INFO | WARNING | ERROR
LOG_LEVEL=INFO
```

---

## 💡 Usage

### Start the Agent

```bash
python -m src.main
```

On first run, this initializes all three services (Gmail, Calendar, Notion) and validates your credentials.

### Run the Orchestrator

To interact with the master orchestrator directly (run the full conversational agent):

```bash
python tests/test_orchestrator_manual.py
```

Then type any natural language command:

```
> Summarize my top 3 unread emails
> Schedule a call with John tomorrow at 2 PM for 30 minutes
> Create a high priority task: Finalize the Q4 report
> What's on my calendar today?
> List my in-progress tasks
```

### Run the Daily Briefing Workflow

```python
from src.agents.orchestrator import MasterOrchestrator

orchestrator = MasterOrchestrator()
briefing = orchestrator.run_workflow("daily_summary")
print(briefing)
```

**Example output:**
```
Good morning! Here's your day at a glance:

📅 CALENDAR — 2 events today:
  • 10:00 AM: Product Sync with Design Team
  • 3:00 PM: 1:1 with Manager

✅ TASKS — 3 high-priority items:
  • Finalize Q4 report [In Progress]
  • Review PR #241 [Not Started]
  • Send client proposal [Not Started]

📧 EMAILS — Key highlights:
  • Alice (urgent): Budget approval needed by EOD
  • John: Follow-up on yesterday's design review
  • HR Team: Open enrollment deadline this Friday

You've got a focused day ahead. Knock it out! 💪
```

### Run Individual Agent Tests

Validate each sub-agent independently:

```bash
# Test Email Agent
python tests/test_email_agent_manual.py

# Test Calendar Agent
python tests/test_calendar_agent_manual.py

# Test Task Agent (Notion)
python tests/test_task_agent_manual.py

# Run Performance Benchmarks
python tests/test_performance.py
```

---

## 📂 Project Structure

```text
Personal-Task-Automation-Agent/
│
├── src/
│   ├── agents/
│   │   ├── orchestrator.py          # MasterOrchestrator — routing & workflows
│   │   ├── email_agent.py           # Gmail-powered email analysis agent
│   │   ├── calendar_agent.py        # Google Calendar management agent
│   │   ├── task_agent.py            # Notion task management agent
│   │   └── notification_agent.py   # Background monitoring & alerting agent
│   │
│   ├── tools/
│   │   ├── gmail_tools.py           # LangChain tools: read & summarize emails
│   │   ├── calendar_tools.py        # LangChain tools: create, list, update events
│   │   └── notion_tools.py          # LangChain tools: create, list, update tasks
│   │
│   ├── services/
│   │   ├── auth_service.py          # Google OAuth 2.0 token management
│   │   ├── gmail_service.py         # Gmail API low-level wrapper
│   │   ├── calendar_service.py      # Google Calendar API low-level wrapper
│   │   └── notion_service.py        # Notion API low-level wrapper
│   │
│   ├── models/
│   │   └── schemas.py               # Shared Pydantic data models
│   │
│   ├── utils/
│   │   └── config.py                # Pydantic Settings — env var loading & validation
│   │
│   └── main.py                      # Entry point — service initialization & health check
│
├── tests/
│   ├── test_email_agent_manual.py   # Manual Email Agent integration test
│   ├── test_calendar_agent_manual.py # Manual Calendar Agent integration test
│   ├── test_task_agent_manual.py    # Manual Task Agent integration test
│   ├── test_orchestrator_manual.py  # Full orchestrator interactive test
│   ├── test_performance.py          # Response time & throughput benchmarks
│   └── test_agents.py               # Unit tests
│
├── credentials/                     # OAuth token storage (gitignored)
│   └── credentials.json             # ← Place your Google OAuth credentials here
│
├── .env.example                     # Environment variable template
├── requirements.txt                 # Python dependencies
└── README.md
```

---

## 🗺️ Roadmap

### ✅ Phase 1 — Core Agent Fleet (Complete)
- [x] `MasterOrchestrator` with LLM-based semantic routing
- [x] Email Agent with Gmail read & summarization tools
- [x] Calendar Agent with create, list, and update tools
- [x] Task Agent with Notion create, list, and update tools
- [x] Daily Briefing multi-step workflow
- [x] `NotificationAgent` with scheduled background monitoring
- [x] Pydantic v2 schema validation on all tool inputs
- [x] Structured logging with configurable `LOG_LEVEL`

### 🔨 Phase 2 — API & Memory (Next)
- [ ] **FastAPI Integration**: REST endpoints to expose all agent capabilities to web/mobile frontends
- [ ] **Short-term Memory**: Thread/conversation management for context-aware multi-turn interactions
- [ ] **Semantic Routing**: Replace LLM-based intent classification with embedding similarity for faster, cheaper routing

### 📋 Phase 3 — Autonomous Monitoring (Planned)
- [ ] **Proactive Email Monitoring**: Background workers that interrupt with high-urgency email alerts
- [ ] **Calendar Conflict Detection**: Automatically flag overlapping events and suggest resolutions
- [ ] **Slack / Discord Integration**: Interface for mobile notifications and command input without a terminal

### 🔭 Phase 4 — Advanced Intelligence (Vision)
- [ ] **Microsoft 365 Support**: Outlook + Teams + Planner connectors as alternatives to Google Workspace + Notion
- [ ] **Voice Interface**: Natural speech-to-command via Whisper API
- [ ] **Learning from Preferences**: Fine-tune routing and summarization style based on user feedback
- [ ] **Multi-User Workspaces**: Team-level delegation and task assignment across shared Notion databases

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** changes using [Conventional Commits](https://www.conventionalcommits.org/):
   ```bash
   git commit -m "feat: add Outlook email service connector"
   ```
4. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** against `main`

> **Good first contributions**: Adding new LangChain tools, writing additional test cases, or improving error messages in the service layer.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](./LICENSE) for details.

---

<div align="center">

**Built to reclaim your focus from the noise of daily digital work.**

*If this project saved you time, consider starring ⭐ the repo.*

[![GitHub Stars](https://img.shields.io/github/stars/Ismail-2001/Personal-Task-Automation-Agent?style=social)](https://github.com/Ismail-2001/Personal-Task-Automation-Agent)

Maintained by [Ismail Sajid](https://github.com/Ismail-2001)

</div>
