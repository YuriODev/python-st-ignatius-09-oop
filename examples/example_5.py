class FootballTournament:
    # Class variables
    tournament_count = 0  # Immutable class variable (though integers are immutable, the count can be updated)
    all_teams = []  # Mutable class variable

    def __init__(self, name: str, location: str, year: int) -> None:
        self.name = name
        self.location = location
        self.year = year
        self.winner = None
        self.participating_teams = []  # Mutable instance variable
        FootballTournament.tournament_count += 1  # Incrementing the total number of tournaments

    def add_team(self, team_name: str) -> None:
        """Add a team to the tournament

        Args:
        team_name (str): Name of the team

        """

        if team_name not in self.participating_teams:
            self.participating_teams.append(team_name)  # Adding the team to the list of participating teams

        if team_name not in FootballTournament.all_teams:
            FootballTournament.all_teams.append(team_name)  # Adding the team to the list of all teams
        print(f"Team '{team_name}' added to the tournament.")

    def set_winner(self, winner: str) -> None:
        """Set the winner of the tournament

        Args:
        winner (str): Name of the winning team

        """

        self.winner = winner
        print(f"Winner of the tournament '{self.name}' set to '{winner}'.")

    def list_participating_teams(self) -> None:
        """List all participating teams in the tournament

        """

        print(f"Participating teams in the tournament '{self.name}': {', '.join(self.participating_teams)}.")

    def __repr__(self) -> str:
        """String representation of the FootballTournament object"""

        return f"Tournament '{self.name}' scheduled for {self.year} in {self.location}. Participating teams: {', '.join(self.participating_teams)}. Winner: {self.winner}."


# Example usage
uefa_cl = FootballTournament(name="UEFA Champions League",
                             location="Istanbul",
                             year=2022)

uefa_cl.add_team(team_name="Real Madrid")
uefa_cl.add_team(team_name="Manchester City")
uefa_cl.set_winner(winner="Real Madrid")
uefa_cl.list_participating_teams()
print(uefa_cl)  # Tournament 'UEFA Champions League' scheduled for 2022 in Istanbul. Participating teams: Real Madrid, Manchester City. Winner: Real Madrid.


world_cup = FootballTournament(name="FIFA World Cup",
                               location="Qatar",
                               year=2022)

world_cup.add_team(team_name="Brazil")
world_cup.add_team(team_name="Germany")
world_cup.set_winner(winner="Brazil")
world_cup.list_participating_teams()
print(world_cup)  # Tournament 'FIFA World Cup' scheduled for 2022 in Qatar. Participating teams: Real Madrid, Manchester City, Brazil, Germany. Winner: Brazil.

copa_america = FootballTournament(name="Copa America",
                                  location="Ecuador",
                                  year=2023)

copa_america.add_team(team_name="Argentina")
copa_america.add_team(team_name="Uruguay")
copa_america.set_winner(winner="Argentina")
copa_america.list_participating_teams()
print(copa_america)  # Tournament 'Copa America' scheduled for 2023 in Ecuador. Participating teams: Real Madrid, Manchester City, Brazil, Germany, Argentina, Uruguay. Winner: Argentina.

print("Total Number of Tournaments:", FootballTournament.tournament_count)  # 3
print("All Teams:", FootballTournament.all_teams)  # ['Real Madrid', 'Manchester City', 'Brazil', 'Germany', 'Argentina', 'Uruguay']
