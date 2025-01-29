import csv
from datetime import datetime

class ScheduleManager:
    def __init__(self, data_file="events.csv"):
        self.data_file = data_file
        self.headers = ["name", "date_time", "location", "description", "attendees"]
        self.events = []
        self.load_data()

    def load_data(self):
        self.events = []
        try:
            with open(self.data_file, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["attendees"] = eval(row["attendees"])
                    self.events.append(row)
        except FileNotFoundError:
            print("No events file found. Starting with an empty schedule.")

    def display_upcoming_events(self):
        print("Upcoming Events:")
        now = datetime.now()
        upcoming_events = [event for event in self.events if datetime.strptime(event["date_time"], "%Y-%m-%d %H:%M") > now]
        if not upcoming_events:
            print("No upcoming events.")
            return

        for event in sorted(upcoming_events, key=lambda e: datetime.strptime(e["date_time"], "%Y-%m-%d %H:%M")):
            print(f"Event: {event['name']}")
            print(f"  Date & Time: {event['date_time']}")
            print(f"  Location: {event['location']}")
            print(f"  Description: {event['description']}")
            print()

    def filter_events_by_date(self, date):
        print(f"Events on {date}:")
        filtered_events = [event for event in self.events if event["date_time"].startswith(date)]
        if not filtered_events:
            print("No events found for this date.")
            return

        for event in filtered_events:
            print(f"Event: {event['name']}")
            print(f"  Date & Time: {event['date_time']}")
            print(f"  Location: {event['location']}")
            print(f"  Description: {event['description']}")
            print()

    def filter_events_by_location(self, location):
        print(f"Events in {location}:")
        filtered_events = [event for event in self.events if event["location"].lower() == location.lower()]
        if not filtered_events:
            print("No events found for this location.")
            return

        for event in filtered_events:
            print(f"Event: {event['name']}")
            print(f"  Date & Time: {event['date_time']}")
            print(f"  Location: {event['location']}")
            print(f"  Description: {event['description']}")
            print()

if __name__ == "__main__":
    schedule_manager = ScheduleManager()

    while True:
        print("\nSchedule Manager")
        print("1. Display Upcoming Events")
        print("2. Filter Events by Date")
        print("3. Filter Events by Location")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            schedule_manager.display_upcoming_events()

        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            schedule_manager.filter_events_by_date(date)

        elif choice == "3":
            location = input("Enter location: ")
            schedule_manager.filter_events_by_location(location)

        elif choice == "4":
            print("Exiting Schedule Manager.")
            break

        else:
            print("Invalid choice. Please try again.")
 