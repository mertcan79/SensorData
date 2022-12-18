from pydantic import BaseModel


class Sensor(BaseModel):
    id: int
    type: str
    timestamp: str
    value: int

    class Config:
        orm_mode = True


class AggregatedSensorData(BaseModel):
    id: int
    type: str
    min_time: str = '2022-12-12 12:34:56.123456'
    max_time: str = '2023-12-12 12:34:56.123456'
    agg_timeframe: str = '5Min'

    class Config:
        orm_mode = True
