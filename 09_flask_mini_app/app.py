from flask import Flask, jsonify, request
app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(msg="Hello from Flask!")

@app.get("/echo")
def echo():
    return jsonify(q=request.args.get("q",""))

if __name__ == "__main__":
    app.run(debug=True)
