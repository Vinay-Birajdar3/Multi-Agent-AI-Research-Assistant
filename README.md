# 🔬 Multi-Agent AI Research System

A powerful AI-driven research platform that automatically searches the web, extracts information, generates detailed reports, and evaluates their quality. Perfect for academics, journalists, content creators, and anyone needing quick, accurate research!

---

## 📋 Table of Contents

- [What is This Project?](#what-is-this-project)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Project Architecture](#project-architecture)
- [Technology Stack](#technology-stack)
- [Installation Guide](#installation-guide)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Detailed Explanation](#detailed-explanation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## What is This Project?

This is an **Intelligent Research Assistant** that uses multiple AI agents working together to help you research any topic automatically. Instead of manually searching Google, reading articles, and writing summaries, just tell it what you want to research, and it does everything for you!

Think of it as having 4 smart robots:
1. **The Searcher** - Finds relevant information online
2. **The Reader** - Reads and understands the content
3. **The Writer** - Creates a well-structured report
4. **The Critic** - Reviews the report and gives feedback

---

## Key Features

✨ **Automated Research Pipeline**
- Searches for reliable information automatically
- Extracts content from multiple sources
- Generates professional reports
- Evaluates report quality

🎨 **Beautiful Web Interface**
- Modern, user-friendly dashboard
- Real-time progress tracking
- Visual quality scores
- Easy export options

📥 **Multiple Export Formats**
- Download as Markdown
- Download as Plain Text
- Formatted for easy sharing

⚙️ **Powered by Advanced AI**
- Uses Groq's lightning-fast LLaMA model
- Integrates with Tavily search API
- BeautifulSoup for intelligent web scraping
- LangChain for agent orchestration

---

## How It Works

### The 4-Step Process

```
1. SEARCH PHASE
   ↓
   AI searches the web and finds 5 reliable sources
   ↓
2. READ PHASE
   ↓
   AI reads and extracts important information from sources
   ↓
3. WRITE PHASE
   ↓
   AI writes a complete, well-structured report
   ↓
4. EVALUATE PHASE
   ↓
   AI reviews the report and gives quality feedback
   ↓
   FINAL REPORT READY FOR DOWNLOAD
```

### What Happens in Each Step

**Step 1: Search Agent** 🔍
- Takes your research topic
- Searches across the internet
- Finds 5 most relevant and reliable sources
- Returns titles, URLs, and snippets

**Step 2: Reader Agent** 📖
- Takes the search results
- Picks the best source to read
- Extracts the main content from the webpage
- Cleans up unnecessary information (ads, navigation, etc.)
- Returns clean, readable text

**Step 3: Writer Chain** ✍️
- Combines search results and extracted content
- Creates a professional research report
- Includes: introduction, key findings, conclusion, sources
- Uses proper formatting and structure

**Step 4: Critic Chain** ⭐
- Reviews the generated report
- Provides quality score (out of 10)
- Identifies strengths
- Suggests improvements
- Gives final verdict

---

## Project Architecture

### System Diagram

```
┌─────────────────┐
│  User Input     │
│  (Research      │
│   Topic)        │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│    STREAMLIT WEB INTERFACE          │
│  (Beautiful UI with progress bars)  │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│    MULTI-AGENT PIPELINE             │
│                                     │
│  ┌──────────────────────────────┐  │
│  │ 1. Search Agent              │  │
│  │    (Web Search via Tavily)   │  │
│  └──────────────────────────────┘  │
│            ↓                        │
│  ┌──────────────────────────────┐  │
│  │ 2. Reader Agent              │  │
│  │    (Content Extraction)      │  │
│  └──────────────────────────────┘  │
│            ↓                        │
│  ┌──────────────────────────────┐  │
│  │ 3. Writer Chain              │  │
│  │    (Report Generation)       │  │
│  └──────────────────────────────┘  │
│            ↓                        │
│  ┌──────────────────────────────┐  │
│  │ 4. Critic Chain              │  │
│  │    (Quality Evaluation)      │  │
│  └──────────────────────────────┘  │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│  OUTPUT & DOWNLOADS                 │
│  - Markdown Report                  │
│  - Text Report                      │
│  - Quality Metrics                  │
└─────────────────────────────────────┘
```

---

## Technology Stack

### AI & Language Models
- **Groq API** - Fast AI inference (LLaMA 3.1 8B model)
- **LangChain** - Framework for building AI agent workflows
- **LangChain-Groq** - Integration between LangChain and Groq

### Web Integration
- **Tavily API** - Intelligent web search
- **BeautifulSoup4** - Web scraping and HTML parsing
- **Requests** - HTTP library for web requests

### User Interface
- **Streamlit** - Modern web app framework
- **Python 3.12** - Programming language

### Utilities
- **python-dotenv** - Environment variable management
- **lxml** - Fast HTML/XML parsing

---

## Installation Guide

### Prerequisites

You need:
- **Python 3.8 or higher** (preferably 3.12)
- **Git** (for cloning the repository)
- **API Keys**: Groq and Tavily (free tier available)

### Step 1: Get API Keys

**Groq API Key:**
1. Go to https://console.groq.com
2. Sign up for a free account
3. Create a new API key
4. Copy your API key

**Tavily API Key:**
1. Go to https://tavily.com
2. Sign up for free
3. Get your API key from the dashboard
4. Copy your API key

### Step 2: Clone the Repository

```bash
git clone https://github.com/Vinay-Birajdar3/Multi-Agent-AI-Research-Assistant.git
cd Multi-Agent-AI-Research-Assistant
```

### Step 3: Create Virtual Environment

This isolates project dependencies so they don't conflict with other projects.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all required packages automatically.

### Step 5: Set Up Environment Variables

Create a `.env` file in the project folder and add:

```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

Replace `your_groq_api_key_here` and `your_tavily_api_key_here` with your actual keys.

---

## Setup Instructions

### Quick Start (5 Minutes)

1. **Install Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create `.env` file** with your API keys (see Installation Guide)

3. **Start the web application:**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser:**
   ```
   http://localhost:8501
   ```

5. **Use the interface:**
   - Enter a research topic
   - Click "Run Research Pipeline"
   - Wait for results
   - Download your report

---

## How to Use

### Using the Web Interface (Recommended)

**1. Start the Application:**
```bash
streamlit run app.py
```

**2. Open Your Browser:**
Visit `http://localhost:8501`

**3. Enter Research Topic:**
- In the left sidebar, enter what you want to research
- Examples:
  - "Artificial Intelligence in Healthcare"
  - "Climate Change Solutions"
  - "Quantum Computing Basics"
  - "Machine Learning Algorithms"

**4. Click "Run Research Pipeline"**
- Watch the progress bar as each step completes
- See real-time results for each agent

**5. Review Results:**
- Search results with sources
- Extracted content from pages
- Generated research report
- Quality evaluation and score

**6. Download Report:**
- Click "Download as Markdown" or "Download as Text"
- Use it in your project, blog, or presentation

### Using Command Line (Alternative)

**1. Run Pipeline Directly:**
```bash
python pipeline.py
```

**2. Enter Topic When Prompted:**
```
Enter a research topic : Renewable Energy
```

**3. Get Output:**
- Prints all 4 steps to console
- Shows final report and evaluation

---

## Project Structure

```
Multi-Agent-AI-Research-Assistant/
│
├── app.py                 # Main Streamlit web application
├── agents.py              # AI agents definition (Search, Reader, Writer, Critic)
├── tools.py               # Tools for web search and scraping
├── pipeline.py            # Main research pipeline orchestration
├── requirements.txt       # Python dependencies
├── .env                   # API keys (keep secret, don't share!)
├── .gitignore             # Files to ignore in git
└── README.md              # This file

```

### File Descriptions

**app.py** (400+ lines)
- Modern Streamlit UI
- Beautiful layout with gradients and animations
- Handles user input
- Displays research results
- Manages file downloads
- Shows progress tracking

**agents.py** (100+ lines)
- Defines Search Agent (web search)
- Defines Reader Agent (content extraction)
- Defines Writer Chain (report writing)
- Defines Critic Chain (evaluation)
- Configures Groq LLM

**tools.py** (50+ lines)
- `web_search()` function - Searches web via Tavily API
- `scrape_url()` function - Extracts content from webpages
- Error handling for API failures

**pipeline.py** (50+ lines)
- Orchestrates 4-step process
- Combines agent outputs
- Main entry point for CLI usage

**requirements.txt**
- Lists all Python packages needed
- Auto-installed with `pip install -r requirements.txt`

---

## Detailed Explanation

### How Search Agent Works

```python
# Input: "Find information about Quantum Computing"
# 
# Process:
# 1. Sends query to Tavily API
# 2. Tavily searches internet
# 3. Returns 5 best results with:
#    - Title
#    - URL
#    - Snippet (preview text)
#
# Output:
# Title: "Quantum Computing Explained - MIT"
# URL: https://...
# Snippet: "Quantum computers use quantum bits..."
```

### How Reader Agent Works

```python
# Input: Search results with URLs
#
# Process:
# 1. Picks best URL from results
# 2. Downloads HTML from webpage
# 3. Uses BeautifulSoup to parse HTML
# 4. Removes: scripts, styles, navigation, ads
# 5. Extracts: main content text
# 6. Limits to first 3000 characters
# 7. Applies 8-second timeout (no slow pages)
#
# Output: Clean, readable text content
```

### How Writer Chain Works

```python
# Input: 
# - Research topic
# - Search results
# - Extracted content
#
# Process:
# 1. Creates prompt with all input data
# 2. Sends to Groq LLM (AI)
# 3. LLM generates structured report with:
#    - Introduction
#    - Key Findings (3-5 points)
#    - Conclusion
#    - Source citations
#
# Output: Professional research report
```

### How Critic Chain Works

```python
# Input: Generated research report
#
# Process:
# 1. Creates evaluation prompt
# 2. Sends report to Groq LLM
# 3. LLM provides:
#    - Quality Score (0-10)
#    - Strengths (what's good)
#    - Weaknesses (what could improve)
#    - Verdict (recommendation)
#
# Output: Quality evaluation feedback
```

### API Keys Explained

**Groq API Key**
- Gives access to fast AI model (LLaMA 3.1)
- Used for: writing, understanding, evaluating
- Free tier: Generous limits
- Where: agents.py line 12

**Tavily API Key**
- Gives access to smart web search
- Used for: finding web sources
- Free tier: 100 searches/month
- Where: tools.py line 15

---

## Troubleshooting

### Problem: "API Key Invalid"
**Solution:**
- Check `.env` file has correct keys
- Ensure no extra spaces or quotes
- Format: `GROQ_API_KEY=key_without_quotes`
- Regenerate keys from respective dashboards

### Problem: "ModuleNotFoundError"
**Solution:**
```bash
# Activate virtual environment first
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Then install dependencies
pip install -r requirements.txt
```

### Problem: "Streamlit not found"
**Solution:**
```bash
# Make sure venv is activated, then:
pip install streamlit==1.58.0
```

### Problem: "Web scraping returns empty"
**Solution:**
- Some websites block scraping
- Try with different search topic
- System automatically handles failures
- Check API limits (Tavily free tier: 100/month)

### Problem: "Slow responses"
**Solution:**
- Groq API should be instant
- Check internet connection
- Tavily API might need moment
- Scraping has 8-second timeout

### Problem: ".env file not found"
**Solution:**
```bash
# Create .env file in project root:
echo GROQ_API_KEY=your_key_here > .env
echo TAVILY_API_KEY=your_key_here >> .env
```

### Problem: Port 8501 already in use
**Solution:**
```bash
# Use different port:
streamlit run app.py --server.port 8502
```

---

## Understanding the Code Flow

### When You Click "Run Research Pipeline"

```
1. app.py receives topic from sidebar
2. app.py calls build_search_agent()
3. Search Agent queries Tavily API
4. Returns 5 sources
5. app.py displays search results
6. app.py calls build_reader_agent()
7. Reader Agent scrapes best source
8. Returns extracted content
9. app.py displays extracted content
10. app.py calls writer_chain.invoke()
11. LLM generates report
12. app.py displays report
13. app.py calls critic_chain.invoke()
14. LLM evaluates report
15. app.py displays evaluation
16. Progress bar reaches 100%
17. Download buttons appear
```

---

## Example Usage

### Research Topic: "AI in Healthcare"

**Input:**
```
Topic: AI in Healthcare
```

**Step 1 Output:**
```
Found 5 sources:
- "AI Transforming Medical Diagnostics" - Medical Journal
- "Machine Learning in Drug Discovery" - Tech Today
- "AI-Powered Healthcare Systems" - Healthcare Weekly
...
```

**Step 2 Output:**
```
Extracted Content:
Artificial intelligence is revolutionizing healthcare
by improving diagnostic accuracy. Deep learning models
can detect diseases from medical images with higher
accuracy than human radiologists...
```

**Step 3 Output:**
```
# AI in Healthcare Research Report

## Introduction
Healthcare industry is experiencing a transformation...

## Key Findings
1. AI improves diagnostic accuracy by 15-20%
2. Machine learning accelerates drug discovery
3. Natural language processing aids clinical notes analysis

## Conclusion
AI is becoming essential in modern healthcare...

## Sources
- [Title](URL)
- [Title](URL)
```

**Step 4 Output:**
```
Quality Score: 8/10

Strengths:
✓ Well-structured report
✓ Accurate information
✓ Good source citations

Weaknesses:
- Could include more recent data
- Missing some alternative perspectives

Verdict: Good quality report suitable for academic use
```

---

## Tips for Best Results

1. **Be Specific** - "AI in Healthcare" better than "AI"
2. **Use Recent Topics** - Current events get better results
3. **Try Multiple Topics** - See different outputs
4. **Review Quality Scores** - 7+/10 is excellent
5. **Download Reports** - Keep them for reference

---

## Frequently Asked Questions

**Q: Can I use this without API keys?**
A: No, you need Groq and Tavily API keys. Both have free tiers.

**Q: How accurate are the reports?**
A: Very accurate! AI combines multiple sources and expert writing. Quality scores help you evaluate results.

**Q: Can I modify the code?**
A: Yes! Fork the repository and make your own improvements.

**Q: What are rate limits?**
A: Tavily free tier: 100 searches/month. Groq: very generous limits.

**Q: Can I deploy this online?**
A: Yes! Use Streamlit Cloud, Heroku, or any Python hosting.

**Q: Is my data private?**
A: Your `.env` file is private. Reports are not stored.

---

## Contributing

Want to improve this project? 

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit (`git commit -m 'Add amazing feature'`)
5. Push (`git push origin feature/amazing-feature`)
6. Open a Pull Request

---

## License

This project is open source and available under the MIT License.

---

## Support & Feedback

- 🐛 Found a bug? Open an issue
- 💡 Have an idea? Start a discussion
- ❓ Have questions? Check the FAQ section

---

## Changelog

### Version 1.0 (Current)
✅ Core 4-agent research pipeline
✅ Beautiful Streamlit UI
✅ Multiple export formats
✅ Quality evaluation system
✅ Progress tracking
✅ Error handling

---

## Future Improvements

🔄 Planned Features:
- Support for more LLM providers
- Custom agent configurations
- Multi-language support
- PDF export
- Report caching
- Research history
- Collaborative research
- API endpoint for integration

---

## Acknowledgments

- **Groq** - Fast AI inference
- **Tavily** - Intelligent web search
- **LangChain** - Agent framework
- **Streamlit** - Web UI framework
- **BeautifulSoup** - Web scraping

---

## Quick Links

- [Groq Console](https://console.groq.com)
- [Tavily API](https://tavily.com)
- [Streamlit Docs](https://docs.streamlit.io)
- [LangChain Docs](https://python.langchain.com)

---

**Happy Researching! 🚀**

*Built with ❤️ using AI and Python*

