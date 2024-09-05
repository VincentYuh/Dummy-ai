from flask import Flask, render_template_string
from dummyAi import generate_ai_response
import socket
from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
    try:
        ai_output = generate_ai_response()

        return render_template('index.html', ai_output=ai_output)

    except:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)