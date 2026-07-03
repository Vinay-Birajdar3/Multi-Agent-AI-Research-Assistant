from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tool import web_search, scrape_url
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
  model = "llama-3.1-8b-instant",
  temperature = 0,
)

# creating first agent - bind tools and call directly
def build_search_agent():
  llm_with_tools = llm.bind_tools([web_search])
  
  def search_runner(query):
    messages = [("user", query)]
    response = llm_with_tools.invoke(messages)
    # Extract tool use and execute
    if hasattr(response, 'tool_calls') and response.tool_calls:
      for tool_call in response.tool_calls:
        if tool_call['name'] == 'web_search':
          result = web_search.invoke(tool_call['args']['query'])
          return result
    return str(response)
  
  return search_runner
  
# creating second agent

def build_reader_agent():
  llm_with_tools = llm.bind_tools([scrape_url])
  
  def reader_runner(url):
    messages = [("user", url)]
    response = llm_with_tools.invoke(messages)
    # Extract tool use and execute
    if hasattr(response, 'tool_calls') and response.tool_calls:
      for tool_call in response.tool_calls:
        if tool_call['name'] == 'scrape_url':
          result = scrape_url.invoke(tool_call['args']['url'])
          return result
    return str(response)
  
  return reader_runner
  
# writer chain: we will use LCEL pipline/ Runnables

writer_prompt = ChatPromptTemplate.from_messages([
  ("system", "You are an expert research writer. Write clear, structured and insightful reports"),
  ("human", """Write a detailed research report on the topic below.
   
   Topic: {topic}
   
   Resarch Gathered:
   {research}
   
   Structure the report as:
   - Introduction
   - key Findings (minimum 3 well-explained points)
   - Conclusion
   - Sources (list all URLs found in the research)
   
   Be detailed, factual and professional,
   """),
])
 
# this chain will technially will generate our output
writer_chain = writer_prompt | llm | StrOutputParser()

#Critic_chain/ to get feed back on our research work

critic_prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a sharp and constructive research critic. Be honest and specific"),
  ("human", """Review the research report below and evaluate it strictly.
   Report:
   {report}
   Respond in this exact format:
   
   Score: X/10
   
   Strengths:
   - ...
   - ...
   
   Areas  to Improve:
   - ...
   - ...
   
   One line verdict:
   - ...
   - ..."""),
])

# critic chain
critic_chain = critic_prompt | llm | StrOutputParser()
