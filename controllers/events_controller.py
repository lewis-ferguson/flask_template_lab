from flask import render_template, Blueprint, request
from models.events_list import events
from models.event import Event
from datetime import date

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title ='Events List', events= events)