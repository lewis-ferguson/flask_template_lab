from datetime import date

class Event():
    def __init__(self, name, room_location, description):
        self.name= name
        self.date = date.today()
        self.guests = []
        self.room_location = room_location
        self.description = description
    
    def num_of_guests(self):
        return len(self.guests)    