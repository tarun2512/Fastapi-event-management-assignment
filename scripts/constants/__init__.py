class AppSpec:
    name = "Mini Event Management System"
    summary = "A backend service to manage events and attendees 📅"
    description = """## Overview

The Mini Event Management System provides a scalable and efficient backend service that allows users to create events, register attendees, and retrieve attendee information for specific events. Designed with clean architecture and asynchronous capabilities using FastAPI and PostgreSQL, this module ensures data integrity, handles edge cases like duplicate registration or overbooking, and offers timezone-adjusted scheduling for global compatibility.

## Features

* **Event Creation**:
  Create events with fields such as name, location, timings, and max capacity, stored in PostgreSQL for reliability.

* **Upcoming Events Listing**:
  List all future events with filtering capabilities based on event start times in a time zone-aware manner.

* **Attendee Registration**:
  Register attendees to specific events with validations to prevent duplicate emails and overbooking based on `max_capacity`.

* **Attendee Retrieval**:
  Retrieve the list of attendees for a particular event, supporting pagination for better performance on large datasets.

* **Clean Architecture**:
  Modular separation of concerns using routers, services, and models to ensure maintainability and testability.

* **Timezone Management**:
  All events are created in IST (Indian Standard Time) and adapt dynamically to other timezones during view or registration.

* **Validation and Error Handling**:
  Meaningful responses and strict validation using Pydantic schemas to ensure a robust API.

* **Bonus Features**:
  * Async implementation using FastAPI for non-blocking IO
  * Pagination on attendee listings
  * Swagger/OpenAPI auto-generated documentation
  * Unit testing support using `pytest` (optional for extended robustness)

"""
