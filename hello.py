import os
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
	return "<h1>Fill Out This Form</h1><form action='/hello' method='POST'>A Greeting: <input type='text' name='greet'> <br/>Your Name: <input type='text' name='name'><br/><input type='submit'>	</form>	"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
