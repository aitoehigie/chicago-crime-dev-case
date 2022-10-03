from datetime import datetime
from enum import unique
from typing import TYPE_CHECKING, List, Optional, Union, Any, Tuple

from pydantic import BaseModel, Field, Extra, validator
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from chicago_crime_dev_case.security import User


class Crime(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    unique_key: int
    case_number: str
    date: datetime
    block: str
    iucr: str
    primary_type: str
    description: str
    location_description: str
    arrest: bool
    domestic: bool
    beat: int = None
    district: int = None
    ward: int = None
    community_area: int = None
    fbi_code: str = None
    x_coordinate: float = None
    y_coordinate: float = None
    year: int = None
    updated_on: datetime
    latitude: float = 0.0
    longitude: float = 0.0
    location: str = None


class CrimeResponse(BaseModel):
    """This the serializer exposed on the API"""

    unique_key: int
    case_number: str
    date: datetime
    block: str
    iucr: str
    primary_type: str
    description: str
    location_description: str
    arrest: bool
    domestic: bool
    beat: int = None
    district: int = None
    ward: int = None
    community_area: int = None
    fbi_code: str = None
    x_coordinate: float = None
    y_coordinate: float = None
    year: int = None
    updated_on: datetime
    latitude: float = None
    longitude: float = None
    location: str = None
    
    class Config:
        validate_assignment = True
    
    @validator('latitude')
    def latitude_must_be_type_float(cls, latitude):
        if isinstance(latitude, float):
            return latitude
        return float(0)
    
    @validator('longitude')
    def longitude_must_be_type_float(cls, longitude):
        if isinstance(longitude, float):
            return longitude
        return float(0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CrimeIncoming(BaseModel):
    """This is the serializer used for POST/PATCH requests"""

    unique_key: int
    case_number: str
    date: datetime
    block: str
    iucr: str
    primary_type: str
    description: str
    location_description: str
    arrest: bool
    domestic: bool
    beat: int = None
    district: int = None
    ward: int = None
    community_area: int = None
    fbi_code: str = None
    x_coordinate: float = None
    y_coordinate: float = None
    year: int = None
    updated_on: datetime
    latitude: float = None
    longitude: float = None
    location: str = None
    
    class Config:
        validate_assignment = True
    
    @validator('latitude')
    def latitude_must_be_type_float(cls, latitude):
        if isinstance(latitude, float):
            return latitude
        return float(0)
    
    @validator('longitude')
    def longitude_must_be_type_float(cls, longitude):
        if isinstance(longitude, float):
            return longitude
        return float(0)    
    class Config:
        extra = Extra.allow
        arbitrary_types_allowed = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

