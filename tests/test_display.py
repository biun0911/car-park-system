import unittest
from display import Display
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    """
    Unit tests for Display
    """
    def setUp(self):
        """
        Set up Display instance
        """
        self.car_park = CarPark("Moondalup Carpark", 100)
        self.display = Display(
            id = 1,
            message = "Welcome to the car park",
            is_on = True,
            car_park= self.car_park
        )


    def test_display_initialized_with_all_attributes(self):
        """
        Test Display is initialized with all attributes.
        """
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        """
        Test update method correctly changes the display message.
        """
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")