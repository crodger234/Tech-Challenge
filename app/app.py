from flask import Flask, request
from os import environ
import encryptme

app = Flask(__name__)

@app.route('/encrypt', methods=['GET'])
def encrypt():
    args = request.args
    return encryptme.main(action="encode", text=args.get("text"), shift=5)

@app.route('/decrypt', methods=['GET'])
def decrypt():
    args = request.args
    return encryptme.main(action="decode", text=args.get("text"), shift=5)

@app.route('/')
def hello_world():
    return 'Hello from flask!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=environ.get("FLASK_SERVER_PORT"))