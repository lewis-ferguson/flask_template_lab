class Event():
    def __init__(self, date, name, room_location, description):
        self.date = date
        self.name= name
        self.guests = []
        self.room_location = room_location
        self.description = description