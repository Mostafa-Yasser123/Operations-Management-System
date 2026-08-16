from enum import Enum


class UserRole(str, Enum):
    DELIVERY = "delivery"
    SUPERVISOR = "supervisor"
    MANAGER = "manager"
    ADMINISTRATOR = "administrator"
    
class VehicleType(str, Enum):
    MOTORCYCLE = "motorcycle"
    CAR = "car"
    VAN = "van"
    TRICYCLE = "tricycle"
    BICYCLE = "bicycle"
    OTHER = "other"   
    
class StoreStatus(str, Enum):
    available = "available"
    unavailable = "unavailable"    