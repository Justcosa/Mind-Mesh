from fastapi import FastAPI, Depends
from fastAPI.journalAPI import get_db
from datetime import datetime
import sqlite3

def get_db_connection():
    # Connects to the same SQLite database as journalAPI.py
    conn = get_db()
    conn.row_factory = sqlite3.Row  # Optional: enables dict-like access to rows
    return conn

def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM journals")
    rows = cursor.fetchall()
    conn.close()  # Safe to close because fetchall() materializes all data
    print(rows)  # Debugging: print fetched rows
    return rows

def create_entry(mood: str, entry: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current device date and time
    cursor.execute(
        "INSERT INTO journals (mood, entry, date) VALUES (?, ?, ?)",
        (mood, entry, current_date)
    )
    conn.commit()
    conn.close()
    return {"message": "Entry created successfully"}

def delete_entry(entry_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM journals WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()
    return {"message": f"Entry with id {entry_id} deleted successfully"}
