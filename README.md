# 🤖 Self-Learning AI Agent

A Python-based AI agent that uses **Google Gemini, Mem0, and Qdrant** to remember previous interactions and provide context-aware responses across conversations.

Unlike a basic chatbot that starts every conversation without context, this project uses persistent memory to retrieve relevant information from previous interactions.

## 🚀 Project Overview

The Self-Learning AI Agent combines a Large Language Model (LLM) with a persistent memory system.

It can:
- Answer user questions using Google Gemini.
- Store information from user interactions.
- Retrieve relevant memories from previous conversations.
- Use retrieved memories to generate more personalized and context-aware responses.
- Retain stored memories across application restarts using a local Qdrant database.

**Note:** This project implements memory-based learning. It does not retrain or modify the underlying Gemini model.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Google Gemini | AI response generation |
| Mem0 | Memory extraction, storage and retrieval |
| Qdrant | Vector database for persistent memory |
| Google GenAI SDK | Communication with Gemini API |
| python-dotenv | Secure API key management |
| Streamlit | Planned graphical user interface |

## 🧠 System Architecture

```text
          USER INPUT
               |
               v
       SELF-LEARNING AGENT
               |
               v
       SEARCH PREVIOUS MEMORY
               |
               v
         MEM0 MEMORY
               |
               v
       QDRANT VECTOR DATABASE
               |
               v
       RETRIEVE RELEVANT DATA
               |
               v
       BUILD CONTEXTUAL PROMPT
               |
               v
          GOOGLE GEMINI
               |
               v
        GENERATE RESPONSE
               |
               v
         DISPLAY ANSWER
               |
               v
        STORE NEW MEMORY
               |
               v
       QDRANT DATABASE
```

## 📂 Project Structure

```text
self-learning-ai-agent/
│
├── agent.py             # Main AI agent and conversation loop
├── memory.py            # Mem0 and Qdrant configuration
├── test_memory.py       # Memory save and retrieval testing
├── view_database.py     # Inspect stored Qdrant memories
│
├── requirements.txt     # Python dependencies
├── .env                 # Gemini API key (not uploaded)
├── .gitignore           # Files excluded from Git
│
└── qdrant_gemini_768/   # Local vector database (not uploaded)
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/self-learning-ai-agent.git
```

### 2. Navigate to the project directory

```bash
cd self-learning-ai-agent
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure your Gemini API key

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Get an API key from [Google AI Studio](https://aistudio.google.com/).

**Important:** Never share or upload your API key.

### 6. Run the AI agent

```bash
python agent.py
```

Start chatting with your agent!

To exit:

```text
exit
```

## 💾 Memory Database

This project uses **Qdrant** as its local vector database.

Mem0 manages the memory operations:
1. Receives information from the agent.
2. Processes and stores memories.
3. Converts information into vector embeddings.
4. Retrieves relevant memories when a new question is asked.
5. Supplies retrieved information to Gemini as context.

The database is stored locally in:

```text
qdrant_gemini_768/
```

The database folder is generated automatically when the application runs. It is excluded from GitHub, so a fresh clone starts with an empty local memory database.

## 🧪 Testing

Test memory storage and retrieval:

```bash
python test_memory.py
```

Inspect stored Qdrant records:

```bash
python view_database.py
```

## 🔮 Future Improvements

- Streamlit-based interactive chat interface.
- User feedback system to improve memory quality.
- Memory deduplication and updating.
- Conversation history management.
- Multiple user support.
- Improved memory relevance and retrieval.
- Deployment as a web application.

## 🎯 Project Objective

The objective is to develop an AI agent that can maintain persistent memory, retrieve useful information from previous interactions, and generate context-aware responses.

This project demonstrates the integration of Large Language Models, vector databases, and long-term memory systems in an AI application.

## 👨‍💻 Author

**Raphael Kevon**

GitHub: [kevon77](https://github.com/kevon77)

---

⭐ If you find this project interesting, consider giving the repository a star!
