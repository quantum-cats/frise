from flask import Flask, url_for, render_template, jsonify, request

import events as ev

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route("/events")
@app.route("/events/<date>")
def events_api(date=None):
    events = ev.get_all_events()

    if date:
        events = [event for event in events if event.date == date]

    author = request.args.get('author')
    if author:
        events = [event for event in events if author in event.author]

    return jsonify([event.to_json() for event in events])


if __name__ == "__main__":
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('events_api'))
        print(url_for('events_api', date='01-03-1990'))
