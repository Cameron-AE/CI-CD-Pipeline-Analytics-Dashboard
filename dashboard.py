import streamlit as st
from analysis import (
    load_data, compute_status_rates, average_duration,
    daily_status_counts, failures_by_author,
    author_daily_failures, find_anomalies
)

st.title("Pipeline Dashboard")

uploaded_file = st.file_uploader("Upload pipeline_data.csv", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.dataframe(df)

    rates = compute_status_rates(df)
    st.subheader("Status Rates")
    st.write(f"Success: {rates['success']:.2f}%")
    st.write(f"Failure: {rates['failure']:.2f}%")
    st.write(f"Cancelled: {rates['cancelled']:.2f}%")

    st.subheader("Average Duration")
    st.write(f"{average_duration(df):.2f} seconds")

    st.subheader("Daily Status Counts")
    st.dataframe(daily_status_counts(df))

    st.subheader("Failures by Author")
    st.bar_chart(failures_by_author(df))

    st.subheader("Author Daily Failures")
    st.dataframe(author_daily_failures(df))

    if st.checkbox("Show anomalies"):
        st.dataframe(find_anomalies(df))