class StadiumManagement:
    stadium_count = 0  # Class variable (immutable)
    events_schedule = {}  # Class variable (mutable)

    def __init__(self, name: str, capacity: int, location: str) -> None:
        self.name = name
        self.capacity = capacity
        self.location = location
        self.events = []  # Instance variable (mutable)
        StadiumManagement.stadium_count += 1  # Incrementing the class variable

    def schedule_event(self, event_name: str, date: str) -> None:
        """Schedule an event at the stadium

        Args:
        event_name (str): Name of the event
        date (str): Date of the event

        """

        self.events.append((event_name, date))
        StadiumManagement.events_schedule[event_name] = date  # Updating the class variable
        print(f"Event '{event_name}' has been scheduled at {self.name} on {date}.")


# Example usage
anfield = StadiumManagement("Anfield", 54074, "Liverpool")
anfield.schedule_event("Premier League Match", "2022-10-22")

wembley = StadiumManagement("Wembley", 90000, "London")
wembley.schedule_event("FA Cup Final", "2023-05-14")

camp_nou = StadiumManagement("Camp Nou", 99354, "Barcelona")
camp_nou.schedule_event("La Liga Match", "2022-11-20")

print(StadiumManagement.stadium_count)  # Output: 3 
print(StadiumManagement.events_schedule)  # Output: {'Premier League Match': '2022-10-22', 'FA Cup Final': '2023-05-14', 'La Liga Match': '2022-11-20'}
