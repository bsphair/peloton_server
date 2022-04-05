# import psycopg2
import csv
from psycopg2 import connect, extensions, sql

conn = connect(
    host="localhost",
    port=54321,
    database="peloton_db",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

# cur.execute("select version()")

# data = cur.fetchone()
# print("Connection established to: ", data)

cur.execute("DROP TABLE IF EXISTS workouts")

create_table = '''CREATE TABLE workouts(
    workout_timestamp VARCHAR(50),
    live_on_demand VARCHAR(50),
    instructor_name VARCHAR(50),
    length INTEGER,
    fitness_discipline VARCHAR(50),
    type VARCHAR(50),
    title VARCHAR(255),
    class_timestamp TIMESTAMPTZ,
    total_output FLOAT,
    average_watts FLOAT,
    average_resistance VARCHAR(50),
    average_cadence FLOAT,
    average_speed FLOAT,
    distance FLOAT,
    calories_burned FLOAT,
    average_heartrate FLOAT
)'''

cur.execute(create_table)

conn.commit()

with open('test_data.csv', 'r') as file:
    next(file)
    cur.copy_from(file, 'workouts', sep=',')



conn.commit()

conn.close()