from flask import render_template, Blueprint, request
from models.events_list import events, add_new_event
from models.event import Event
from datetime import date

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title ='Events List', events= events)


@events_blueprint.route('/events', methods =["POST"])
def add_event():
    event_name = request.form['name']
    event_room_location = request.form['room_location']
    event_description = request.form['description']
    new_event = Event(event_name, event_room_location, event_description)
    add_new_event(new_event)
    return render_template('index.jinja', title='Events List', events = events)