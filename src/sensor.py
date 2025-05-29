from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    """
    Abstract class for sensors
    Sensor to detect vehicle and update the car park
    """
    def __init__(self, id, is_active=True, car_park=None):
        """
        Initialize sensor

        :param id: Unique identifier
        :param is_active: The sensor is active or not, optional
        :param car_park: Associated car park instance, optional
        """
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __string__(self):
        """
        :return: A string representation of the sensor status
        """
        status = "Active" if self.is_active else "Inactive"
        return f"Sensor {self.id} is {status}."

    @abstractmethod
    def update_car_park(self, plate):
        """
        Abstract method to update the car park with detected license plate

        :param plate: License plate number
        """
        pass

    def _scan_plate(self):
        """
        Scan a vehicle plate

        :return: A random fake plate string
        """
        return 'FAKE-' + format(random.randint(0,999), "03d")

    def detect_vehicle(self):
        """
        Detect vehicle and update the car park with its plate
        """
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    """
    Sensor to detect vehicles entering the car park
    """
    def update_car_park(self, plate):
        """
        Add the detected vehicle plate to the car park

        :param plate: License plate number for incoming vehicle
        """
        self.car_park.add_car(plate)
        print(f"Incoming vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    """
    Sensor to detect vehicles exiting the car park
    """
    def update_car_park(self, plate):
        """
        Remove the detected vehicle plate from the car park

        :param plate: License plate number for exiting vehicle
        """
        self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        """
        Scan a vehicle plate that is leaving the car park

        :return: A random chosen plate from the car park registered plates
        """
        return random.choice(self.car_park.plates)