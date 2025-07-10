from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List

app = FastAPI()

DATABASE = "assets.db"

# Asset data model
class Asset(BaseModel):
    AssetTag: str
    Model: str
    AssignedTo: str
    Status: str
    LastSeenDate: str
    WarrantyEndDate: str
    Department: str
    Location: str

# Helper to get DB connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Create assets table if not exists
def create_table():
    conn = get_db_connection()
    conn.execute("""
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

create_table()

@app.get("/assets", response_model=List[Asset])
def get_all_assets():
    conn = get_db_connection()
    assets = conn.execute("SELECT * FROM assets").fetchall()
    conn.close()
    return [dict(asset) for asset in assets]

@app.get("/assets/{asset_tag}", response_model=Asset)
def get_asset_by_tag(asset_tag: str):
    conn = get_db_connection()
    asset = conn.execute("SELECT * FROM assets WHERE AssetTag = ?", (asset_tag,)).fetchone()
    conn.close()
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return dict(asset)

@app.post("/assets", response_model=Asset)
def create_asset(asset: Asset):
    conn = get_db_connection()
    try:
        conn.execute("""
            INSERT INTO assets (AssetTag, Model, AssignedTo, Status, LastSeenDate, WarrantyEndDate, Department, Location)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (asset.AssetTag, asset.Model, asset.AssignedTo, asset.Status, asset.LastSeenDate, asset.WarrantyEndDate, asset.Department, asset.Location))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Asset with this AssetTag already exists")
    conn.close()
    return asset

@app.put("/assets/{asset_tag}", response_model=Asset)
def update_asset(asset_tag: str, asset: Asset):
    conn = get_db_connection()
    existing_asset = conn.execute("SELECT * FROM assets WHERE AssetTag = ?", (asset_tag,)).fetchone()
    if existing_asset is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Asset not found")
    conn.execute("""
        UPDATE assets SET Model = ?, AssignedTo = ?, Status = ?, LastSeenDate = ?, WarrantyEndDate = ?, Department = ?, Location = ?
        WHERE AssetTag = ?
    """, (asset.Model, asset.AssignedTo, asset.Status, asset.LastSeenDate, asset.WarrantyEndDate, asset.Department, asset.Location, asset_tag))
    conn.commit()
    conn.close()
    return asset

@app.delete("/assets/{asset_tag}")
def delete_asset(asset_tag: str):
    conn = get_db_connection()
    asset = conn.execute("SELECT * FROM assets WHERE AssetTag = ?", (asset_tag,)).fetchone()
    if asset is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Asset not found")
    conn.execute("DELETE FROM assets WHERE AssetTag = ?", (asset_tag,))
    conn.commit()
    conn.close()
    return {"detail": f"Asset {asset_tag} deleted"}
# This is a test comment to check git changes
