# Stadium Management System

## Code

```python
class StadiumManagement:
    stadium_count = 0
    events_schedule = {}

    def __init__(self, name: str, capacity: int, location: str) -> None:
        self.name = name
        self.capacity = capacity
        self.location = location
        self.events = []
        StadiumManagement.stadium_count += 1

    def schedule_event(self, event_name: str, date: str) -> None:
        """Schedule an event at the stadium

        Args:
        event_name (str): Name of the event
        date (str): Date of the event

        """

        self.events.append((event_name, date))
        StadiumManagement.events_schedule[event_name] = date 
        print(f"Event '{event_name}' has been scheduled at {self.name} on {date}.")


# Example usage
anfield = StadiumManagement("Anfield", 54074, "Liverpool")
anfield.schedule_event("Premier League Match", "2022-10-22") # Output: Event 'Premier League Match' scheduled on 2022-10-22 at Anfield.

wembley = StadiumManagement("Wembley", 90000, "London")
wembley.schedule_event("FA Cup Final", "2023-05-14") # Output: Event 'FA Cup Final' scheduled on 2023-05-14 at Wembley.

camp_nou = StadiumManagement("Camp Nou", 99354, "Barcelona")
camp_nou.schedule_event("La Liga Match", "2022-11-20") # Output: Event 'La Liga Match' scheduled on 2022-11-20 at Camp Nou.

print(StadiumManagement.stadium_count)  # Output: 3 
print(StadiumManagement.events_schedule)  # Output: {'Premier League Match': '2022-10-22', 'FA Cup Final': '2023-05-14', 'La Liga Match': '2022-11-20'}

```

This Python class, `StadiumManagement`, is designed to manage stadium events, including scheduling and tracking them. Here's a breakdown of its components and functionality:

## Class Overview

- **Class Variables:**
  - `stadium_count`: A class-level counter tracking the number of `StadiumManagement` instances created. It's an immutable type (int) that gets incremented every time a new stadium instance is created.
  - `events_schedule`: A dictionary that holds the schedule of events across all instances. It's a mutable type and can be updated with new events.

## Constructor Method: `__init__`

- The constructor initializes each stadium instance with `name`, `capacity`, and `location` attributes, and sets up an empty list `events` for instance-specific events.
- It also increments the `stadium_count` class variable by 1 every time a new instance is created.

## Instance Method: `schedule_event`

- This method takes an event's `name` and `date` as parameters and adds the event to both the instance's `events` list and the class-wide `events_schedule` dictionary.
- Demonstrates how instance methods can modify both instance and class variables.

## Example Usage

- Creating instances of `StadiumManagement` for "Anfield", "Wembley", and "Camp Nou" stadiums.
- Scheduling different events for each stadium instance.
- Outputs demonstrate how class and instance variables are updated.

## Outputs Explained

- `print(StadiumManagement.stadium_count)` displays the total number of stadium instances created.
- `print(StadiumManagement.events_schedule)` shows the consolidated schedule of events across all instances.

This example highlights the use of class and instance variables, the process of scheduling events, and how data is shared and managed within a class and its instances.
