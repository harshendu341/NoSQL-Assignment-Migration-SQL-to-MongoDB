import sqlite3
import random
from datetime import datetime, timedelta

# Create a SQLite connection and cursor
conn = sqlite3.connect('flightDatabase.db')  # Use 'flightDatabase.db' as the SQLite database
cursor = conn.cursor()

# Create a flights table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS flights (
        id INTEGER PRIMARY KEY,
        flight_number TEXT,
        origin TEXT,
        destination TEXT,
        departure_date TEXT,
        arrival_date TEXT
    )
''')


# Function to generate random flight data
def generate_flight_data(num_records):
    flights_data = []
    cities = ['JFK', 'LAX', 'ORD', 'SFO', 'ATL', 'DFW', 'LHR', 'CDG', 'FRA', 'MUC', 'DXB', 'PEK', 'HND']

    for _ in range(num_records):
        flight_number = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2)) + str(random.randint(100, 999))
        origin = random.choice(cities)
        destination = random.choice(cities)
        while destination == origin:
            destination = random.choice(cities)

        departure_date = datetime.now() + timedelta(days=random.randint(1, 30))
        arrival_date = departure_date + timedelta(hours=random.randint(1, 12))

        flights_data.append((flight_number, origin, destination, departure_date.strftime('%Y-%m-%d %H:%M:%S'),
                             arrival_date.strftime('%Y-%m-%d %H:%M:%S')))

    return flights_data


# Generate flight data (200 records)
flights_data = generate_flight_data(200)

# Insert generated data into the flights table
cursor.executemany('''
    INSERT INTO flights (flight_number, origin, destination, departure_date, arrival_date)
    VALUES (?, ?, ?, ?, ?)
''', flights_data)

# Commit changes and close connection
conn.commit()
conn.close()
