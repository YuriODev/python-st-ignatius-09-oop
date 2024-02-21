# Football Officials Management System

## Code

```python
class OfficialsManagement:
    total_officials = 0
    officials_roles = {}

    def __init__(self, name: str, role: str, experience_years: int) -> None:
        self.name = name
        self.role = role
        self.experience_years = experience_years
        OfficialsManagement.total_officials += 1
        if role in OfficialsManagement.officials_roles:
            OfficialsManagement.officials_roles[role].append(name)
        else:
            OfficialsManagement.officials_roles[role] = [name]

    def print_official_details(self) -> None:
        """Print the details of the official"""
      
        print(f"{self.name}, a {self.role}, has {self.experience_years} years of experience.")


# Example usage
# Creating instances of OfficialsManagement
mark_clattenburg = OfficialsManagement("Mark Clattenburg", "Referee", 13)
howard_webb = OfficialsManagement("Howard Webb", "Referee", 15)
mike_dean = OfficialsManagement("Mike Dean", "Fourth Official", 10)

# Displaying information about the officials
mark_clattenburg.print_official_details()
howard_webb.print_official_details()
mike_dean.print_official_details()

print(OfficialsManagement.total_officials)  # Output: 3
print(OfficialsManagement.officials_roles)  # Output: {'Referee': ['Mark Clattenburg', 'Howard Webb'], 'Fourth Official': ['Mike Dean']}
```



This Python class, `OfficialsManagement`, is designed for managing football officials, including referees and fourth officials. It demonstrates class-level tracking and categorization of officials by role. Below is a detailed breakdown of its structure and functionality:

## Class Overview

- **Class Variables:**
  - `total_officials`: A class-level counter that tracks the total number of `OfficialsManagement` instances, representing the total number of officials managed by the system. It is an immutable integer that gets incremented with each new official added.
  - `officials_roles`: A dictionary that categorizes officials based on their roles (e.g., Referee, Fourth Official). It maps a role to a list of officials' names, allowing for easy access and management of officials by role.

## Constructor Method: `__init__`

- The constructor method initializes each official instance with `name`, `role`, and `experience_years`.
- It increments the `total_officials` class variable by 1 for each new instance, reflecting the addition of a new official to the system.
- The constructor also updates the `officials_roles` dictionary. If the official's role already exists in the dictionary, their name is appended to the list of names associated with that role. If the role does not exist, a new entry is created with the official's role as the key and a list containing the official's name as the value.

## Instance Method: `print_official_details`

- This method prints the details of an official, including their name, role, and years of experience. It showcases how instance variables can be accessed and used within instance methods to display information about individual officials.

## Example Usage and Outputs

- Three instances of `OfficialsManagement` are created, representing officials Mark Clattenburg, Howard Webb, and Mike Dean, each with their respective roles and years of experience.
- The `print_official_details` method is called for each instance to display the official's details.
- Finally, the `total_officials` and `officials_roles` class variables are printed, demonstrating how the class tracks the total number of officials and organizes them by role.

## Conclusion

The `OfficialsManagement` class exemplifies the use of class and instance variables in Python for managing a collection of objects with shared characteristics (in this case, football officials). It highlights the principles of object-oriented programming applied to a real-world problem, showcasing modularity, encapsulation, and the organization of data.
