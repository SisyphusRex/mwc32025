"""Employee module"""

# Third Party Imports
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String, Float

# Base class for other models to inherit from
Base = declarative_base()


class Zipcode(Base):
    """Class to represent a single employee"""

    __tablename__ = "zipcodes"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    zip_code = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    latitude = Column(Float(2), nullable=False)
    longitude = Column(Float(2), nullable=False)

    def __init__(self, zip_code, city, state, latitude, longitude):
        """Constructor"""
        self.zip_code = zip_code
        self.city = city
        self.state = state
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        """String method"""
        return f"{self.zip_code:<10} {self.city:<10} {self.state:<10} {self.latitude:<10} {self.longitude:<10}"
