import unittest
from unittest.mock import patch  # Corrected import for mock.patch
from example_2 import OfficialsManagement  # Adjust this import as necessary


class TestOfficialsManagement(unittest.TestCase):

    def setUp(self):
        """Reset class variables before each test."""
        OfficialsManagement.total_officials = 0
        OfficialsManagement.officials_roles = {}

    def test_total_officials_count(self):
        """Test that the total officials count increments correctly."""
        OfficialsManagement("Mark Clattenburg", "Referee", 13)
        OfficialsManagement("Howard Webb", "Referee", 15)
        OfficialsManagement("Mike Dean", "Fourth Official", 10)
        self.assertEqual(OfficialsManagement.total_officials, 3)

    def test_officials_roles_updates_correctly(self):
        """Test that officials roles are updated correctly."""
        OfficialsManagement("Mark Clattenburg", "Referee", 13)
        OfficialsManagement("Howard Webb", "Referee", 15)
        OfficialsManagement("Mike Dean", "Fourth Official", 10)
        expected_roles = {
            'Referee': ['Mark Clattenburg', 'Howard Webb'],
            'Fourth Official': ['Mike Dean']
        }
        self.assertEqual(OfficialsManagement.officials_roles, expected_roles)

    def test_print_official_details(self):
        """Test that official details are printed as expected."""
        official = OfficialsManagement("Mark Clattenburg", "Referee", 13)
        with unittest.mock.patch('builtins.print') as mocked_print:
            official.print_official_details()
            mocked_print.assert_called_with("Mark Clattenburg, a Referee, has 13 years of experience.")


if __name__ == '__main__':
    unittest.main()
