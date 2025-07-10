import sqlite3

conn = sqlite3.connect("assets.db")  # Connect or create database in project root
cursor = conn.cursor()

# Create the assets table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS assets (
    AssetTag TEXT PRIMARY KEY,
    Model TEXT,
    AssignedTo TEXT,
    Status TEXT,
    LastSeenDate TEXT,
    WarrantyEndDate TEXT,
    Department TEXT,
    Location TEXT
)
""")

conn.commit()
conn.close()

print("Table 'assets' created successfully!")
