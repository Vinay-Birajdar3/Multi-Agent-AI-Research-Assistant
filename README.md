# Multi-Agent-AI-Research-System
Built a Multi-Agent AI Research System using LangChain, Python, and Streamlit with autonomous web search, scraping, report generation, and AI-based evaluation workflows.

# Multi-Agent AI Research System

An autonomous AI-powered research system built using LangChain, Python, and Streamlit. The system performs real-time web research, scrapes webpage content, generates structured reports, and evaluates report quality using multiple specialized AI agents.

---

# Features

* 🔍 Real-time web search using Tavily API
* 🌐 Webpage scraping with BeautifulSoup
* 🤖 Multi-agent AI workflow using LangChain
* 📝 Automated research report generation
* 📊 AI-based report evaluation and feedback
* 🔄 Shared state orchestration pipeline
* 🎨 Interactive Streamlit frontend

---

# Tech Stack

* Python
* LangChain
* OpenAI API
* Tavily Search API
* Streamlit
* BeautifulSoup
* LCEL (LangChain Expression Language)

---

# Project Workflow

User Query
↓
Search Agent → Retrieves web sources
↓
Reader Agent → Extracts webpage content
↓
Writer Chain → Generates research report
↓
Critic Chain → Evaluates report quality
↓
Final Output

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/multi-agent-ai-research-system.git

cd multi-agent-ai-research-system
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory and add:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Project Structure

```bash
├── app.py
├── agents.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── .env
└── README.md
```

---

# Key Concepts Used

* Multi-Agent Systems
* Agentic AI Workflows
* Tool Calling
* State Management
* LCEL Pipelines
* Web Scraping
* LLM Orchestration

---

# Future Improvements

* Add memory support
* Integrate vector databases
* Multi-step reasoning agents
* PDF report export
* Async parallel agent execution
* Local LLM support

---

# Author

Vinay Birajdar & Sankalp Kale

---

