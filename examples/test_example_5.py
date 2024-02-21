import unittest
from unittest.mock import patch
from example_5 import FootballTournament  # Adjust this import as necessary


class TestFootballTournament(unittest.TestCase):

    def setUp(self):
        """Reset class variables before each test."""
        FootballTournament.tournament_count = 0
        FootballTournament.all_teams = []

    def test_tournament_count_increment(self):
        """Test that the tournament count increments correctly."""
        FootballTournament("UEFA Champions League", "Istanbul", 2022)
        FootballTournament("FIFA World Cup", "Qatar", 2022)
        self.assertEqual(FootballTournament.tournament_count, 2)

    def test_add_team_updates_correctly(self):
        """Test that teams are added correctly to the tournament and all teams list."""
        uefa_cl = FootballTournament("UEFA Champions League", "Istanbul", 2022)
        uefa_cl.add_team("Real Madrid")
        uefa_cl.add_team("Manchester City")
        self.assertIn("Real Madrid", uefa_cl.participating_teams)
        self.assertIn("Manchester City", FootballTournament.all_teams)

    def test_set_winner(self):
        """Test setting the winner of the tournament."""
        world_cup = FootballTournament("FIFA World Cup", "Qatar", 2022)
        world_cup.set_winner("Brazil")
        self.assertEqual(world_cup.winner, "Brazil")

    def test_repr_output(self):
        """Test the __repr__ method output of the FootballTournament class."""
        copa_america = FootballTournament("Copa America", "Ecuador", 2023)
        copa_america.add_team("Argentina")
        copa_america.set_winner("Argentina")
        expected_repr = "Tournament 'Copa America' scheduled for 2023 in Ecuador. Participating teams: Argentina. Winner: Argentina."
        self.assertEqual(repr(copa_america), expected_repr)

    @patch('builtins.print')
    def test_list_participating_teams(self, mocked_print):
        """Test that participating teams are listed correctly."""
        uefa_cl = FootballTournament("UEFA Champions League", "Istanbul", 2022)
        uefa_cl.add_team("Real Madrid")
        uefa_cl.list_participating_teams()
        mocked_print.assert_called_with("Participating teams in the tournament 'UEFA Champions League': Real Madrid.")


if __name__ == '__main__':
    unittest.main()
