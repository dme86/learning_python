# class Point():
    # def __init__(self, input1, input2):
        # self.x = input1
        # self.y = input2

# p = Point(2, 8)
# print(p.x)
# print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [] # empty list

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3) # start a flight object with capacity = 3

people = ["Dan","Sarah","Caro","Wencke"]    # list of people for a flight
for person in people:                       # go to list, define element as person
    success = flight.add_passenger(person)  # check if person is able to have a seat or capacity of Flight(x) is reached
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")
