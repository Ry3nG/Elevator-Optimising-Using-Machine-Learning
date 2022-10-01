# implements a single elevator class
class Elevator:
    def __init__(self, num_floors, elevator_speed, elevator_capacity):
        self.num_floors = num_floors
        self.elevator_speed = elevator_speed
        self.elevator_capacity = elevator_capacity
        self.current_floor = 0
        self.direction = 0
        self.passengers = []
        self.destination = []
        self.time = 0

    def __str__(self):
        return " Current Floor: " + str(self.current_floor) + " Direction: " + str(self.direction) + " Passengers: " + str(self.passengers) + " Destination: " + str(self.destination) + " Time: " + str(self.time)

    def move(self, time):
        self.time = time
        if self.direction == 1:
            self.current_floor += 1
        elif self.direction == -1:
            self.current_floor -= 1
        else:
            self.current_floor = self.current_floor

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)

    def add_destination(self, destination):
        self.destination.append(destination)

    def remove_destination(self, destination):
        self.destination.remove(destination)

    def get_current_floor(self):
        return self.current_floor

    def get_direction(self):
        return self.direction

    def get_passengers(self):
        return self.passengers

    def get_destination(self):
        return self.destination

    def get_time(self):
        return self.time

    def set_current_floor(self, current_floor):
        self.current_floor = current_floor

    def set_direction(self, direction):
        self.direction = direction

    def set_passengers(self, passengers):
        self.passengers = passengers

    def set_destination(self, destination):
        self.destination = destination

    def set_time(self, time):
        self.time = time

    def get_num_floors(self):
        return self.num_floors

    def get_elevator_speed(self):
        return self.elevator_speed

    def get_elevator_capacity(self):
        return self.elevator_capacity

