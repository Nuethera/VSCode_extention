from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/tts', methods=[ 'GET'])
def tts_get():
    prompt = str(request.args.get("text"))
    #text to code here

    return jsonify({"text":prompt,"CODE":"code is being written."})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)