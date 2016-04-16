import os
from flask import Flask, request, render_template
from math import exp

app = Flask(__name__)

@app.route('/')
def home():
    return '<form action="/echo" method="POST"><input placeholder="peso(kg)" name="peso"><input placeholder="altura(m)" name="altura"><input type="submit" value="Calcular"></form>'
 
@app.route("/echo", methods=['POST'])
def echo(): 
    return "IMC =  " + str(float(request.form.get('peso', '')))
 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
