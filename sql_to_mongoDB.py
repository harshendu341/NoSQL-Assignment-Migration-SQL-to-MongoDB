import pymongo
import sqlite3

# Connect to MongoDB (assuming it's running on localhost)
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['flightDatabase']  # Create or connect to a database named 'flightDatabase'
collection = db['flights']  # Create a collection named 'flights' within the database

# Reconnect to SQLite to fetch data
conn = sqlite3.connect('flightDatabase.db')  # Connect to 'flightDatabase.db'
cursor = conn.cursor()

# Fetch data from SQLite flights table
cursor.execute('SELECT * FROM flights')
rows = cursor.fetchall()

# Insert each row into MongoDB
for row in rows:
    flight_doc = {
        'flight_number': row[1],
        'origin': row[2],
        'destination': row[3],
        'departure_date': row[4],
        'arrival_date': row[5]
    }
    collection.insert_one(flight_doc)

# Close connections
conn.close()
client.close()
