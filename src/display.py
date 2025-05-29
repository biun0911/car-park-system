class Display:
    """
    Display in the car park system
    """
    def __init__(self, id, car_park, message="", is_on=False):
        """
        Initialize the display

        :param id: Unique identifier for the display
        :param car_park: Associated car park instance
        :param message: Message to display, optional
        :param is_on: The display is on or off, optional
        """
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    def __string__(self):
        """
        :return: A string representation of the display message
        """
        return f"Display {self.id}: {self.message}."

    def update(self, data):
        """
        update the display with new data

        :param data: key and value pair to display
        """
        for key, value in data.items():
            print(f"{key}: {value}")
        if data.get("message") is not None:
            self.message = data["message"]
        if data.get("is_on") is not None:
            self.is_on = data["is_on"]
        if data.get("car_park") is not None:
            self.car_park.update(data["car_park"])