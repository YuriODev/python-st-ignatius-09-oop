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
