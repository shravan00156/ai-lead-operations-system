import streamlit as st
import pandas as pd
import psycopg2

# ==========================================
# DATABASE CONNECTION
# ==========================================

DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/ai_lead_ops"

connection = psycopg2.connect(DATABASE_URL)

# ==========================================
# FETCH LEADS
# ==========================================

query = """
SELECT * FROM leads
ORDER BY id DESC
"""

df = pd.read_sql(query, connection)

# ==========================================
# PAGE TITLE
# ==========================================

st.set_page_config(
    page_title="AI Lead Ops Dashboard",
    layout="wide"
)

st.title("🚀 AI Lead Operations Dashboard")

# ==========================================
# METRICS
# ==========================================

total_leads = len(df)

high_priority = len(
    df[df["priority"] == "high"]
)

qualified_leads = len(
    df[df["status"] == "qualified"]
)

closed_leads = len(
    df[df["status"] == "closed"]
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Leads",
    total_leads
)

col2.metric(
    "High Priority",
    high_priority
)

col3.metric(
    "Qualified Leads",
    qualified_leads
)

col4.metric(
    "Closed Leads",
    closed_leads
)

# ==========================================
# RECENT LEADS
# ==========================================

st.subheader("📋 Recent Leads")

st.dataframe(df)

# ==========================================
# STATUS DISTRIBUTION
# ==========================================

st.subheader("📊 Lead Status Distribution")

status_counts = df["status"].value_counts()

st.bar_chart(status_counts)

# ==========================================
# PRIORITY DISTRIBUTION
# ==========================================

st.subheader("🔥 Lead Priority Distribution")

priority_counts = df["priority"].value_counts()

st.bar_chart(priority_counts)

# ==========================================
# RECENT HIGH PRIORITY LEADS
# ==========================================

st.subheader("🚨 High Priority Leads")

high_priority_df = df[
    df["priority"] == "high"
]

st.dataframe(high_priority_df)

# ==========================================
# CLOSE DATABASE
# ==========================================

connection.close()