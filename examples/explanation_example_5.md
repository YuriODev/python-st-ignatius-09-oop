# Football Tournament Organization

## Code

```python
class FootballTournament:
    tournament_count = 0
    all_teams = []

    def __init__(self, name: str, location: str, year: int) -> None:
        self.name = name
        self.location = location
        self.year = year
        self.winner = None
        self.participating_teams = []
        FootballTournament.tournament_count += 1

    def add_team(self, team_name: str) -> None:
        """Add a team to the tournament

        Args:
        team_name (str): Name of the team

        """

        if team_name not in self.participating_teams:
            self.participating_teams.append(team_name)

        if team_name not in FootballTournament.all_teams:
            FootballTournament.all_teams.append(team_name)
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
```

The `FootballTournament` class encapsulates the concept of a football tournament, including its name, location, year, participating teams, and the tournament winner. This class demonstrates key OOP principles, such as encapsulation and the use of class and instance variables.

## Class Overview

- **Class Variables:**
  - `tournament_count`: An immutable class variable that tracks the total number of `FootballTournament` instances created. It's used to count the tournaments.
  - `all_teams`: A mutable class variable that stores a list of all teams ever added to any tournament. This demonstrates how data can be shared among all instances of a class.

## Constructor Method: `__init__`

- Initializes a new instance of the `FootballTournament` class with the tournament's name, location, and year. It also initializes `winner` to `None` and `participating_teams` to an empty list.

## Instance Methods

- `add_team`: Adds a team to the tournament's list of participating teams if it's not already present. It also updates the class-wide list of all teams.
- `set_winner`: Sets the tournament's winning team.
- `list_participating_teams`: Prints a list of teams participating in the tournament.
- `__repr__`: Provides a formatted string representation of the `FootballTournament` object, including its name, year, location, participating teams, and the winner.

## Example Usage

- The example creates instances of the `FootballTournament` class for different tournaments: UEFA Champions League, FIFA World Cup, and Copa America.
- Teams are added to each tournament using the `add_team` method, and the winner is set with `set_winner`.
- The `list_participating_teams` method displays the teams participating in each tournament.
- Finally, the `__repr__` method is used to print detailed information about each tournament, including the participating teams and the winner.

## Observations

- **Mutable vs Immutable Class Variables:** The class demonstrates the impact of mutable (`all_teams`) and immutable (`tournament_count`) class variables on all instances.
- **Instance Variables vs Class Variables:** The distinction between instance-specific data (`participating_teams`, `winner`) and data shared across all instances (`tournament_count`, `all_teams`) is showcased.
- **Encapsulation:** The class methods encapsulate the logic for managing tournaments, such as adding teams and setting winners, ensuring that the internal state is modified in a controlled manner.

This class provides a robust template for managing football tournaments, showcasing practical applications of OOP concepts in Python.
