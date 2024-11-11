from langchain.memory import RedisChatMessageHistory

# Connect to Redis
message_history = RedisChatMessageHistory(
    url="redis://localhost:6379",
    session_id="chat_session_1"
)

# Retrieve messages
messages = message_history.messages
for message in messages:
    print(f"Role: {message.type}")
    print(f"Content: {message.content}\n")