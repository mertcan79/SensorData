# SensorData

A FastAPI based application which is capable of storing raw measurements from
sensors as well as retrieve data aggregates from these sensors upon request.

The data is stored in a Postgresql database and psycopg2 is used for simplicity.

There are three main end points, home, get and create.

1. The /create endpoint adds sensor info to database
- Sensor ID
- Measurement type
- Timestamp of recording
- Measurement value

2. The /get endpoint creates an aggregation of the existing data and returns statistics based on the resampling.

The returned aggregates contain:
- Min value
- Mean value
- Max value
- Timestamp of the aggregated datapoint
The user inserts parameters to shape the resulting data such as sensor ID, measurement type, resampling frequency and the timeframe.
