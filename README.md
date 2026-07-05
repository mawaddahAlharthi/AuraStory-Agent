# ✨ AuraStory: Next-Gen Interactive AI Storyteller ✨

> **An advanced, secure, and pedagogical AI co-creation agent designed for children.** Built using the modern **Google AI Agent SDK (`gemini-2.5-flash`)**, Model Context Protocol (MCP), and Streamlit for the **2026 Kaggle Capstone Event**.

---

## 🌟 Key Innovations & Magic Features

| Feature | Tech Stack | Pedagogical Impact |
| :--- | :--- | :--- |
| **🎨 Child-Centric Chat UI** | Streamlit | Immersive storybook interface with clean, structured text pacing. |
| **🛡️ Deterministic Guardrails** | System Instructions | Enforces age-appropriate vocabulary with absolute safety metrics. |
| **🧩 Local Asset Tooling** | FastMCP Backend | Secure dynamic context handling using structural tool schemas. |
| **🚀 Multi-Turn Memory** | Streamlit Session State | Persistent narrative continuity across deep branching decisions. |

---

## 📁 Project Architecture & Blueprints

Our repository follows a production-grade, modular structure aligned with Google's framework benchmarks:

&#96;&#96;&#96;text
AuraStory-Agent/
├── 📄 app.py               # Main Orchestrator & Polished Streamlit Chat Interface
├── 📄 agent.py             # Console-based Testing Harness for Raw Model Validation
├── 📄 mcp_server.py        # Dedicated FastMCP Server for File System Safe Tools
├── 📄 README.md            # Highly Visual Developer & Judge Documentation
└── 📂 .agents/
    └── 📂 skills/
        └── 📂 story-craft/
            └── 📄 SKILL.md # System Core Prompts & Fine-Tuned Safety Policies
&#96;&#96;&#96;

---

## 📦 Local Activation & Play Guide

Follow these simplified steps to spinning up the entire infrastructure locally on your machine:

### 1️⃣ Clone & Navigate
&#96;&#96;&#96;bash
git clone https://github.com/mawaddahAlharthi/AuraStory-Agent.git
cd AuraStory-Agent
&#96;&#96;&#96;

### 2️⃣ Environment Setup
&#96;&#96;&#96;powershell
# Initialize virtual system
python -m venv venv

# Bypass security restrictions (Windows Only)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activate the venv
.\venv\Scripts\Activate
&#96;&#96;&#96;

### 3️⃣ Pull Dependencies
&#96;&#96;&#96;powershell
pip install google-genai streamlit python-dotenv mcp
&#96;&#96;&#96;

### 4️⃣ Inject Secure API Key
Create a `.env` file in the root folder and add your key:
&#96;&#96;&#96;env
GEMINI_API_KEY=your_actual_gemini_key_here
&#96;&#96;&#96;

### 5️⃣ Launch the Web Application! 🚀
&#96;&#96;&#96;powershell
streamlit run app.py
&#96;&#96;&#96;

---

## 🛠️ Deep Diagnostics (MCP Inspector)
To thoroughly validate the model's structural tool binding registry without spawning the full user interface:
&#96;&#96;&#96;powershell
npx @modelcontextprotocol/inspector python mcp_server.py
&#96;&#96;&#96;
*Navigate to `http://localhost:3000` inside your browser and tap **Connect** to audit core skill execution logs.*

---

## 🎚️ Model Hyperparameters & Safety Core
* **Core Model:** `gemini-2.5-flash`
* **Temperature:** `0.7` *(Optimized for rich story descriptive narratives while locking out content drift or hallucination rules)*
* **Zero-Trust Boundaries:** Dynamic split token tracking ensures the prompt loops freeze intentionally for child feedback before proceeding to a definitive happy conclusion.
