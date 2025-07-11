🚀 TrackIT - IT Asset Lifecycle Tracker

TrackIT is a beginner-friendly, end-to-end DevOps project designed to help automate the tracking of IT assets within an organization. It uses modern technologies like **Python**, **FastAPI**, **SQLite**, **Docker**, **GitHub Actions**, and **Power BI** to build a lightweight asset management system.

🎯 Project Goals

- 🗃️ Track IT assets across departments
- 🔄 Automate data ingestion from CSV to a database
- 🧠 Serve data via a modern API (FastAPI)
- 📊 Visualize IT asset lifecycle via Power BI
- ⚙️ Deploy using Docker and CI/CD (GitHub Actions)
- 🛠️ Learn real-world DevOps and backend practices

📁 Project Structure

```plaintext
TrackIT/
├── backend/
│   ├── main.py                 # FastAPI backend code
│   ├── assets.db               # SQLite database (ignored via .gitignore)
│   └── __pycache__/            # Python cache files
├── data/
│   └── asset_data.csv          # Sample CSV file with raw asset data
├── docs/
│   └── TrackIT_Documentation.pdf  # Full beginner documentation
├── scripts/
│   ├── etl.py                  # ETL script to load CSV to SQLite
│   └── create_table.py         # Script to create table in SQLite DB
├── README.md                   # This project overview and documentation
├── query_db.py                 # Simple script to manually test DB queries
├── .gitignore                  # Files and folders Git should ignore
└── .github/
    └── workflows/
        └── ci.yml              # GitHub Actions CI workflow



