import csv

class BudgetManager:
    def __init__(self, data_file="events.csv"):
        self.data_file = data_file
        self.headers = ["name", "date_time", "location", "description", "attendees", "budget_venue", "budget_catering", "budget_entertainment", "budget_miscellaneous"]
        self.events = {}
        self.load_data()

    def load_data(self):
        self.events = {}
        try:
            with open(self.data_file, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["attendees"] = eval(row.get("attendees", "[]"))
                    row["budget_venue"] = float(row.get("budget_venue", 0))
                    row["budget_catering"] = float(row.get("budget_catering", 0))
                    row["budget_entertainment"] = float(row.get("budget_entertainment", 0))
                    row["budget_miscellaneous"] = float(row.get("budget_miscellaneous", 0))
                    self.events[row["name"]] = row
        except FileNotFoundError:
            print("No events file found. Starting with empty data.")

    def save_data(self):
        with open(self.data_file, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            for event in self.events.values():
                writer.writerow(event)

    def set_budget(self, event_name, venue, catering, entertainment, miscellaneous):
        if event_name not in self.events:
            print(f"Event '{event_name}' not found.")
            return

        self.events[event_name]["budget_venue"] = venue
        self.events[event_name]["budget_catering"] = catering
        self.events[event_name]["budget_entertainment"] = entertainment
        self.events[event_name]["budget_miscellaneous"] = miscellaneous
        self.save_data()
        print(f"Budget for event '{event_name}' updated.")

    def view_budget(self, event_name):
        if event_name not in self.events:
            print(f"Event '{event_name}' not found.")
            return

        event = self.events[event_name]
        print(f"Budget for event '{event_name}':")
        print(f"  Venue: {event['budget_venue']}")
        print(f"  Catering: {event['budget_catering']}")
        print(f"  Entertainment: {event['budget_entertainment']}")
        print(f"  Miscellaneous: {event['budget_miscellaneous']}")
        total_budget = sum([event["budget_venue"], event["budget_catering"], event["budget_entertainment"], event["budget_miscellaneous"]])
        print(f"  Total Budget: {total_budget}")

if __name__ == "__main__":
    budget_manager = BudgetManager()

    while True:
        print("\nBudget Manager")
        print("1. Set Budget")
        print("2. View Budget")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            event_name = input("Event Name: ")
            venue = float(input("Budget for Venue: "))
            catering = float(input("Budget for Catering: "))
            entertainment = float(input("Budget for Entertainment: "))
            miscellaneous = float(input("Budget for Miscellaneous: "))
            budget_manager.set_budget(event_name, venue, catering, entertainment, miscellaneous)

        elif choice == "2":
            event_name = input("Event Name: ")
            budget_manager.view_budget(event_name)

        elif choice == "3":
            print("Exiting Budget Manager.")
            break

        else:
            print("Invalid choice. Please try again.")
