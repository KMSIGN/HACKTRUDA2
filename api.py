import backend
import flask
from flask import request
import json

app = flask.app.Flask('app')


@app.route('/answer')
def answer():
    data = request.get_json(force=False)
    if data['position'] in parser.models:
        questions = parser.models[data['position']].values()
        answer = parser.answer_questions(data['uid'], questions)
        return str(json.dumps(answer))


if __name__ == '__main__': 
    parser = backend.HHParser()
    print(parser.models.keys())
    app.run(port=3213, debug=True)