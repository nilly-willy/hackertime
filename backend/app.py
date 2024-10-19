from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from groq import Groq


app = Flask(__name__)
CORS(app)

# recipe
recipe = ""
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


# Endpoint to process input from React
@app.route('/api/process_input', methods=['POST'])
def process_input():
    data = request.get_json()
    recipe = data['input']
    print(data)
    #user_input = data['input']

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"""{recipe}""",
        }
    ],
    model="llama3-8b-8192",
    )
    
    print(chat_completion.choices[0].message.content)
    return jsonify({'processed': data})


# Running app
app.run()