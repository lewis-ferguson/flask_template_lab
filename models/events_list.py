from models.event import Event
from datetime import date

event1 =Event("Music Festival", [date.today(), date.today()], 1, "Ed-Sheeran Live music")
event2 = Event("Karting", date.today(), 4, "Petrol Go-karts")


events = [event1, event2]


def add_new_event(event):
    events.append(event)
    
def add_guests(event, num):
    event.guests += int(num)
    
