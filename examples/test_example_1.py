import unittest
from example_1 import StadiumManagement 


class TestStadiumManagement(unittest.TestCase):

    def setUp(self):
        """Reset class variables before each test."""
        StadiumManagement.stadium_count = 0
        StadiumManagement.events_schedule = {}

    def test_stadium_count_increments_correctly(self):
        """Test that the stadium count increments as expected."""
        StadiumManagement("Anfield", 54074, "Liverpool")
        StadiumManagement("Wembley", 90000, "London")
        StadiumManagement("Camp Nou", 99354, "Barcelona")
        self.assertEqual(StadiumManagement.stadium_count, 3)

    def test_events_schedule_updates_correctly(self):
        """Test that the events schedule updates correctly."""
        anfield = StadiumManagement("Anfield", 54074, "Liverpool")
        anfield.schedule_event("Premier League Match", "2022-10-22")
        
        wembley = StadiumManagement("Wembley", 90000, "London")
        wembley.schedule_event("FA Cup Final", "2023-05-14")
        
        self.assertEqual(StadiumManagement.events_schedule, {
            "Premier League Match": "2022-10-22",
            "FA Cup Final": "2023-05-14"
        })

    def test_individual_stadium_events_list(self):
        """Test that individual stadium's events list updates correctly."""
        anfield = StadiumManagement("Anfield", 54074, "Liverpool")
        anfield.schedule_event("Premier League Match", "2022-10-22")
        self.assertIn(("Premier League Match", "2022-10-22"), anfield.events)

if __name__ == '__main__':
    unittest.main()
