# ✨ AuraStory — Next-Gen Interactive AI Storyteller ✨

> **An advanced, secure, and pedagogical AI co-creation agent designed for children.**
> Built with the **Google AI Agent SDK (`gemini-2.5-flash`)**, the **Model Context Protocol (MCP)**, and **Streamlit** — created for the **2026 Kaggle Capstone Event**.

<p align="center">
  <img src="https://img.shields.io/badge/Model-Gemini%202.5%20Flash-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Protocol-MCP-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/UI-Streamlit-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
</p>

---

## 🌟 Key Innovations & Magic Features

| Feature | Tech Stack | Pedagogical Impact |
| :--- | :--- | :--- |
| 🎨 **Child-Centric Chat UI** | Streamlit | Immersive storybook interface with clean, structured text pacing |
| 🛡️ **Deterministic Guardrails** | System Instructions | Enforces age-appropriate vocabulary with absolute safety metrics |
| 🧩 **Local Asset Tooling** | FastMCP Backend | Secure, dynamic context handling using structured tool schemas |
| 🚀 **Multi-Turn Memory** | Streamlit Session State | Persistent narrative continuity across deep branching decisions |

---

## 📁 Project Architecture & Blueprints

Our repository follows a production-grade, modular structure aligned with Google's framework benchmarks:

```text
AuraStory-Agent/
├── 📄 app.py               # Main Orchestrator & Polished Streamlit Chat Interface
├── 📄 agent.py             # Console-based Testing Harness for Raw Model Validation
├── 📄 mcp_server.py        # Dedicated FastMCP Server for File System Safe Tools
├── 📄 README.md            # Highly Visual Developer & Judge Documentation
└── 📂 .agents/
    └── 📂 skills/
        └── 📂 story-craft/
            └── 📄 SKILL.md  # System Core Prompts & Fine-Tuned Safety Policies
```

---

## 📦 Local Activation & Play Guide

Follow these simplified steps to spin up the entire infrastructure locally on your machine.

### 1️⃣ Clone & Navigate

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AuraStory-Agent
```

### 2️⃣ Environment Setup

```powershell
# Initialize virtual environment
python -m venv venv

# Bypass execution restrictions (Windows only)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activate the virtual environment
.\venv\Scripts\Activate
```

### 3️⃣ Pull Dependencies

```powershell
pip install google-genai streamlit python-dotenv mcp
```

### 4️⃣ Inject Secure API Key

Create a `.env` file in the root folder and add your key:

```env
GEMINI_API_KEY=your_actual_gemini_key_here
```

### 5️⃣ Launch the Web Application 🚀

```powershell
streamlit run app.py
```

---

## 🛠️ Deep Diagnostics (MCP Inspector)

To thoroughly validate the model's structural tool-binding registry without spawning the full user interface:

```powershell
npx @modelcontextprotocol/inspector python mcp_server.py
```

Navigate to `http://localhost:3000` in your browser and click **Connect** to audit core skill execution logs.

---

## 🎚️ Model Hyperparameters & Safety Core

| Parameter | Value | Description |
| :--- | :--- | :--- |
| **Core Model** | `gemini-2.5-flash` | Primary reasoning and generation engine |
| **Temperature** | `0.7` | Optimized for rich, descriptive narratives while locking out content drift or hallucination |
| **Zero-Trust Boundaries** | Enabled | Dynamic split-token tracking ensures prompt loops pause intentionally for child feedback before proceeding to a definitive, happy conclusion |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request.

## 📄 License

This project is released for the 2026 Kaggle Capstone Event. Add your preferred license here (e.g., MIT).
