from flask import Flask, Response
import json
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/hello")
def hello():
    return Response(json.dumps({'response':"Hello user"}),status=200,mimetype='application/json')


if __name__ == "__main__":
    app.run(threaded=True, debug=True)