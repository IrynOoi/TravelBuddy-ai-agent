# Travel Buddy Agent (Vertex AI + ADK)

## 1) Configure the Agent in Agent Designer (UI)

After completing the UI configuration for:
- AI Agent setup
- Data Store connection

You may encounter a **Preview error** due to a current backend issue.

---

## 2) Agent Designer Preview Issue (Thought Signature API Bug)

Currently, the Agent Designer preview is not functioning properly due to a recent update in Google’s Gemini API (versions 2.5 and 3.0). These models now require an additional backend parameter called `thought_signature` when operating in an agent or tool-calling environment.

However, the visual Agent Designer UI has not yet been fully updated to include this required parameter in its backend requests. As a result, even if all tools and routing are removed from the canvas, the system still sends the request as an agent-formatted payload.

When the Gemini 2.5/3.0 model receives this incomplete payload (missing the required `thought_signature` or containing an unsupported empty tool configuration), it rejects the request and returns a **400 Invalid Argument** error.

---

## 3) Local Setup Using ADK

After completing the UI configuration, run the following commands locally:

### Step 1: Authenticate with Google Cloud
```bash
gcloud auth application-default login
```

---

### Step 2: Create Project Directory
```bash
mkdir vertex-ai-agent
cd vertex-ai-agent
```

---

### Step 3: Create and Activate Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# OR
.venv\Scripts\activate      # Windows
```

---

### Step 4: Install Google ADK
```bash
pip install google-adk
```

---

### Step 5: Create Environment File
```bash
nano .env
```

Add your required environment variables inside `.env`.

---

## 4) Project Structure

Make sure your project structure looks like this:

```
vertex-ai-agent/
├── .venv/
├── .env
└── travel_buddy/
    ├── __init__.py
    └── agent.py   # Paste code from "Get Code" button in UI
```

---

### If Needed: Initialize Module File
```bash
echo 'from .agent import root_agent' > travel_buddy/__init__.py
```

---

## 5) Run the Agent Locally

⚠️ You must be inside the `vertex-ai-agent/` directory before running:

```bash
adk web --port 8080
```

Then open your browser:

```
http://localhost:8080
```

---

## Reference Video
https://youtu.be/rl_7RsE8dWs?si=6EnQw8tzFWC6PywR
