import os
import asyncio
from dotenv import load_dotenv
from google import genai

load_dotenv()

if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("🔴 Error: GEMINI_API_KEY not found in .env file.")

client = genai.Client()

# Tools definitions
def save_story_chapter(title: str, chapter_num: int, content: str) -> str:
    """Saves the text content of a generated story chapter locally."""
    return f"🟢 Success: Chapter {chapter_num} saved."

def simulate_image_generation(scene_description: str) -> str:
    """Simulates secure generation of a visual scene asset for the story book."""
    print(f" '{scene_description}'")
    return "🟢 Success: Image rendered."

async def run_story_agent():
    print("\n==================================================")
    print("✨ Welcome to AuraStory: The Interactive Child Agent ✨")
    print("==================================================\n")
    
    story_idea = input("≫ Enter a theme or idea for your story: ")
    if not story_idea:
        story_idea = "A brave little falcon exploring space"

    print(f"\n🚀 Initiating AuraStory core engine for theme: '{story_idea}'...\n")

    system_instruction = """
    You are AuraStory, an expert interactive child education and storytelling AI agent.
    
    CRITICAL RULES:
    1. Write in a rich, descriptive, and beautifully detailed storybook style. Do NOT write short summaries.
    2. Write EXACTLY one chapter at a time. Never combine chapters.
    3. At the absolute end of Chapter 1, you MUST stop and present exactly 3 clear choices formatted as:
       Option A: [Description]
       Option B: [Description]
       Option C: [Description]
    4. Call both tools (`save_story_chapter` and `simulate_image_generation`) for each chapter you generate.
    """

    model_id = "gemini-2.5-flash"
    
    # إعداد الجلسة مع تثبيت الـ Temperature المبدع
    chat = client.chats.create(
        model=model_id,
        config={
            "system_instruction": system_instruction,
            "tools": [save_story_chapter, simulate_image_generation],
            "temperature": 0.8  # إعادة الإبداع والتفصيل
        }
    )

    # --- الشابتر 1 ---
    print("🤖 Agent is crafting Chapter 1...\n")
    prompt_ch1 = f"Let's start a beautifully detailed adventure based on this theme: {story_idea}. Generate ONLY Chapter 1 now, followed by Option A, B, and C."
    response_ch1 = chat.send_message(prompt_ch1)
    
    print("--------------------------------------------------")
    print(response_ch1.text)
    print("--------------------------------------------------\n")

    # انتظار خيار الطفل بشكل إجباري
    child_choice = input("≫ Type your choice for the next chapter (A, B, or C): ")
    
    # --- الشابتر 2 (الخاتمة) ---
    print(f"\n🤖 Agent is crafting the final conclusion based on Option {child_choice.upper()}...\n")
    prompt_ch2 = f"The child chose option {child_choice.upper()}. Now, write the final chapter (Chapter 2) as a rich, satisfying, and happy conclusion to the story. Wrap up everything beautifully and do NOT provide any options at the end."
    response_ch2 = chat.send_message(prompt_ch2)
    
    print("--------------------------------------------------")
    print(response_ch2.text)
    print("--------------------------------------------------\n")

    print("🎉 Story is fully complete! The narrative has reached its final conclusion.")

if __name__ == "__main__":
    asyncio.run(run_story_agent())