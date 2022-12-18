from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class SensorBase(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(256), nullable=False)
    timestamp = Column(String(256), nullable=False)
    value = Column(Float, nullable=False)

    class Config:
        arbitrary_types_allowed = True

