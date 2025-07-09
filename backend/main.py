from fastapi import FastAPI
import sqlite3
from typing import List, Dict

app = FastAPI()

# Function to get all assets from the database
def get_all_assets() -> List[Dict]:
    conn = sqlite3.connect("../assets.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assets")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# Root endpoint - just to test server is running
@app.get("/")
def read_root():
    return {"message": "Welcome to IT Asset Lifecycle Tracker API!"}

# Endpoint to get all assets
@app.get("/assets")
def read_assets():
    return get_all_assets()
