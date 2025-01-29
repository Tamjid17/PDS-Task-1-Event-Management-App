import csv
import os
from datetime import datetime

class EventManager:
    def __init__(self, data_file="events.csv"):
        self.data_file = data_file
        self.headers = ["name", "date_time", "location", "description", "attendees",
                        "budget_venue", "budget_catering", "budget_entertainment", "budget_miscellaneous"]
        self.load_data()

    def load_data(self):
        self.events = {}
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["attendees"] = eval(row["attendees"])
                    row["budget_venue"] = float(row.get("budget_venue", 0.0))
                    row["budget_catering"] = float(row.get("budget_catering", 0.0))
                    row["budget_entertainment"] = float(row.get("budget_entertainment", 0.0))
                    row["budget_miscellaneous"] = float(row.get("budget_miscellaneous", 0.0))
                    self.events[row["name"]] = row

    def save_data(self):
        with open(self.data_file, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            for event in self.events.values():
                writer.writerow(event)

    def create_event(self, name, date_time, location, description):
        if name in self.events:
            print(f"Event '{name}' already exists.")
            return
        self.events[name] = {
            "name": name,
            "date_time": date_time,
            "location": location,
            "description": description,
            "attendees": [],
            "budget_venue": 0.0,
            "budget_catering": 0.0,
            "budget_entertainment": 0.0,
            "budget_miscellaneous": 0.0,
        }
        self.save_data()
        print(f"Event '{name}' created successfully.")

    def edit_event(self, name, **kwargs):
        if name not in self.events:
            print(f"Event '{name}' not found.")
            return
        for key, value in kwargs.items():
            if key in self.headers and key != "name":
                self.events[name][key] = value
        self.save_data()
        print(f"Event '{name}' updated successfully.")

    def delete_event(self, name):
        if name in self.events:
            del self.events[name]
            self.save_data()
            print(f"Event '{name}' deleted successfully.")
        else:
            print(f"Event '{name}' not found.")

    def view_events(self):
        if not self.events:
            print("No events found.")
            return
        for name, details in self.events.items():
            print(f"Event: {name}")
            print(f"  Date & Time: {details['date_time']}")
            print(f"  Location: {details['location']}")
            print(f"  Description: {details['description']}")
            print(f"  Attendees: {len(details['attendees'])}")
            print()

    def add_attendee(self, event_name, name, email, rsvp_status):
        if event_name not in self.events:
            print(f"Event '{event_name}' not found.")
            return
        attendee = {
            "name": name,
            "email": email,
            "rsvp_status": rsvp_status
        }
        self.events[event_name]["attendees"].append(attendee)
        self.save_data()
        print(f"Attendee '{name}' added to event '{event_name}'.")

    def remove_attendee(self, event_name, email):
        if event_name not in self.events:
            print(f"Event '{event_name}' not found.")
            return
        attendees = self.events[event_name]["attendees"]
        self.events[event_name]["attendees"] = [a for a in attendees if a["email"] != email]
        self.save_data()
        print(f"Attendee with email '{email}' removed from event '{event_name}'.")

    def view_attendees(self, event_name):
        if event_name not in self.events:
            print(f"Event '{event_name}' not found.")
            return
        attendees = self.events[event_name]["attendees"]
        if not attendees:
            print(f"No attendees found for event '{event_name}'.")
            return
        print(f"Attendees for '{event_name}':")
        for attendee in attendees:
            print(f"  Name: {attendee['name']}, Email: {attendee['email']}, RSVP: {attendee['rsvp_status']}")