import os
from dotenv import load_dotenv
from mem0 import Memory

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env")

config = {
    "llm": {
        "provider": "gemini",
        "config": {
            "model": "gemini-3.5-flash-lite",
            "api_key": api_key,
            "temperature": 0.1,
            "max_tokens": 1000
        }
    },
    "embedder": {
        "provider": "gemini",
        "config": {
            "model": "gemini-embedding-001",
            "api_key": api_key,
            "embedding_dims": 768
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "mem0_gemini",
            "embedding_model_dims": 768,
            "path": "./qdrant_gemini_768"
        }
    }
}

memory = Memory.from_config(config)

print("Mem0 initialized successfully!")