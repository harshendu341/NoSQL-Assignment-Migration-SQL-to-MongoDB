import tkinter as tk
import sqlite3
import pymongo

def fetch_sqlite_flights():
    # Connect to SQLite database
    conn = sqlite3.connect('flightDatabase.db')
    cursor = conn.cursor()

    # Query and fetch all data from the flights table
    cursor.execute('SELECT * FROM flights')
    rows = cursor.fetchall()

    # Close connection
    conn.close()

    return rows

def fetch_mongodb_flights():
    # Connect to MongoDB (assuming it's running on localhost)
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['flightDatabase']
    collection = db['flights']

    # Retrieve all documents (flight data) from MongoDB collection
    flights_data = list(collection.find())

    # Close MongoDB connection
    client.close()

    return flights_data

def display_flights():
    # Fetch flights data from SQLite
    sqlite_flights = fetch_sqlite_flights()

    # Fetch flights data from MongoDB
    mongodb_flights = fetch_mongodb_flights()

    # Create GUI window
    root = tk.Tk()
    root.title("Flight Data Viewer")

    # Create a text widget for SQLite flight data (comma-separated values)
    sqlite_text_widget = tk.Text(root, height=15, width=80)
    sqlite_text_widget.pack(padx=20, pady=10)

    # Insert SQLite flight data into the text widget as comma-separated values
    sqlite_text_widget.insert(tk.END, "SQLite Flight Data:\n\n")
    for flight in sqlite_flights:
        flight_info = ", ".join(str(field) for field in flight) + "\n"
        sqlite_text_widget.insert(tk.END, flight_info)

    # Create a text widget for MongoDB flight data (key-value pairs)
    mongodb_text_widget = tk.Text(root, height=15, width=80)
    mongodb_text_widget.pack(padx=20, pady=10)

    # Insert MongoDB flight data into the text widget as key-value pairs
    mongodb_text_widget.insert(tk.END, "MongoDB Flight Data (Key-Value Pairs):\n\n")
    for flight in mongodb_flights:
        flight_info = f"Flight Number: {flight['flight_number']}\nOrigin: {flight['origin']}\nDestination: {flight['destination']}\nDeparture Date: {flight['departure_date']}\nArrival Date: {flight['arrival_date']}\n\n"
        mongodb_text_widget.insert(tk.END, flight_info)

    # Run the GUI main loop
    root.mainloop()

# Call the display_flights function to show SQLite and MongoDB flight data in the GUI
display_flights()
