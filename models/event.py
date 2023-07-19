from datetime import date

class Event():
    def __init__(self, name, date, room_location, description):
        self.name= name
        self.date = [date]
        self.guests = 0
        self.room_location = room_location
        self.description = description
    
      