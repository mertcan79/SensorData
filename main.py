from fastapi import FastAPI, Body
from typing import Dict
from datetime import datetime
import pandas as pd
import numpy as np
from db.schemas import Sensor, AggregatedSensorData
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from core.config import Settings


def start_application():
    app = FastAPI(title='MertcanCoskun', version='1.0.0')
    return app


settings = Settings()

app = start_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.post("/create/", )
# Insert the user data into the database
def create_sensor(sensor_to_insert: Sensor = Body(...)):
    connection = psycopg2.connect(user=settings.POSTGRES_USER,
                                  password=settings.POSTGRES_PASSWORD,
                                  host=settings.POSTGRES_SERVER,
                                  port=settings.POSTGRES_PORT,
                                  database=settings.POSTGRES_DB)
    # Create a cursor
    cursor = connection.cursor()

    # Execute the INSERT statement
    cursor.execute("INSERT INTO sensors (id, type, timestamp, value) VALUES (%s, %s, %s, %s)",
                   (sensor_to_insert.id, sensor_to_insert.type, sensor_to_insert.timestamp, sensor_to_insert.value))

    # Commit the transaction
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return {"message": "Row inserted successfully"}


@app.get("/get")
def get_sensor(request_data: AggregatedSensorData) -> Dict:
    try:
        connection = psycopg2.connect(user=settings.POSTGRES_USER,
                                      password=settings.POSTGRES_PASSWORD,
                                      host=settings.POSTGRES_SERVER,
                                      port=settings.POSTGRES_PORT,
                                      database=settings.POSTGRES_DB)
        cursor = connection.cursor()

        type_for_query = request_data.type
        id_for_query = request_data.id
        min_time_for_query = request_data.min_time
        max_time_for_query = request_data.max_time

        q = "SELECT * FROM sensors WHERE type = '{}' AND id ={} AND (timestamp >= '{}' AND timestamp <= '{}' )". \
            format(type_for_query, id_for_query, min_time_for_query, max_time_for_query)
        cursor.execute(q)
        records = cursor.fetchall()
        df = pd.DataFrame(records, columns=['id', 'type', 'timestamp', 'value'])
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        result_df = df.groupby(pd.Grouper(freq=request_data.agg_timeframe, key='timestamp')).agg(
            Mean=('value', np.mean),
            Min=('value', np.min),
            Max=('value', np.max))
        result_df = result_df.reset_index()
        result_df = result_df[(request_data.min_time <= result_df.timestamp) & (request_data.max_time > result_df.timestamp)]

        return result_df.dropna().to_dict()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


@app.get("/")
def read_sensors():
    try:
        connection = psycopg2.connect(user=settings.POSTGRES_USER,
                                      password=settings.POSTGRES_PASSWORD,
                                      host=settings.POSTGRES_SERVER,
                                      port=settings.POSTGRES_PORT,
                                      database=settings.POSTGRES_DB)
        cursor = connection.cursor()
        q = "SELECT * FROM sensors"

        cursor.execute(q)
        records = cursor.fetchall()
        return records

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
