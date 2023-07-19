from models.event import Event
from datetime import date

event1 =Event("Music Festival",  1, "Ed-Sheeran Live music", False)
event2 = Event("Karting", 4, "Petrol Go-karts", True)


events = [event1, event2]


def add_new_event(event):
    events.append(event)
    
def add_guests(event, num):
    event.guests += int(num)
    
