import streamlit as st
from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain
import time

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="AI Research System",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "Multi-Agent AI Research System v1.0"}
)

# ============================================================================
# CUSTOM STYLING
# ============================================================================
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        animation: fadeIn 0.5s;
    }
    
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    .step-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .step-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #667eea;
        margin-bottom: 1rem;
    }
    
    .step-content {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    .success-badge {
        display: inline-block;
        background: #10b981;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    
    .info-badge {
        display: inline-block;
        background: #3b82f6;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    .sidebar-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
    }
    
    .report-score {
        font-size: 2.5rem;
        font-weight: 700;
        color: #667eea;
        text-align: center;
    }
    
    .url-badge {
        display: inline-block;
        background: #e0e7ff;
        color: #667eea;
        padding: 0.4rem 0.8rem;
        border-radius: 6px;
        font-size: 0.85rem;
        margin: 0.3rem 0.3rem 0.3rem 0;
        word-break: break-word;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HEADER
# ============================================================================
st.markdown('<div class="main-header">🔬 Multi-Agent AI Research System</div>', unsafe_allow_html=True)
st.markdown("""
<div class="sub-header">
    Autonomous AI-powered research platform with intelligent web search, content analysis, 
    report generation, and quality evaluation powered by advanced multi-agent workflows.
</div>
""", unsafe_allow_html=True)

st.divider()

# ============================================================================
# SIDEBAR CONFIGURATION
# ============================================================================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-card">
        <h3 style="margin-top: 0;">⚙️ Research Configuration</h3>
        <p style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 0;">Configure and execute your research query</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Topic Input
    topic = st.text_input(
        "🔍 Research Topic",
        placeholder="e.g., Quantum Computing, AI in Healthcare, Climate Change Solutions",
        help="Enter the topic you want to research"
    )
    
    st.divider()
    
    # Information Box
    st.info("""
    **How it works:**
    1. **Search**: Finds recent web sources
    2. **Read**: Scrapes and extracts content
    3. **Write**: Generates structured reports
    4. **Evaluate**: Provides quality feedback
    """)
    
    st.divider()
    
    # Run Button
    run_button = st.button(
        "🚀 Run Research Pipeline",
        use_container_width=True,
        type="primary",
        help="Execute the multi-agent research workflow"
    )
    
    st.divider()
    
    # Stats
    st.subheader("📊 About This System")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Agents", "4", help="Number of AI agents")
    with col2:
        st.metric("Tools", "2", help="Web search & scraping")
    with col3:
        st.metric("LLM", "Groq", help="Language model")

# ============================================================================
# MAIN CONTENT AREA
# ============================================================================
if run_button and topic:
    st.success(f"🎯 **Researching:** {topic}")
    st.markdown("---")
    
    # Progress tracking
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # ====================================================================
        # STEP 1: SEARCH AGENT
        # ====================================================================
        status_text.info("⏳ Step 1/4: Searching for information...")
        progress_bar.progress(25)
        
        st.markdown("""
        <div class="step-container">
            <div class="step-title">📊 Step 1: Web Search Results</div>
        </div>
        """, unsafe_allow_html=True)
        
        search_placeholder = st.container()
        
        search_agent = build_search_agent()
        search_result = search_agent(f"Find recent, reliable and detailed information about: {topic}")
        search_results = search_result if search_result else "No results found"
        
        with search_placeholder:
            st.markdown("""
            <div class="step-content">
            """ + search_results.replace('\n', '<br>') + """
            </div>
            """, unsafe_allow_html=True)
        
        # ====================================================================
        # STEP 2: READER AGENT
        # ====================================================================
        status_text.info("⏳ Step 2/4: Scraping content from sources...")
        progress_bar.progress(50)
        
        st.markdown("""
        <div class="step-container">
            <div class="step-title">📄 Step 2: Content Extraction</div>
        </div>
        """, unsafe_allow_html=True)
        
        reader_placeholder = st.container()
        
        reader_agent = build_reader_agent()
        reader_result = reader_agent(f"Based on the following result about '{topic}', pick the most relevant URL and scrape it for deeper content.\n\nSearch Results:\n{search_results[:800]}")
        scraped_content = reader_result if reader_result else "Could not scrape content"
        
        with reader_placeholder:
            st.markdown("""
            <div class="step-content">
            """ + scraped_content[:500].replace('\n', '<br>') + ("""<br><br><em>... (content truncated for display)</em>""" if len(scraped_content) > 500 else "") + """
            </div>
            """, unsafe_allow_html=True)
        
        # ====================================================================
        # STEP 3: WRITER CHAIN
        # ====================================================================
        status_text.info("⏳ Step 3/4: Generating research report...")
        progress_bar.progress(75)
        
        st.markdown("""
        <div class="step-container">
            <div class="step-title">📝 Step 3: Generated Research Report</div>
        </div>
        """, unsafe_allow_html=True)
        
        research_combined = (
            f"SEARCH RESULTS : \n {search_results} \n\n"
            f"DETAILED SCRAPED CONTENT : \n {scraped_content} \n\n"
        )
        
        report = writer_chain.invoke({
            "topic": topic,
            "research": research_combined
        })
        
        # Display report with better formatting
        report_col = st.container()
        with report_col:
            st.markdown("""
            <div class="step-content">
            """ + report.replace('\n', '<br>').replace('**', '<strong>').replace('- ', '• ') + """
            </div>
            """, unsafe_allow_html=True)
        
        # ====================================================================
        # STEP 4: CRITIC CHAIN
        # ====================================================================
        status_text.info("⏳ Step 4/4: Evaluating report quality...")
        progress_bar.progress(90)
        
        feedback = critic_chain.invoke({
            "report": report
        })
        
        # Parse score from feedback
        score = "N/A"
        try:
            if "Score:" in feedback:
                score_text = feedback.split("Score:")[1].split("\n")[0].strip().split("/")[0]
                score = score_text
        except:
            pass
        
        # Display evaluation with score
        st.markdown("""
        <div class="step-container">
            <div class="step-title">✅ Step 4: Quality Evaluation & Feedback</div>
        </div>
        """, unsafe_allow_html=True)
        
        eval_col1, eval_col2, eval_col3 = st.columns([2, 1, 2])
        
        with eval_col2:
            st.markdown(f'<div class="report-score">{score}/10</div>', unsafe_allow_html=True)
            st.markdown('<p style="text-align: center; color: #666; font-size: 0.9rem;">Quality Score</p>', unsafe_allow_html=True)
        
        with eval_col1:
            pass
        
        with eval_col3:
            pass
        
        st.markdown("""
        <div class="step-content">
        """ + feedback.replace('\n', '<br>').replace('**', '<strong>').replace('- ', '• ') + """
        </div>
        """, unsafe_allow_html=True)
        
        # ====================================================================
        # COMPLETION
        # ====================================================================
        progress_bar.progress(100)
        status_text.success("✨ Research pipeline completed successfully!")
        
        st.divider()
        
        # Download section
        st.subheader("📥 Export Results")
        
        full_report = f"""# Research Report: {topic}

## 🔍 Search Results
{search_results}

---

## 📄 Extracted Content
{scraped_content}

---

## 📝 Generated Report
{report}

---

## ✅ Quality Evaluation
{feedback}

---

*Generated by Multi-Agent AI Research System*
*Report Date: {time.strftime('%Y-%m-%d %H:%M:%S')}*
"""
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.download_button(
                label="📥 Download as Markdown",
                data=full_report,
                file_name=f"research_report_{topic.replace(' ', '_')}.md",
                mime="text/markdown",
                use_container_width=True
            )
        
        with col2:
            st.download_button(
                label="📄 Download as Text",
                data=full_report,
                file_name=f"research_report_{topic.replace(' ', '_')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        # Show stats
        st.divider()
        st.subheader("📊 Research Summary")
        
        metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
        
        with metrics_col1:
            st.metric("Report Quality", f"{score}/10", help="Quality score from critic agent")
        
        with metrics_col2:
            search_count = search_results.count("Title:")
            st.metric("Sources Found", search_count, help="Number of web sources")
        
        with metrics_col3:
            report_length = len(report.split())
            st.metric("Words in Report", report_length, help="Total words in generated report")
        
        with metrics_col4:
            st.metric("Topics", topic.count(" ") + 1, help="Number of topics covered")
    
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
        st.info("Please check your API keys in the .env file and try again.")

elif run_button and not topic:
    st.warning("⚠️ Please enter a research topic to proceed!")
    st.info("👈 Enter a topic in the sidebar and click 'Run Research Pipeline' to get started!")

else:
    # Welcome section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🔍 Smart Search
        Find recent, reliable sources from across the web using advanced search algorithms.
        """)
    
    with col2:
        st.markdown("""
        ### 📚 Content Analysis
        Automatically extract and analyze relevant information from multiple sources.
        """)
    
    with col3:
        st.markdown("""
        ### 📝 Report Generation
        Generate comprehensive, well-structured research reports automatically.
        """)
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🤖 Multi-Agent AI
        Multiple specialized AI agents work together for superior results.
        """)
    
    with col2:
        st.markdown("""
        ### ⚡ Fast & Reliable
        Get instant research results with high-quality analysis.
        """)
    
    with col3:
        st.markdown("""
        ### 💾 Easy Export
        Download your reports in multiple formats for easy sharing.
        """)
    
    st.divider()
    
    st.info("""
    👈 **Getting Started:**
    1. Enter a research topic in the sidebar
    2. Click the "Run Research Pipeline" button
    3. Watch the AI agents work their magic
    4. Download your comprehensive research report
    """)

