import flask
from flask import request
import json

app = flask.Flask('trud_api')
models = {}


@app.route('/models', methods=['GET'])
def models():
    return str(json.dumps(models))


@app.route('/complete_questions', methods=['GET'])
def complete_questions():
    content = request.get_json(force=True)
    return content['name']


if __name__ == "__main__":
    with open('models.json', 'rb') as file:
        models = dict(json.load(file))
    app.run(port=3123)
