from schedule_manager import ScheduleManager
from budget_manager import BudgetManager
from event_manager import EventManager

if __name__ == "__main__":
    manager = EventManager()
    schedule_manager = ScheduleManager()
    budget_manager = BudgetManager()
    while True:
        print("\nEvent Manager")
        print("1. Create Event")
        print("2. Edit Event")
        print("3. Delete Event")
        print("4. View Events")
        print("5. Add Attendee")
        print("6. Remove Attendee")
        print("7. View Attendees")
        print("8. Display Upcoming Events")
        print("9. Filter Events by Date")
        print("10. Filter Events by Location")
        print("11. Set Event Budget")
        print("12. View Event Budget")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Event Name: ")
            date_time = input("Date & Time: ")
            location = input("Location: ")
            description = input("Description: ")
            manager.create_event(name, date_time, location, description)

        elif choice == "2":
            name = input("Event Name to Edit: ")
            date_time = input("New Date & Time (leave blank to skip): ")
            location = input("New Location (leave blank to skip): ")
            description = input("New Description (leave blank to skip): ")
            updates = {}
            if date_time: updates["date_time"] = date_time
            if location: updates["location"] = location
            if description: updates["description"] = description
            manager.edit_event(name, **updates)

        elif choice == "3":
            name = input("Event Name to Delete: ")
            manager.delete_event(name)

        elif choice == "4":
            manager.view_events()

        elif choice == "5":
            event_name = input("Event Name: ")
            attendee_name = input("Attendee Name: ")
            email = input("Email: ")
            rsvp_status = input("RSVP Status (Confirmed/Declined/Maybe): ")
            manager.add_attendee(event_name, attendee_name, email, rsvp_status)

        elif choice == "6":
            event_name = input("Event Name: ")
            email = input("Attendee Email to Remove: ")
            manager.remove_attendee(event_name, email)

        elif choice == "7":
            event_name = input("Event Name: ")
            manager.view_attendees(event_name)

        elif choice == "8":
            schedule_manager.display_upcoming_events()

        elif choice == "9":
            date = input("Enter date (YYYY-MM-DD): ")
            schedule_manager.filter_events_by_date(date)

        elif choice == "10":
            location = input("Enter location: ")
            schedule_manager.filter_events_by_location(location)

        elif choice == "11":
            event_name = input("Event Name: ")
            venue = float(input("Budget for Venue: "))
            catering = float(input("Budget for Catering: "))
            entertainment = float(input("Budget for Entertainment: "))
            miscellaneous = float(input("Budget for Miscellaneous: "))
            budget_manager.set_budget(event_name, venue, catering, entertainment, miscellaneous)

        elif choice == "12":
            event_name = input("Event Name: ")
            budget_manager.view_budget(event_name)

        elif choice == "13":
            print("Exiting Event Manager.")
            break

        else:
            print("Invalid choice. Please try again.")
