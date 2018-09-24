from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route("/")
def home():
    return 'Welcome to Gaea'

@app.route("/getPrediction", methods=["POST"])
def prediction():
    #json = request.get_json(force = True)
    #data = json['data']
    return jsonify(
        success=True,
        response=str(random.randint(1000000,10000000))
    )

if __name__ == '__main__':
    app.run()