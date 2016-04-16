import os
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return '<form action="/echo" method="POST"><input name="text"><input type="submit" value="Echo"></form>'
 
@app.route("/echo", methods=['POST'])
def echo(): 
    return "You said: " + request.args.get('text', '')
 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
