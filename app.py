"""
Hospital Analytics Dashboard.

This Streamlit app displays a simple dashboard using data from the
analytics schema.

For this first version, the app uses one analytics view:

    analytics.vw_appointments_by_status

Students can extend this dashboard by creating more views and charts.
"""

from pathlib import Path
import sys
import logging

import pandas as pd
import plotly.express as px
import streamlit as st

# ============================================================
# Import project modules
# ============================================================

# app.py is located at the project root.
# db_connection.py is located inside the src folder.
BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"

sys.path.append(str(SRC_DIR))

from db_connection import get_engine

# ============================================================
# Logging configuration
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

# ============================================================
# Streamlit page configuration
# ============================================================

st.set_page_config(
    page_title="Hospital Analytics Dashboard",
    page_icon="🏥",
    layout="wide"
)

# ============================================================
# Database connection
# ============================================================

engine = get_engine()

# ============================================================
# Data loading
# ============================================================

def load_appointments_by_status() -> pd.DataFrame:

    query = """
        SELECT
            status,
            total_appointments
        FROM analytics.vw_appointments_by_status;
    """

    logger.info("Loading data from analytics.vw_appointments_by_status")

    with engine.connect() as conn:
        return pd.read_sql(query,conn)

# ============================================================
# Dashboard layout
# ============================================================

st.title("Hospital Analytics Dashboard")
st.caption("Simple analytics dashboard powered by PostgreSQL and Streamlit.")

st.subheader("Appointments by Status")

appointments_by_status_df = load_appointments_by_status()

if appointments_by_status_df.empty:
    st.warning("No data available.Run the pipeline first.")
else:
    total_appointments = appointments_by_status_df["total_appointments"].sum()

    st.metric(
        label="Total appointments",
        value=int(total_appointments)
    )
