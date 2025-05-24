class Sensor:
    def __init__(self, id, is_active=True, car_park=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __string__(self):
        status = "Active" if self.is_active else "Inactive"
        return f"Sensor {self.id} is {status}."

class EntrySensor(Sensor):
    pass
class ExitSensor(Sensor):
    pass