import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
st.set_page_config(page_title="AuraStory Agent", page_icon="✨", layout="centered")

st.title("✨ AuraStory: Interactive AI Agent")
st.caption("A Secure & Pedagogical Interactive Storytelling Journey for Children")
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
    1. Write exactly ONE chapter at a time. Keep the narrative engaging but concise (around 2-3 paragraphs).
    2. At the absolute end of Chapter 1, you MUST present exactly 3 choices formatted exactly like this:
       [SPLIT]
       * **Option A:** Description
       * **Option B:** Description
       * **Option C:** Description
    3. For Chapter 2 (the FINAL CHAPTER), write a beautiful, happy conclusion and do NOT provide any options.
    """
    st.session_state.chat_session = client.chats.create(
        model="gemini-2.5-flash",
        config={"system_instruction": system_instruction, "temperature": 0.7}
    )
    st.session_state.messages = []
    st.session_state.story_started = False
    st.session_state.ch1_generated = False
    st.session_state.ch2_generated = False

# دالة ذكية لفصل القصة عن الخيارات وعرضها بشكل مرتب
def display_formatted_message(role, text):
    with st.chat_message(role):
        if "[SPLIT]" in text:
            parts = text.split("[SPLIT]")
            st.markdown(parts[0])  # يعرض نص القصة أولاً
            st.info("👇 **What will you do next? Choose one option:**") # فاصل بصري
            st.markdown(parts[1])  # يعرض الخيارات منسقة ومنفصلة بالأسفل
        else:
            st.markdown(text)

# عرض التاريخ المنسق
for message in st.session_state.messages:
    display_formatted_message(message["role"], message["content"])

# --- المرحلة 1: بداية الشابتر الأول ---
if not st.session_state.story_started:
    story_idea = st.text_input("≫ Enter an exciting theme to start your adventure:", placeholder="e.g., A brave little falcon exploring space...")
    if st.button("Start Adventure 🚀") and story_idea:
        st.session_state.story_started = True
        
        with st.spinner("🤖 Agent is crafting Chapter 1..."):
            prompt_ch1 = f"Let's start an adventure based on this theme: {story_idea}. Generate ONLY Chapter 1 now, followed by Option A, B, and C divided by [SPLIT]."
            response = st.session_state.chat_session.send_message(prompt_ch1)
            
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.session_state.ch1_generated = True
        st.rerun()

# --- المرحلة 2: خيار الطفل والشابتر الأخير ---
elif st.session_state.ch1_generated and not st.session_state.ch2_generated:
    if child_choice := st.chat_input("Type your choice (A, B, or C) for the next chapter..."):
        with st.chat_message("user"):
            st.markdown(child_choice)
        st.session_state.messages.append({"role": "user", "content": child_choice})
        
        with st.spinner("🤖 Agent is crafting the final conclusion..."):
            prompt_ch2 = f"The child chose option {child_choice.upper()}. Now, write the final chapter (Chapter 2) as a rich, satisfying, and happy conclusion to the story. Wrap up everything beautifully and do NOT provide any options."
            response = st.session_state.chat_session.send_message(prompt_ch2)
            
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.session_state.ch2_generated = True
        st.rerun()

# --- المرحلة 3: النهاية ---
elif st.session_state.ch2_generated:
    st.success("🎉 Story is fully complete! The narrative has reached its final conclusion.")
    if st.button("Start a New Story 🔄"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()