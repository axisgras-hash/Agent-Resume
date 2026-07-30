# #==========LOAD MODULES========================
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_groq import ChatGroq
# import langchain
# from langchain.agents import create_agent

# from tavily import TavilyClient
# import pytesseract as pyt 
# import streamlit as st
# import os
# import time
# from PIL import Image
# import pandas as pd
# import numpy as np



# # To Show web-app: complete page layout
# st.set_page_config(layout="wide")

# # To Give Title
# st.title("AI RESUME GENERATOR")

# st.write("""This app helps user to build customized Professional
# Resume with Latest Job apply links""")

# st.image("https://github.com/axisgras-hash/Agent-Resume/blob/main/bg.png")

# st.sidebar.title("Fill Important Details")
# st.sidebar.image("https://github.com/axisgras-hash/Agent-Resume/blob/main/bg.png")



# # ========API KEYS============# 
# # Step 3 API keys
# TAVILY_API_KEY = st.sidebar.text_input("Tavily-API",type = "password")
# GROQ_API_KEY = st.sidebar.text_input("Groq-API",type = "password")
# GOOGLE_API_KEY = st.sidebar.text_input("Gemini-API",type = "password")

# all_API = [TAVILY_API_KEY,GROQ_API_KEY,
#            GOOGLE_API_KEY ]
# if not all(all_API):
#     st.error("Must give API keys")
#     st.stop()
# elif all(all_API):
#     st.success("API KEYS LOADED SUCCESSFULLY")
# else:
#     st.info("PASS ALL API-KEYS")
    

# # MULTISELECT OPTION
# options = ["Delhi","Mumbai",
#            "Pune","Banglore",
#            "Gurugram/Gurgaon"]
# location = st.sidebar.multiselect("Select Location",
#                                   options = options)

# profile_op = ["Data Analysts","AI Engineer",
#               "Gen AI Developer","Full-Stack Dev",
#               "Data Scientist"]
# profile = st.sidebar.multiselect("Select Job Profile",
#                                   options = profile_op)


# # =========GET USER INFO=============
# st.markdown("""### GET USER INFO""")
# user_info = st.text_area("""Write your Resume Description: """)


# # ================ MODEL====================
# model = ChatGoogleGenerativeAI(
#     model = 'gemini-3.5-flash-lite',
#     google_api_key = GOOGLE_API_KEY
# )

# # response = model.invoke("Hello Buddy!")
# # response.content[-1]['text']


# # ======================TOOLS===============
# def search_latest_news_jobs(query):
#   """This function helps to fetch latest
#   news or jobs related article using
#   tavily"""

#   client = TavilyClient(
#       api_key = TAVILY_API_KEY)
#   response = client.search(query)
#   return response




# # Agent Creation
# agent = create_agent(
#     model = model,
#     tools = [search_latest_news_jobs])

# # agent


# def main_agent(agent, query):
#   """This is main agent, or leader agent
#   orchestrate sub agents"""

#   # Giving prompt to create detailed prompt
#   # for code generation
#   prompt = """You are AI assistant and
#   below given is a prompt, your
#   task is to give detailed prompt for
#   this.
#   You are a professional Resume generator
#   where user will give their personal info,
#   you have to create detailed Resume
#   for students or professional one,
#   it must be with dynamic UI and UX and,
#   with advanced CSS Professional Designing
#   Make sure to give output in HTML format only
#   no markdowns allowed
#   """

#   response = agent.invoke({'messages':[{'role':'user',
#                                         'content':prompt}]})
#   detailed_prompt = response['messages'][-1].content[-1]['text']

#   # SAVE PROMPT using File Handling

#   with open('prompt.txt','w') as f:
#     f.write(detailed_prompt)

#   user_details = f"""Below Given is a user details
#   generate Resume based on that, if not
#   given keep: Default Resume: Python Developer
#   user details: {query}"""

#   final_prompt = prompt + detailed_prompt + user_details

#   # CODE GENERATION
#   response = agent.invoke({'messages':[{'role':'user',
#                                         'content':final_prompt}]})
#   code = response['messages'][-1].content[-1]['text']

#   return code


# # code = main_agent(agent,"ALAN TURING, GEN AI EXPERT")
# # from IPython import display as DISPLAY
# # DISPLAY.HTML(code)



# # Fetch Latest Domain related Jobs using Tavily

# def get_jobs(agent,
#              Location,
#              Profile):
#   Location = "Noida,Delhi"
#   Profile = "Data Analysts, AI Engineer"

#   prompt = f"""Based on user given Job profile,
#   fetch latest jobs or job apply article
#   using Naukri, Linkedin, Indeed, or all popular
#   Job apply platforms, Show Results with
#   JOB PROFILE NAME, LOCATION, SALARY, COMPANY NAME,
#   SHOW jobs only related to given
#   {Location} and {Profile}. Output must be in
#   Professional HTML Naukri theme cards with Dynamic Design,
#   Show atleast Top 10-20 results with direct apply link"""


#   response = agent.invoke({'messages':[{'role':'user',
#                                           'content':prompt}]})
#   code = response['messages'][-1].content[-1]['text']

#   return code

# # code = get_jobs(agent)
# # DISPLAY.HTML(code)


# if st.button("Generate Resume"):
#            with st.spinner("Agent Running"):
#                       code = main_agent(agent,user_info)
#                       st.html(code , width="stretch" , 
#                               unsafe_allow_javascript=True)
#                       st.divider()  # to give horizontal div
#                       job_code = get_jobs(agent,location,profile)
#                       st.html(job_code , width="stretch" , 
#                               unsafe_allow_javascript=True)
                      

# =====================================================================
# 1. MODULES & LIBRARIES
# =====================================================================
import os
import time
from PIL import Image
import numpy as np
import pandas as pd
import streamlit as st
import pytesseract as pyt 

import langchain
from tavily import TavilyClient
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

# =====================================================================
# 2. APPLICATION CONFIGURATION & UI SETUP
# =====================================================================
# To Show web-app: complete page layout
st.set_page_config(layout="wide")

st.title("AI RESUME GENERATOR")
st.write("This app helps users build a customized Professional Resume with Latest Job application links.")

# GitHub image asset verification
IMAGE_URL = "https://githubusercontent.com"
st.image(IMAGE_URL)

st.sidebar.title("Fill Important Details")
st.sidebar.image(IMAGE_URL)

# =====================================================================
# 3. SIDEBAR INTERFACE (API KEYS & CONFIGURATIONS)
# =====================================================================
# Step 3 API keys
TAVILY_API_KEY = st.sidebar.text_input("Tavily-API", type="password")
GROQ_API_KEY = st.sidebar.text_input("Groq-API", type="password")
GOOGLE_API_KEY = st.sidebar.text_input("Gemini-API", type="password")

# Form Location multi-selectors
options = ["Delhi", "Mumbai", "Pune", "Banglore", "Gurugram/Gurgaon"]
location = st.sidebar.multiselect("Select Location", options=options)

# Form Profile multi-selectors
profile_op = ["Data Analysts", "AI Engineer", "Gen AI Developer", "Full-Stack Dev", "Data Scientist"]
profile = st.sidebar.multiselect("Select Job Profile", options=profile_op)

# =====================================================================
# 4. MAIN PAGE INPUT FIELDS
# =====================================================================
st.markdown("### 📝 GET USER INFO")
user_info = st.text_area("Write your Resume Description:")

# =====================================================================
# 5. CORE AGENT TOOLS & FUNCTIONS
# =====================================================================
def search_latest_news_jobs(query):
    """Fetches real-time web results via Tavily using the sidebar credentials."""
    client = TavilyClient(api_key=TAVILY_API_KEY)
    response = client.search(query)
    return response


def main_agent(agent_instance, query):
    """Generates structural professional resume layout matching user bio description."""
    prompt = """You are an expert AI Resume Generator assistant.
    Your task is to take the user data provided and generate a detailed professional resume.
    It must feature a modern, dynamic UI/UX design with professional embedded CSS styling.
    Make sure to give your output strictly as a raw HTML block. 
    Do NOT wrap the output in markdown code blocks like ```html ... ```. Output ONLY valid HTML markup.
    """

    user_details = f"\n\nUser details:\n{query if query else 'Default Resume: Python Developer'}"
    final_prompt = prompt + user_details

    response = agent_instance.invoke({'messages': [{'role': 'user', 'content': final_prompt}]})
    
    # Extract string directly from AIMessage content block to fix indexing errors
    code = response['messages'][-1].content
    return code


def get_jobs(agent_instance, locations_list, profiles_list):
    """Fetches active jobs filtering context dynamically via user selection parameters."""
    # Build clean string labels out of user multiselect arrays
    loc_str = ", ".join(locations_list) if locations_list else "Major Tech Hubs (Delhi, Mumbai, Bangalore)"
    prof_str = ", ".join(profiles_list) if profiles_list else "Data Analyst / Software Developer"

    prompt = f"""Based on the user criteria, search real-time for active job openings.
    Target Locations: {loc_str}
    Target Profiles: {prof_str}
    
    Search popular platforms like Naukri, LinkedIn, and Indeed. 
    Extract: JOB PROFILE NAME, LOCATION, SALARY, COMPANY NAME, and the DIRECT APPLY LINK.
    Format your complete response into professional HTML Naukri-themed job cards with clean CSS margins.
    Do NOT wrap the output in markdown code blocks like ```html ... ```. Output ONLY valid HTML markup.
    """

    response = agent_instance.invoke({'messages': [{'role': 'user', 'content': prompt}]})
    code = response['messages'][-1].content
    return code

# =====================================================================
# 6. RUNTIME ORCHESTRATION & TRIGGER VALIDATION
# =====================================================================
if st.button("Generate Resume"):
    # Guardrail check to verify keys are filled and prevent st.stop() breaking the spinner
    if not all([TAVILY_API_KEY, GROQ_API_KEY, GOOGLE_API_KEY]):
        st.sidebar.error("❌ Please provide all required API Keys in the sidebar first!")
    elif not user_info.strip():
        st.warning("⚠️ Please provide profile details in the text area before processing.")
    else:
        # Spinner initiates smoothly now because requirements are verified first
        with st.spinner("⏳ Agent Running... Initializing environments and processing data..."):
            try:
                # Setup model and environment dependencies directly inside button event loop
                os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY
                
                runtime_model = ChatGoogleGenerativeAI(
                    model='gemini-3.5-flash-lite', # Using tool-stable model
                    google_api_key=GOOGLE_API_KEY
                )
                
                # Create runtime graph instances safely
                runtime_agent = create_agent(
                    model=runtime_model,
                    tools=[search_latest_news_jobs]
                )
                
                # 1. Process Resume Block
                st.markdown("### 📄 Your Generated Resume")
                resume_html = main_agent(runtime_agent, user_info)
                st.html(resume_html, width="stretch", unsafe_allow_javascript=True)
                
                st.divider()  # Aesthetic layout break
                
                # 2. Process Job Matching Cards Block
                st.markdown("### 💼 Matching Live Job Opportunities")
                job_html = get_jobs(runtime_agent, location, profile)
                st.html(job_html, width="stretch", unsafe_allow_javascript=True)
                
            except Exception as e:
                st.error(f"An unexpected agent error occurred: {e}")


