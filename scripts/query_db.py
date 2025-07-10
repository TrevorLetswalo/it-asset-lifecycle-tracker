import sqlite3
import pandas as pd

# Path to the SQLite database
db_path = "backend/assets.db"

# Connect to the database
conn = sqlite3.connect(db_path)

# Query the first 5 rows from the assets table
query = "SELECT * FROM assets LIMIT 5;"

# Load the results into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Display the results
print("✅ Preview of the assets table:")
print(df)
