from psycopg2 import connect, extensions, sql

conn = connect(
    host="localhost",
    port=54321,
    database="peloton_db",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS workouts")

create_table = '''CREATE TABLE workouts(
    workout_timestamp VARCHAR(255),
    live_on_demand VARCHAR(255),
    instructor_name VARCHAR(255),
    length VARCHAR(255),
    fitness_discipline VARCHAR(255),
    type VARCHAR(255),
    title VARCHAR(255),
    class_timestamp VARCHAR(50),
    total_output FLOAT,
    average_watts FLOAT,
    average_resistance VARCHAR(255),
    average_cadence FLOAT,
    average_speed FLOAT,
    distance FLOAT,
    calories_burned FLOAT,
    average_heartrate FLOAT
)'''

cur.execute(create_table)

conn.commit()

with open('../data/clean_data.csv', 'r') as file:
    next(file)
    cur.copy_from(file, 'workouts', sep=',')

conn.commit()

conn.close()