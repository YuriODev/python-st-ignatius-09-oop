# Home Energy Audit System

## Code

```python
class HomeEnergyAudit:
    total_audits = 0  # Class variable (immutable)
    recommendations_list = ["Insulate the attic", "Upgrade to energy-efficient appliances"]  # Class variable (mutable)

    def __init__(self, homeowner: str, address: str, audit_date: str, energy_consumption: dict) -> None:
        self.homeowner = homeowner
        self.address = address
        self.audit_date = audit_date
        self.energy_consumption = energy_consumption
        self.specific_recommendations = []
        HomeEnergyAudit.total_audits += 1  # Incrementing the total number of audits

    def add_recommendation(self, recommendation: str) -> None:
        """Add a specific recommendation to the list

        Args:
        recommendation (str): Specific recommendation for the homeowner

        """

        self.specific_recommendations.append(recommendation)
        print(f"Recommendation '{recommendation}' added for {self.homeowner}.")
        HomeEnergyAudit.recommendations_list.append(recommendation)


# Example usage
audit1 = HomeEnergyAudit(homeowner="John Doe",
                         address="123 Elm St",
                         audit_date="2022-09-15",
                         energy_consumption={"Heating": 200, "Cooling": 150})
audit1.add_recommendation(recommendation="Seal windows and doors to reduce drafts")


audit2 = HomeEnergyAudit(homeowner="Jane Smith",
                         address="456 Oak St",
                         audit_date="2022-10-01",
                         energy_consumption={"Heating": 300, "Cooling": 120})
audit2.add_recommendation(recommendation="Install solar panels")

audit3 = HomeEnergyAudit(homeowner="Emily White",
                         address="789 Pine St",
                         audit_date="2022-11-20",
                         energy_consumption={"Heating": 250, "Cooling": 130})
audit3.add_recommendation(recommendation="Upgrade to energy-efficient HVAC system")

print("Total Number of Audits:", HomeEnergyAudit.total_audits)  # 3
print("Recommendations List:", HomeEnergyAudit.recommendations_list)  # ['Insulate the attic', 'Upgrade to energy-efficient appliances']
```

The `HomeEnergyAudit` class is designed to manage home energy audits. It tracks the total number of audits conducted and maintains a list of energy-saving recommendations. This class showcases how class variables can be used alongside instance variables to manage global and individual attributes respectively.
## Class Overview

- **Class Variables:**
  - `total_audits`: A class-level counter that keeps track of the total number of home energy audits conducted. It's an immutable integer that increases with each instantiation of a `HomeEnergyAudit` object.
  - `recommendations_list`: A class-level list that contains general recommendations for energy saving. It is mutable and can be added to with specific recommendations from each audit.

## Constructor Method: `__init__`

- Initializes a `HomeEnergyAudit` instance with homeowner information, audit date, and energy consumption details.
- Increments the `total_audits` class variable to reflect a new audit being conducted.
- Initializes an empty list `specific_recommendations` for storing recommendations specific to this audit.

## Instance Method: `add_recommendation`

- Adds a specific energy-saving recommendation for the homeowner to both the instance's specific recommendations list and the class's general recommendations list.
- Demonstrates how an instance method can modify both instance variables and class variables.
- **Keyword Arguments:** This method uses keyword arguments, enhancing code readability by explicitly naming the recommendation being added.

## Example Usage and Outputs

- Three instances of `HomeEnergyAudit` are created, representing energy audits for different homeowners. Each instance is initialized with the homeowner's details and energy consumption data.
- The `add_recommendation` method is called for each instance, adding a specific energy-saving recommendation based on the audit's findings.
- The total number of audits and the comprehensive list of recommendations, including both general and specific suggestions, are printed, showcasing the class's ability to track and manage audit data globally and individually.

## Conclusion

The `HomeEnergyAudit` class illustrates effective use of class and instance variables in a practical application. It demonstrates how to track global information, such as the total number of audits and a list of general recommendations, while also managing specific data for each audit. The use of keyword arguments further enhances the readability and maintainability of the code, making it a robust solution for managing home energy audits and recommendations.

