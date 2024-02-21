class OfficialsManagement:
    total_officials = 0  # Class variable (immutable)
    officials_roles = {}  # Class variable (mutable)

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
