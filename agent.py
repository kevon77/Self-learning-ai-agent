
import os
from dotenv import load_dotenv
from google import genai
from memory import memory

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env")

# Initialize Gemini
client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash-lite"
USER_ID = "user1"


def ask_agent(question, user_id=USER_ID):

    print("\nSearching previous memories...")

    # 1. Retrieve relevant memories
    search_result = memory.search(
        query=question,
        filters={"user_id": user_id}
    )

    memories = [
        item["memory"]
        for item in search_result.get("results", [])
    ]

    memory_context = "\n".join(memories) if memories else "No previous memories found."

    print("Memories retrieved:", len(memories))

    # 2. Build prompt with memory context
    prompt = f"""
You are a helpful self-learning AI agent.

Use the following previous memories when they are relevant.
Do not invent personal information.
If no relevant memory exists, answer normally.

PREVIOUS MEMORIES:
{memory_context}

CURRENT QUESTION:
{question}

Give a clear and helpful answer.
"""

    # 3. Generate response using Gemini
    print("Gemini is thinking...")

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    answer = response.text or "I couldn't generate a response."

    # 4. Save the user's new input as memory
    memory.add(
        question,
        user_id=user_id
    )

    return answer


if __name__ == "__main__":

    print("=" * 45)
    print("       SELF-LEARNING AI AGENT")
    print("=" * 45)

    while True:

        question = input("\nYou: ").strip()

        if question.lower() in ["exit", "quit", "bye"]:
            print("Agent: Goodbye!")
            break

        if not question:
            continue

        try:
            answer = ask_agent(question)
            print("\nAgent:", answer)

        except Exception as error:
            print("\nError:", error)
