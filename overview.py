
import streamlit as st

def show_overview():

    st.title("🔐 Maskforge Security Dashboard")

    st.subheader("Data Privacy & PII Protection")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", "1250")
    col2.metric("PII Columns", "5")
    col3.metric("Security Status", "Protected")

    st.divider()

    st.subheader("Database Connection")

    st.success("Database Connected")

    st.write("Welcome to Maskforge!")

