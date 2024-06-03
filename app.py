from flask import Flask

PORT = 5000
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!\n'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=PORT)
