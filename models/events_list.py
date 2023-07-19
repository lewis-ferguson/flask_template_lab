from models.event import Event

event1 =Event("Music Festival", 1, "Ed-Sheeran Live music")
event2 = Event("Karting", 4, "Petrol Go-karts")

events = [event1, event2]

def add_new_event(event):
    events.append(event)
    
def add_guests(event, num):
    event.guests += int(num) 