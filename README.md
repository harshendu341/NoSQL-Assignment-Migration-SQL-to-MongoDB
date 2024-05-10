# Flight Data Management System

This repository contains Python scripts for managing flight data using SQLite and MongoDB databases.

## Prerequisites

Before running the scripts, make sure you have the following installed:

- Python 3.x
- SQLite (included with Python)
- MongoDB
- Required Python libraries (`pymongo`, `tkinter`)

## Setup and Execution

Follow these steps to set up and execute the scripts in the correct order:

1. **SQL_db_creation.py**
    - This script initializes a SQLite database (`flightDatabase.db`) and creates a `flights` table to store flight records.
    - Run this script first to create the SQLite database and table.
    ```bash
    python SQL_db_creation.py
    ```

2. **sql_db_records.py**
    - Use this script to view the records stored in the SQLite database (`flightDatabase.db`).
    - This script displays flight records stored in the SQLite database.
    ```bash
    python sql_db_records.py
    ```

3. **sql_to_mongoDB.py**
    - This script migrates flight data from the SQLite database (`flightDatabase.db`) to a MongoDB database (`flightDatabase`) and `flights` collection.
    - Run this script to transfer flight data from SQLite to MongoDB.
    ```bash
    python sql_to_mongoDB.py
    ```

4. **flight_data_viewer.py**
    - This script displays flight data from both SQLite and MongoDB in a graphical user interface (GUI) using `tkinter`.
    - Execute this script after transferring data to MongoDB (`sql_to_mongoDB.py`).
    ```bash
    python flight_data_viewer.py
    ```

## File Descriptions

- `SQL_db_creation.py`: Python script to create a SQLite database (`flightDatabase.db`) and `flights` table.
- `sql_db_records.py`: Python script to view records stored in the SQLite database.
- `sql_to_mongoDB.py`: Python script to migrate flight data from SQLite to MongoDB.
- `flight_data_viewer.py`: Python script to display flight data from both SQLite and MongoDB in a `tkinter` GUI.

## Notes

- Ensure that MongoDB is running locally on `localhost` at port `27017` for successful interaction with MongoDB.
- Customize the scripts and GUI as needed based on specific requirements and preferences.
