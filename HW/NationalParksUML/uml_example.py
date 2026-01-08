from typing import List, Optional, Tuple
from datetime import date, datetime
from decimal import Decimal


class Park:
    def __init__(
        self, 
        name: str, 
        location: Tuple[float, float],  # (latitude, longitude)
        area_km2: float,
        opening_hours: str = "8:00-18:00"
    ) -> None:
        self.name: str = name
        self.location: Tuple[float, float] = location
        self.area_km2: float = area_km2
        self.opening_hours: str = opening_hours
        self.lodges: List['Lodge'] = []
        self.rangers: List['Ranger'] = []
        self.visitors_today: int = 0
        self.established_year: Optional[int] = None
    
    def get_location(self) -> Tuple[float, float]:
        return self.location
    

class Lodge:
    def __init__(
        self, 
        name: str, 
        park: Park,
        capacity: int,
        price_per_night: Decimal,
        location: Optional[Tuple[float, float]] = None
    ) -> None:
        self.name: str = name
        self.park: Park = park
        self.capacity: int = capacity
        self.price_per_night: Decimal = price_per_night
        self.location: Optional[Tuple[float, float]] = location
        self.available_rooms: int = capacity
        self.park.add_lodge(self)
    
    def get_location(self) -> Tuple[float, float]:
        """Returns lodge location, or park location if not set"""
        if self.location:
            return self.location
        return self.park.get_location()
    
    def book_room(self) -> bool:
        if self.available_rooms > 0:
            self.available_rooms -= 1
            return True
        return False


class User:
    def __init__(self, name: str, email: str, phone: str) -> None:
        self.name: str = name
        self.email: str = email
        self.phone: str = phone
        self.created_at: datetime = datetime.now()


class Visitor(User):
    def __init__(self, name: str, email: str, phone: str, age: int) -> None:
        super().__init__(name, email, phone)
        self.age: int = age
        self.ticket: Optional['Ticket'] = None
        self.annual_pass: Optional['AnnualPass'] = None
        self.visit_history: List[Tuple[Park, date]] = []
    
    def record_visit(self, park: Park, visit_date: date) -> None:
        self.visit_history.append((park, visit_date))
    


class Ranger(User):
    def __init__(
        self, 
        name: str, 
        email: str, 
        phone: str,
        park: Park,
        employee_id: str
    ) -> None:
        super().__init__(name, email, phone)
        self.employee_id: str = employee_id
        self.park: Park = park
        self.is_on_duty: bool = False
        self.park.add_ranger(self)
    
    def clock_in(self) -> None:
        self.is_on_duty = True
    
    def clock_out(self) -> None:
        self.is_on_duty = False


class Ticket:
    def __init__(
        self, 
        park: Park, 
        purchase_date: date,
        visitor: Visitor,
        price: Decimal
    ) -> None:
        self.park: Park = park
        self.purchase_date: date = purchase_date
        self.visitor: Visitor = visitor
        self.price: Decimal = price
        self.used: bool = False
        self.entry_time: Optional[datetime] = None
        self.ticket_type: str = "single_day"  # or "multi_day", "group", etc.
    
    def is_valid(self) -> bool:
        return not self.used and self.purchase_date == date.today()
    
    def use(self) -> None:
        self.used = True
        self.entry_time = datetime.now()


class AnnualPass:
    def __init__(
        self, 
        year: int, 
        visitor: Visitor,
        price: Decimal,
        pass_type: str = "individual"
    ) -> None:
        self.year: int = year
        self.visitor: Visitor = visitor
        self.price: Decimal = price
        self.pass_type: str = pass_type  # "individual", "family", "senior"
        self.purchase_date: date = date.today()
        self.parks_visited: List[Park] = []
    
    def is_valid(self) -> bool:
        from datetime import datetime
        return datetime.now().year == self.year
    
    def record_park_visit(self, park: Park) -> None:
        if park not in self.parks_visited:
            self.parks_visited.append(park)
