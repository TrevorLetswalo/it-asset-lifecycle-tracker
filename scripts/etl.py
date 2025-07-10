import pandas as pd
import sqlite3

# Step 1: Load the data from CSV
df = pd.read_csv("../data/asset_data.csv")

# Step 2: Connect to SQLite database (auto-creates if not there)
conn = sqlite3.connect("../assets.db")

# Step 3: Load data into a table called "assets"
df.to_sql("assets", conn, if_exists="replace", index=False)

# Step 4: Confirm success
print("✅ Data loaded into 'assets.db' successfully.")

# Optional: Show preview
print(df.head())
