class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or [] # uses the first value if not None, otherwise uses the second value
        self.sensors = sensors or []
        self.displays = displays or []

        def __string__(self):
            return f"Car Park at {self.location}, with {self.capacity} bays."
