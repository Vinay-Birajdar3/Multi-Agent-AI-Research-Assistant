from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

def run_research_pipeline(topic: str) -> dict: # using dict to save output of tool and agent in aprticular state
  
  state = {} # local storage to store the result of 1st agent and 2nd too
  
  # search agent working
  print("\n" +" ="*50)
  print("step 1 - search agent is working....")
  print("="*50)
  
  search_agent = build_search_agent()
  search_result = search_agent(f"Find recent, reliable and detailed information about: {topic}")

  state["search_results"] = search_result if search_result else "No results found"

  print(state["search_results"])
  
  # step 2- reader agent
  print("\n" +" ="*50)
  print("step 2 - reader agent is scraping top resources....")
  print("="*50)
  
  reader_agent = build_reader_agent()
  # Extract a URL if available from search results
  reader_result = reader_agent(f"Based on the following result about '{topic}', pick the most relevant URL and scrape it for deeper content.\n\nSearch Results:\n{state['search_results'][:800]}")
  
  state['scraped_content'] = reader_result if reader_result else "No content scraped"
  
  print("\nscraped content\n", state['scraped_content'])  
  
  #step 3 - writer chain
  print("\n" +" ="*50)
  print("step 3 - writer is drafting the report....")
  print("="*50)
  
  # combining to get combined result both agent
  research_combined = (
    f"SEARCH RESULTS : \n {state['search_results']} \n\n"
    f"DETAILED SCRAPPED CONTENT : \n {state['scraped_content']} \n\n"
  )
  
  state["report"] = writer_chain.invoke({
    "topic": topic,
    "research" : research_combined
  })
  
  print("\n Final Report\n", state['report'])
  
  #step-4 Critic report
  print("\n" +" ="*50)
  print("step 4 - critic is reviewing the report....")
  print("="*50)
  
  state["feedback"] = critic_chain.invoke({
    "report":state['report']
  })
  
  print("\n Critic report \n", state['feedback'])
  
  return state

if __name__ == "__main__":
  topic = input("\n Enter a research topic :")
  run_research_pipeline(topic)