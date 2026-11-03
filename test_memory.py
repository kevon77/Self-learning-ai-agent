from memory import memory

print("Saving memory...")

memory.add(
    "I am building a self-learning AI agent using Python and Gemini.",
    user_id="user1"
)

print("Memory saved!")

print("\nSearching memory...")

result = memory.search(
    query="What project am I building?",
    filters={"user_id": "user1"}
)

print("\nRetrieved memory:")
print(result)