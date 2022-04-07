import pandas as pd

df = pd.read_csv('../data/data.csv')

df.drop(columns=['Avg. Incline', 'Avg. Pace (min/mi)'], inplace=True)

# rename the columns
df = df.rename(columns = {
    'Workout Timestamp': 'workout_timestamp',
    'Live/On-Demand': 'live_on_demand',
    'Instructor Name': 'instructor_name',
    'Length (minutes)': 'length',
    'Fitness Discipline': 'fitness_discipline',
    'Type': 'type',
    'Title': 'title',
    'Class Timestamp': 'class_timestamp',
    'Total Output': 'total_output',
    'Avg. Watts': 'average_watts',
    'Avg. Resistance': 'average_resistance',
    'Avg. Cadence (RPM)': 'average_cadence',
    'Avg. Speed (mph)': 'average_speed',
    'Distance (mi)': 'distance',
    'Calories Burned': 'calories_burned',
    'Avg. Heartrate': 'average_heartrate'
    })


# Format the timestamp
df["workout_timestamp"] = pd.to_datetime(df["workout_timestamp"].str[:16])
df["class_timestamp"] = pd.to_datetime(df["class_timestamp"].str[:16])

# Remove the % symbol from the average resistance column
df['average_resistance'] = df['average_resistance'].str.rstrip('%')

filled_df = df.fillna({ 
    "live_on_demand": "",  
    "instructor_name": "",
    "type": "",
    "length": 0,
    "class_timestamp": "",
    "total_output": 0,
    "average_watts": 0,
    "average_resistance": 0,
    "average_cadence": 0,
    "average_speed": 0,
    "distance": 0,
    "calories_burned": 0,
    "average_heartrate": 0
})


filled_df.to_csv('../data/clean_data.csv', index=False)

