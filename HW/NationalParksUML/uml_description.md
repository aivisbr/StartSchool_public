# Park Management System - UML Class Diagram Description

## Overview
This UML class diagram represents a park management system that handles multiple parks, their lodges, staff (rangers), visitors, and entry permits (tickets and annual passes).

## Class Structure

### Core Classes

#### **Park**
The central entity representing a national park or similar recreational area.

**Attributes:**
- `name`: str - Name of the park
- `location`: Tuple[float, float] - Geographic coordinates (latitude, longitude)
- `area_km2`: float - Park area in square kilometers
- `opening_hours`: str - Operating hours
- `established_year`: Optional[int] - Year the park was established
- `lodges`: List[Lodge] - Collection of lodges within the park
- `rangers`: List[Ranger] - Collection of rangers assigned to the park
- `visitors_today`: int - Current day's visitor count

**Methods:**
- `get_location()`: Returns the park's geographic coordinates

---

#### **Lodge**
Represents accommodation facilities within a park.

**Attributes:**
- `name`: str - Lodge name
- `park`: Park - Reference to the parent park
- `capacity`: int - Total room capacity
- `available_rooms`: int - Currently available rooms
- `price_per_night`: Decimal - Nightly rate
- `location`: Optional[Tuple[float, float]] - Specific lodge coordinates (falls back to park location if not set)

**Methods:**
- `get_location()`: Returns lodge coordinates or park coordinates if not specified
- `book_room()`: Attempts to book a room, returns success status

---

### User Hierarchy

#### **User** (Base Class)
Abstract base class for all system users.

**Attributes:**
- `name`: str - User's full name
- `email`: str - Email address
- `phone`: str - Contact phone number
- `created_at`: datetime - Account creation timestamp

---

#### **Visitor** (extends User)
Represents park visitors/guests.

**Attributes:**
- `age`: int - Visitor's age
- `ticket`: Optional[Ticket] - Current ticket (if any)
- `annual_pass`: Optional[AnnualPass] - Annual pass (if any)
- `visit_history`: List[Tuple[Park, date]] - Record of past park visits

**Methods:**
- `record_visit()`: Logs a park visit to the visitor's history

---

#### **Ranger** (extends User)
Represents park staff/employees.

**Attributes:**
- `employee_id`: str - Unique employee identifier
- `park`: Park - Assigned park
- `is_on_duty`: bool - Current duty status

**Methods:**
- `clock_in()`: Mark ranger as on duty
- `clock_out()`: Mark ranger as off duty

---

### Entry Permit Classes

#### **Ticket**
Single-use or limited-duration park entry permit.

**Attributes:**
- `park`: Park - Park this ticket is valid for
- `visitor`: Visitor - Ticket holder
- `purchase_date`: date - Date of purchase
- `price`: Decimal - Ticket cost
- `ticket_type`: str - Type (e.g., "single_day", "multi_day", "group")
- `used`: bool - Whether ticket has been used
- `entry_time`: Optional[datetime] - Timestamp when ticket was used for entry

**Methods:**
- `is_valid()`: Checks if ticket is still valid
- `use()`: Marks ticket as used and records entry time

---

#### **AnnualPass**
Year-long unlimited park access permit.

**Attributes:**
- `year`: int - Valid year
- `visitor`: Visitor - Pass holder
- `price`: Decimal - Pass cost
- `pass_type`: str - Type (e.g., "individual", "family", "senior")
- `purchase_date`: date - Purchase date
- `parks_visited`: List[Park] - Parks visited with this pass

**Methods:**
- `is_valid()`: Checks if pass is valid for current year
- `record_park_visit()`: Adds a park to the visited parks list

---

## Relationships

### Inheritance (IS-A relationships)
- **User** ← **Visitor**: A Visitor is a type of User
- **User** ← **Ranger**: A Ranger is a type of User

### Composition/Aggregation (HAS-A relationships)
- **Park** ◆→ **Lodge**: Parks contain lodges
- **Park** ◆→ **Ranger**: Parks have rangers assigned to them
- **Park** ◆→ **Ticket**: Tickets are associated with specific parks
- **Visitor** ◆→ **Ticket**: Visitors have tickets
- **Visitor** ◆→ **AnnualPass**: Visitors have annual passes

### Associations
- **AnnualPass** → **Park**: Annual passes track which parks have been visited
- **Lodge** → **Park**: Each lodge belongs to a park
- **Ranger** → **Park**: Each ranger is assigned to a park
- **Ticket** → **Park**: Each ticket is valid for a specific park

---

## Key Design Patterns

1. **Inheritance**: The User base class provides common attributes (name, email, phone, created_at) to both Visitor and Ranger subclasses

2. **Composition**: Parks aggregate Lodges and Rangers, representing strong ownership relationships

3. **Strategy Pattern**: Entry validation can work with either Ticket or AnnualPass objects

4. **Delegation Pattern**: Lodge's `get_location()` method delegates to Park's location when the lodge doesn't have specific coordinates

---

## Business Logic Highlights

- **Entry Control**: Visitors can enter parks if they have either a valid ticket or annual pass
- **Staff Management**: Rangers are assigned to specific parks and can track their duty status
- **Accommodation**: Lodges track capacity and availability for booking
- **Usage Tracking**: Both tickets and annual passes track usage and validity
- **Visit History**: System maintains records of visitor activity across parks
