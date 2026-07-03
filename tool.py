from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from tavily import TavilyClient
import os
from rich import print
import streamlit as st

load_dotenv()

# Get API key from Streamlit secrets (for cloud) or environment variables (for local)
try:
    tavily_api_key = st.secrets["TAVILY_API_KEY"]
except (KeyError, FileNotFoundError):
    tavily_api_key = os.getenv("TAVILY_API_KEY")

tavily = TavilyClient(api_key=tavily_api_key)

#tool 1
@tool
def web_search(query: str) -> str:
  """Search the web for recent and reliable information on a topic . Returns Titles, URLs and snippets"""
  results = tavily.search(query = query, max_results=5)
  out = []
  
  for r in results['results']:
    out.append(
      f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
    )
    
  return "\n--------\n".join(out)

#print(web_search.invoke("What is the recent news of war?"))

@tool
def scrape_url(url: str) -> str:
  """Scrape and return clean text content from a given URL for deeper reading."""
  try:
    resp = requests.get(url, timeout=8, headers={'User-Agent': "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
      tag.decompose()
    return soup.get_text(separator=" ", strip=True)[:3000]
  except Exception as e:
    return f"Could not scrape URL: {str(e)}"
  
#print(scrape_url.invoke("https://desifakes.com/threads/pooja-hegde-fantasy.45938/"))