```markdown
# AuraStory: Secure & Pedagogical Interactive Child Co-Creation Agent System

An advanced, stateful, and production-grade AI agent system developed for the **2026 Kaggle Capstone Event**. AuraStory utilizes the modern Google AI Agent SDK (`gemini-2.5-flash`), Model Context Protocol (MCP), and Streamlit to co-create tailored, branching interactive stories for children while maintaining strict pedagogical safeguards and local asset persistence.

---

## 🚀 Key Architectural Features

* **Multi-Turn Reactive Chat UI:** Built with Streamlit for a highly responsive, child-friendly visual storytelling layout.
* **Deterministic Guardrails:** Backed by structured prompt logic to enforce strict safety rules, appropriate vocabulary, and exact story pacing.
* **Model Context Protocol (MCP) Integration:** Exposes isolated file system capabilities safely via specialized tools (`save_story_chapter` & `simulate_image_generation`).
* **Clean Separation of Concerns:** Decouples core algorithmic prompts, custom server tools, and interface rendering for high extensibility.

---

## 📁 Repository Layout & Files

* `app.py` - The core application file running the dynamic Streamlit interface and orchestrating the active chat session memory.
* `agent.py` - Terminal-based execution script for direct console testing and raw model validation.
* `mcp_server.py` - The dedicated FastMCP server handling tool schemas and execution contexts.
* `.agents/skills/story-craft/SKILL.md` - Static system instruction blueprints enforcing alignment policies.
* `.gitignore` - Safeguard file preventing internal virtual environments (`venv`) and secure API credentials (`.env`) from going public.

---

## 📦 Production Local Installation

Follow these explicit steps to activate, pull dependencies, and run the infrastructure locally:

### 1. Clone the Repository
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AuraStory-Agent

```

### 2. Configure the Isolated Virtual Environment

```powershell
# Initialize Environment
python -m venv venv

# Bypass Execution Restrictions (Windows Only if required)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activate Virtual Environment
.\venv\Scripts\Activate

```

### 3. Install Framework Dependencies

```powershell
pip install google-genai streamlit python-dotenv mcp

```

### 4. Setup Secure Credentials

Create a `.env` file in the root directory of your project:

```env
GEMINI_API_KEY=your_actual_api_key_here

```

### 5. Execute the Core Interface

To launch the beautiful, child-ready interactive web application:

```powershell
streamlit run app.py

```

---

## 🛠️ Testing the MCP Backend Renders

To thoroughly inspect and validate the tool registration schemas without the UI overhead, use the official Google MCP Inspector:

```powershell
npx @modelcontextprotocol/inspector python mcp_server.py

```

Open `http://localhost:3000` in your browser, and tap **Connect** to visualize tool bindings.

---

## ⚖️ Safety Compliance & Framework Metrics

AuraStory operates on a zero-trust model for narrative progression. The engine caps dynamic storytelling to precise episodic intervals, enforcing mandatory structural branching choices (Option A, B, and C) before reaching a fully realized, non-hallucinated final happy conclusion. All computational execution flows conform strictly to the 2026 Google AI Architecture benchmarks.

```

