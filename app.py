import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

load_dotenv()

st.set_page_config(page_title="AuraStory - AI Interactive Storytelling", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #1a103c 50%, #2d124d 100%) !important;
        color: #f1f5f9 !important;
    }
    
    
    h1 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #ffffff !important;
        text-shadow: 0 0 10px #a855f7, 0 0 20px #6366f1;
        text-align: center;
        font-size: 3.2rem !important;
        font-weight: 800;
    }
    
    .stChatMessage, .stChatMessage p, .stChatMessage span, div[data-testid="stMarkdownContainer"] p {
        color: #ffffff !important;
        font-size: 1.3rem !important;
        line-height: 1.8 !important;
        font-weight: 400 !important;
    }
    
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.06) !important;
        border: 1px solid rgba(168, 85, 247, 0.25) !important;
        border-radius: 22px !important;
        padding: 25px !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4) !important;
        margin-bottom: 20px !important;
    }
    
    .stAlert {
        background-color: rgba(99, 102, 241, 0.2) !important;
        border: 1px solid #6366f1 !important;
        border-radius: 15px !important;
    }
    .stAlert p {
        color: #ffffff !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
    }
    
    div[data-testid="stColumn"] {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(168, 85, 247, 0.15) !important;
        border-radius: 20px !important;
        padding: 20px !important;
        text-align: center;
        transition: all 0.3s ease-in-out !important;
    }
    div[data-testid="stColumn"]:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 8px 25px rgba(168, 85, 247, 0.4) !important;
    }
    
    div.stButton > button {
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 14px 28px !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        display: block !important;
        white-space: normal !important;
        height: auto !important;
    }
    
    div.stButton > button:hover {
        transform: scale(1.02) !important;
        box-shadow: 0 6px 22px rgba(168, 85, 247, 0.6) !important;
        color: #ffffff !important;
        border: none !important;
    }

    div.stButton > button[key*="opt_a"] { background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%) !important; }
    div.stButton > button[key*="opt_b"] { background: linear-gradient(135deg, #4c1d95 0%, #8b5cf6 100%) !important; }
    div.stButton > button[key*="opt_c"] { background: linear-gradient(135deg, #831843 0%, #ec4899 100%) !important; }
    
    .stTextInput > div > div > input {
        background-color: #ffffff !important;
        color: #0b0f19 !important;
        border: 2px solid rgba(168, 85, 247, 0.4) !important;
        border-radius: 15px !important;
        padding: 14px !important;
        font-size: 1.2rem !important;
        font-weight: 500 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.write("<h1>🔮 AuraStory</h1>", unsafe_allow_html=True)
st.caption("✨ AI-POWERED STORIES. ENDLESS IMAGINATION. ✨")
st.markdown("---")

if not os.getenv("GEMINI_API_KEY"):
    st.error("🔴 API Key missing! Please configure your .env file.")
    st.stop()

@st.cache_resource
def get_gemini_client():
    return genai.Client()

client = get_gemini_client()

if "chat_session" not in st.session_state:
    system_instruction = """
    You are AuraStory, an expert interactive child education and storytelling AI agent.
    
    CRITICAL RULES:
    1. Write exactly ONE chapter at a time. Keep the narrative highly engaging, magical, and tailored for children (around 2-3 paragraphs).
    2. At the absolute end of Chapter 1, you MUST present exactly 3 exciting choices formatted exactly like this:
       [SPLIT]
       Option A: Description of the first choice
       [SPLIT]
       Option B: Description of the second choice
       [SPLIT]
       Option C: Description of the third choice
    3. For Chapter 2 (the FINAL CHAPTER), write a beautiful, happy, satisfying conclusion and do NOT provide any options.
    """
    st.session_state.chat_session = client.chats.create(
        model="gemini-2.5-flash",
        config={"system_instruction": system_instruction, "temperature": 0.7}
    )
    st.session_state.messages = []
    st.session_state.story_started = False
    st.session_state.ch1_generated = False
    st.session_state.ch2_generated = False
    st.session_state.options = ["Option A: Explore the mysterious path", "Option B: Climb the glowing tree", "Option C: Follow the sparkling river"]
    st.session_state.story_input = ""

def display_formatted_message(role, text):
    with st.chat_message(role):
        if "[SPLIT]" in text:
            parts = text.split("[SPLIT]")
            st.markdown(parts[0])  
            
            extracted_opts = [p.strip("* \n") for p in parts[1:] if p.strip()]
            if not st.session_state.ch2_generated and len(extracted_opts) >= 3:
                st.session_state.options = extracted_opts[:3]
        else:
            st.markdown(text)

for message in st.session_state.messages:
    display_formatted_message(message["role"], message["content"])

if not st.session_state.story_started:
    st.markdown("### 🌌 Create New Story")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("🪐 **Space Adventure**")
        st.write("<small style='color:#cbd5e1;'>A brave little falcon exploring the stars.</small>", unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)
        if st.button("Choose Space 🚀", key="btn_space"):
            st.session_state.story_input = "A brave little falcon exploring the stars and discovering a planet made of candy."
            st.rerun()  
            
    with col2:
        st.markdown("🦄 **Fantasy World**")
        st.write("<small style='color:#cbd5e1;'>A friendly dragon looking for a hidden castle.</small>", unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)
        if st.button("Choose Fantasy 🔮", key="btn_fantasy"):
            st.session_state.story_input = "A friendly baby dragon looking for a hidden magical castle in the clouds."
            st.rerun()
            
    with col3:
        st.markdown("🦁 **Animal Kingdom**")
        st.write("<small style='color:#cbd5e1;'>A clever squirrel solving mysteries in the forest.</small>", unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)
        if st.button("Choose Forest 🌳", key="btn_forest"):
            st.session_state.story_input = "A clever detective squirrel solving mysteries and finding lost acorns in the glowing forest."
            st.rerun()

    st.write("<br>", unsafe_allow_html=True)
    
    story_idea = st.text_input(
        "≫ What kind of story shall we create today?", 
        value=st.session_state.story_input,
        placeholder="Type your magical idea here or click a theme above..."
    )
    
    if st.button("Create Magical Story ✨🚀", key="btn_submit_story") and story_idea:
        with st.spinner("🧙‍♂️ Magic Wand is crafting Chapter 1..."):
            try:
                prompt_ch1 = f"Let's start an adventure based on this theme: {story_idea}. Generate Chapter 1, then write [SPLIT] followed by Option A, then [SPLIT] followed by Option B, then [SPLIT] followed by Option C."
                response = st.session_state.chat_session.send_message(prompt_ch1)
                
                st.session_state.story_started = True
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                st.session_state.ch1_generated = True
                st.rerun()
            except APIError as e:
                st.error("⚠️ **The Magic Wand is currently resting due to high demand!** Please wait a few seconds and click again. ✨")

elif st.session_state.ch1_generated and not st.session_state.ch2_generated:
    st.write("<br><h3>🌟 Make Your Choice, Little Adventurer:</h3>", unsafe_allow_html=True)
    st.info("👇 **Click on the path description below that you want to follow:**")
    
    child_choice = None
    
    if st.button(f"🪐 {st.session_state.options[0]}", key="opt_a"):
        child_choice = "A"
    if st.button(f"🔮 {st.session_state.options[1]}", key="opt_b"):
        child_choice = "B"
    if st.button(f"🌳 {st.session_state.options[2]}", key="opt_c"):
        child_choice = "C"
            
    if child_choice:
        with st.spinner("🔮 Gathering star dust for the happy ending..."):
            try:
                prompt_ch2 = f"The child chose option {child_choice}. Now, write the final chapter (Chapter 2) as a rich, satisfying, and happy conclusion to the story. Wrap up everything beautifully and do NOT provide any options."
                response = st.session_state.chat_session.send_message(prompt_ch2)
                
                st.session_state.messages.append({"role": "user", "content": f"I choose Option {child_choice}!"})
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                st.session_state.ch2_generated = True
                st.rerun()
            except APIError as e:
                st.error("⚠️ **The Magic Stars are a bit crowded right now!** Please click your choice button again. 🌟")

elif st.session_state.ch2_generated:
    st.write("<br>", unsafe_allow_html=True)
    st.balloons()
    st.success("🎉 The narrative has reached its final happy conclusion! You are a wonderful storyteller.")
    
    if st.button("Create Another Story 🔄", key="btn_restart"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()