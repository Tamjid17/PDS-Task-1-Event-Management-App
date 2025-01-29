# Event Management System 🎉

A Python-based Command Line Interface (CLI) application designed to streamline event organization, attendee tracking, schedule management, and budget oversight.

---

## Features ✨

### 📅 Event Management
- **Create/Edit/Delete Events**: Manage events with name, date/time, location, and description.
- **CSV Storage**: Events are stored in `events.csv` for persistence.
- **Event Overview**: View all events with key details.

### 👥 Attendee Management
- **Add/Remove Attendees**: Manage attendees per event with name, email, and RSVP status.
- **Attendee Tracking**: View attendee lists with RSVP statuses (Confirmed/Declined/Maybe).

### 🕒 Schedule Management
- **Upcoming Events**: Display chronologically ordered upcoming events.
- **Filters**: Filter events by date or location.

### 💰 Budget Management
- **Budget Allocation**: Set budgets for venue, catering, entertainment, and miscellaneous costs.
- **Budget Overview**: View allocated budgets per event.

### 🚀 Advanced Features (Partial/Future Implementation)
- *Event Search*: Filter events by name/date/location (basic implementation).
- *Data Export*: CSV export functionality (via file access).

## Running the Application ⚙️

1. **Prerequisites**: Ensure Python 3.8+ is installed.
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Event-Management-App.git
   cd Event-Management-App
   python main.py

---

## File Structure 📂

```plaintext
Event-Management-App/
├─ main.py                 # Entry point for the CLI application
├─ schedule_manager.py     # Handles event scheduling and filters
├─ budget_manager.py       # Manages budget allocation and tracking
├─ event_manager.py        # Core logic for event/attendee management
├─ events.csv              # Database for storing event data
├─ __pycache__/            # Python cache directory