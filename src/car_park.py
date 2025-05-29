from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json



class CarPark:
    """
    A car park with a location, capacity, plates, sensors, displays and logging
    """
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None, log_file=Path("log.txt")):
        """
        Initialize the car park

        :param location: Location of the car
        :param capacity: Maximum capacity of the car
        :param plates: list of license plates, optional
        :param sensors: list of sensors, optional
        :param displays: List of displays, optional
        :param log_file: log file path, optional
        """
        self.location = location
        self.capacity = capacity
        self.plates = plates or [] # uses the first value if not None, otherwise uses the second value
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

    def __string__(self):
        """
        :return: A string representation of the car park
        """
        return f"Car Park at {self.location}, with {self.capacity} bays."

    def register(self, component):
        """
        Register a component

        :param component: The component to register (Sensor or Display)
        :raise TypeError: If the component is not a Sensor or Display
        """
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def _log_car_activity(self, plate, action):
        """
        Log the car activity with timestamp to the log file

        :param plate: License plate
        :param action: Action taken (entered or removed)
        """
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def add_car(self, plate):
        """
        Add a car's plate to the car park, update displays and log the entry

        :param plate: License plate for the car entering
        """
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        """
        Remove a car's plate from the car park, update displays and log the removal

        :param plate: License plate for the car exiting
        """
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "removed")

    def write_config(self):
        """
        Save the car park configuration to config.json file
        """
        with open("config.json", "w") as f:
            json.dump({"location": self.location,
                      "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @property
    def available_bays(self):
        """
        Available bays for the car park

        :return: The number of available bays (it won't be less than 0)
        """
        available = self.capacity - len(self.plates)
        return max(0, available)

    def update_displays(self):
        """
        Update the displays of the car park
        """
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        """
        Create a car park instance from a config file (json)

        :param config_file: Path to the config file (json)
        :return: A car park instance
        """
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])