import os
<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, request, render_template
>>>>>>> eb29e3ff9f987d4bb1acb701cea09f0966c229c9

app = Flask(__name__)

@app.route('/')
def home():
    return '<form action="/echo" method="POST"><input name="text"><input type="submit" value="Echo"></form>'
 
@app.route("/echo", methods=['POST'])
def echo(): 
    return "You said: " + request.form['text']
 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
