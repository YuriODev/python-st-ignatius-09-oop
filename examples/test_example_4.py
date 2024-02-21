import unittest
from example_4 import HomeEnergyAudit  # Adjust this import as necessary


class TestHomeEnergyAudit(unittest.TestCase):

    def setUp(self):
        """Reset class variables before each test."""
        HomeEnergyAudit.total_audits = 0
        HomeEnergyAudit.recommendations_list = ["Insulate the attic", "Upgrade to energy-efficient appliances"]

    def test_total_audits_increment(self):
        """Test that the total audits count increments correctly."""
        HomeEnergyAudit("John Doe", "123 Elm St", "2022-09-15", {"Heating": 200, "Cooling": 150})
        HomeEnergyAudit("Jane Smith", "456 Oak St", "2022-10-01", {"Heating": 300, "Cooling": 120})
        self.assertEqual(HomeEnergyAudit.total_audits, 2)

    def test_add_recommendation_updates_lists_correctly(self):
        """Test that recommendations are added correctly to the specific and general lists."""
        audit = HomeEnergyAudit("Emily White", "789 Pine St", "2022-11-20", {"Heating": 250, "Cooling": 130})
        audit.add_recommendation("Upgrade to energy-efficient HVAC system")

        self.assertIn("Upgrade to energy-efficient HVAC system", audit.specific_recommendations)
        self.assertIn("Upgrade to energy-efficient HVAC system", HomeEnergyAudit.recommendations_list)

    def test_recommendations_list_initial_state(self):
        """Test the initial state of the recommendations list."""
        self.assertEqual(HomeEnergyAudit.recommendations_list, ["Insulate the attic", "Upgrade to energy-efficient appliances"])


if __name__ == '__main__':
    unittest.main()
