from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
# Add CORS support with specific options
CORS(app, resources={
    r"/api/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

messages = []

@app.route('/api/messages', methods=['GET', 'POST', 'OPTIONS'])  # Add OPTIONS
def handle_messages():
    # Handle OPTIONS request explicitly
    if request.method == 'OPTIONS':
        return jsonify({}), 200

    if request.method == 'GET':
        return jsonify(messages)

    if request.method == 'POST':
        data = request.get_json()
        message = {
            'id': len(messages),
            'text': data.get('text', ''),
            'sender': data.get('sender', 'Anonymous'),
            'timestamp': datetime.now().strftime('%H:%M:%S')
        }
        messages.append(message)
        return jsonify(message)

# Add a test route to verify server is running
@app.route('/')
def home():
    return "Server is running!"

if __name__ == '__main__':
    app.run(debug=True)