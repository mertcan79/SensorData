# SensorData

A FastAPI based application which is capable of storing raw measurements from
sensors as well as retrieve data aggregates from these sensors upon request.

The data is stored in a Postgresql database and psycopg2 is used.

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

The user enters parameters to shape the resulting data such as sensor ID, measurement type, resampling frequency and the timeframe.

3. / endpoint lists all the entries in the sensors table.

The test script creates random variables using the /create end point and creates aggregations using the /get endpoint.

Some things are left on a non production level ready state for simplicity and explicity rather than creating a big project.
