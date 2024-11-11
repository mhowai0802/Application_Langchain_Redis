import json
from langchain.memory import RedisChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_ollama import ChatOllama
import os
from flask import Flask,request, jsonify
from flask_cors import CORS
import logging
from datetime import datetime

app = Flask(__name__)
app.logger.disabled = True
log = logging.getLogger('werkzeug')

log.disabled = True

CORS(app)

# Configure Redis connection
redis_url = "redis://localhost:6379"  # Modify with your Redis connection string
session_id = "chat_session_1"  # Unique identifier for the chat session

llm = ChatOllama(model="mistral",temperature=0)

# Initialize Redis message history
message_history = RedisChatMessageHistory(
    url=redis_url,
    session_id=session_id,
    ttl=600  # Time to live in seconds (optional)
)
# Create memory instance with Redis backend
memory = ConversationBufferMemory(
    chat_memory=message_history,
    return_messages=True
)
# Initialize language model and conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

@app.route('/')
def hello():
    return jsonify('Hello, World!')

@app.route('/save_chat', methods=['POST'])
def save_chat():
    data = request.get_json()
    response = conversation.predict(input=data['text'])
    formatted_message = {
        "id": 1,
        "text": response,
        "sender": "User_hahaha",
        "timestamp": datetime.now().strftime("%H:%M"),
        "type": "user_message"
    }
    return jsonify({
        "success": True,
        "data": formatted_message
    })

if __name__ == '__main__':
    app.run(debug=True)