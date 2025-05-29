import unittest
from car_park import CarPark
from pathlib import Path

class TestCarPark(unittest.TestCase):
    """
    Unit tests for CarPark class
    """
    def setUp(self):
        """
        Set up CarPark instance
        """
        self.car_park = CarPark("123 Example Street", 100)

    def test_car_park_initialized_with_all_attributes(self):
        """
        Test CarPark is initialized with all attributes
        """
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path("log.txt"))

    def test_add_car(self):
        """
        Test adding car to the car park updates plates and available bays
        """
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        """
        Test removing a car from the car park updates the plates list and restores available bays
        """
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        """
        Test adding more cars than the capacity and removing car after overfilling
        """
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        """
        Test removing a car that does not exist raises a ValueError
        """
        with self.assertRaises(ValueError):
             self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        """
        Test registering an invalid component raises a TypeError
        """
        with self.assertRaises(TypeError):
             self.car_park.register("No a Sensor or Display")

    def test_log_file_created(self):
        """
        Test log file creation when initializing CarPark
        """
        new_carpark = CarPark("123 Example Street", 100, log_file = "new_log.txt")
        self.assertTrue(Path("new_log.txt").exists())

    def tearDown(self):
        """
        Remove files created during the test
        """
        Path("new_log.txt").unlink(missing_ok=True)

    def test_car_logged_when_entering(self):
        """
        Test the car entering is logged correctly
        """
        new_carpark = CarPark("123 Example Street", 100,
                                log_file="new_log.txt")  # TODO: change this to use a class attribute or new instance variable
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("entered", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_car_logged_when_exiting(self):
        """
        Test the car exiting is logged correctly
        """
        new_carpark = CarPark("123 Example Street", 100,
                                log_file="new_log.txt")  # TODO: change this to use a class attribute or new instance variable
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("removed", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

if __name__ == "__main__":
   unittest.main()