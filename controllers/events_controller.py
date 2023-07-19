from flask import render_template, Blueprint, request
from models.events_list import events, add_new_event, add_guests
from models.event import Event
from datetime import date

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title ='Events List', events= events)


@events_blueprint.route('/events', methods =["POST"])
def add_event():
    event_name = request.form['name']
    event_date = request.form['date']
    event_guests = request.form['guests']
    event_room_location = request.form['room_location']
    event_description = request.form['description']
    event_recurring = request.form['recurring']
    new_event = Event(event_name, event_room_location, event_description, event_recurring)
    add_new_event(new_event)
    add_guests(new_event, event_guests)
    new_event.date = event_date
    return render_template('index.jinja', title='Events List', events = events)