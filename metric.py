import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(layout="wide")
st.title("Dashboard - Cloud Computing Performance Metrics")

# Load data with caching
@st.cache_data
def load_data():
    df = pd.read_csv(r"D:\vmCloud_data.csv")
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df = df.sort_values("timestamp")
    return df

# Load data
with st.spinner("Loading and processing data..."):
    original_df = load_data()  # keep unfiltered copy
    df = original_df.copy()

# Sidebar filters
st.sidebar.subheader("Filter Data")

# Show total rows before filtering
st.sidebar.info(f"Original total rows: {len(original_df)}")

# Date range filter
if "timestamp" in df.columns:
    min_date = df["timestamp"].min().date()
    max_date = df["timestamp"].max().date()
    start_date, end_date = st.sidebar.date_input( 
        "Select Date Range",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    # Apply filtering only if selected range is smaller than full range
    if start_date != min_date or end_date != max_date:
        df = df[(df["timestamp"].dt.date >= start_date) & (df["timestamp"].dt.date <= end_date)]
        st.sidebar.info(f"Rows after filtering: {len(df)}")
    else:
        st.sidebar.info("Showing all rows (full date range selected)")

# Row display slider (for sample and summary)
row_display_limit = st.sidebar.slider(
    "Select number of rows to display",
    min_value=10,
    max_value=1000,
    value=100,
    step=10
)

# Sample preview
with st.expander(f"Preview: Sample of {row_display_limit} Rows"):
    st.dataframe(df.sample(min(row_display_limit, len(df))), use_container_width=True)

# Quick summary stats
if not df.empty:
    st.subheader("Quick Stats Summary")
    df_sample = df.sample(row_display_limit) if len(df) > row_display_limit else df
    st.dataframe(df_sample.describe().round(2), use_container_width=True)

    # CPU usage chart (sampled)
    if "timestamp" in df.columns and "cpu_usage" in df.columns:
        df_chart = df[["timestamp", "cpu_usage"]].dropna()
        if len(df_chart) > 1000:
            df_chart = df_chart.sample(500, random_state=1)
        st.subheader("CPU Usage Over Time")
        st.line_chart(df_chart.set_index("timestamp"))

    # Average metrics per VM
    if all(col in df.columns for col in ["vm_id", "cpu_usage", "memory_usage", "power_consumption"]):
        st.subheader("Average Resource Usage per VM")
        avg_metrics = (
            df.groupby("vm_id")[["cpu_usage", "memory_usage", "power_consumption"]]
            .mean()
            .dropna()
            .round(2)
        )
        if len(avg_metrics) > 50:
            avg_metrics = avg_metrics.sample(50, random_state=1)
        st.line_chart(avg_metrics)

    # Task status distribution
    if "task_status" in df.columns:
        st.subheader("Task Status Distribution")
        status_counts = df["task_status"].value_counts()
        st.bar_chart(status_counts)

else:
    st.warning("No data available for the selected date range.")

