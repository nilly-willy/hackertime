from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from groq import Groq


app = Flask(__name__)

# Route for seeing a data
@app.route('/data')
def get_time():

    # Returning an api for showing in  reactjs
    return {
        'Name':"geek", 
        "Age":"22",
        "Date":x, 
        "programming":"python"
        }

    
# Running app
if __name__ == '__main__':
    app.run(debug=True)