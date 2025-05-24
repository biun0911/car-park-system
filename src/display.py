class Display:
    def __init__(self, id, car_park, message="", is_on=False):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    def __string__(self):
        return f"Display {self.id}: {self.message}."

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
        if data.get("message") is not None:
            self.message = data["message"]
        if data.get("is_on") is not None:
            self.is_on = data["is_on"]
        if data.get("car_park") is not None:
            self.car_park.update(data["car_park"])