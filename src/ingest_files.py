# pathlib is used to work with file and folder paths in a clean way.
# It is preferable to manually concatenating strings for paths.
from pathlib import Path

# datetime is used to register when files were loaded or processed.
from datetime import datetime

# Displays informational and error messages in the terminal.
import logging

# pandas is used to read CSV files and load them into PostgreSQL.
import pandas as pd

# text is used to safely execute SQL queries with parameters.
from sqlalchemy import text

# SQLAlchemyError is used to catch database-related errors.
from sqlalchemy.exc import SQLAlchemyError

# get_engine centralizes the database connection logic.
# The credentials are handled in src/db_connection.py using the .env file.
from db_connection import get_engine


# ============================================================
# Logging configuration
# ============================================================

# Configure logging to show messages in the terminal only.
# No log file is created.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

# Create a logger for this file.
logger = logging.getLogger(__name__)



# ============================================================
# Database connection
# ============================================================

# Create a reusable SQLAlchemy engine.
# This engine is used by pandas and SQLAlchemy to connect to PostgreSQL.
engine = get_engine()


# ============================================================
# Project folders
# ============================================================

# BASE_DIR points to the root folder of the project.
# Example:
# If this file is located at:
# hospital_analytics_project/src/ingest_files.py
#
# Then BASE_DIR will be:
# hospital_analytics_project
BASE_DIR = Path(__file__).resolve().parent.parent

# RAW_DATA_DIR points to the folder where raw CSV files are stored.
# Expected structure:
# data/raw/patients/
# data/raw/doctors/
# data/raw/appointments/
# data/raw/treatments/
# data/raw/billing/
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

# ============================================================
# Source configuration
# ============================================================

# SOURCES maps each type of CSV file to:
# 1. the folder where the files are located
# 2. the PostgreSQL schema
# 3. the PostgreSQL table where the data should be loaded
#
# Example:
# CSV files in data/raw/appointments/
# will be loaded into raw.appointments
SOURCES = {
    "patients": {
        "folder": RAW_DATA_DIR / "patients",
        "schema": "raw",
        "table": "patients",
    },
    "doctors": {
        "folder": RAW_DATA_DIR / "doctors",
        "schema": "raw",
        "table": "doctors",
    },
    "appointments": {
        "folder": RAW_DATA_DIR / "appointments",
        "schema": "raw",
        "table": "appointments",
    },
    "treatments": {
        "folder": RAW_DATA_DIR / "treatments",
        "schema": "raw",
        "table": "treatments",
    },
    "billing": {
        "folder": RAW_DATA_DIR / "billing",
        "schema": "raw",
        "table": "billing",
    },
}