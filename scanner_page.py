
import streamlit as st

def show_scanner():

    st.title("🔍 PII Scanner")
    st.write("Detect and classify sensitive customer information.")

    data = [
        {
            "Column": "customer_name",
            "Classification": "Name",
            "Risk": "High"
        },
        {
            "Column": "email",
            "Classification": "Email",
            "Risk": "High"
        },
        {
            "Column": "phone",
            "Classification": "Phone",
            "Risk": "High"
        },
        {
            "Column": "city",
            "Classification": "Location",
            "Risk": "Medium"
        },
        {
            "Column": "customer_id",
            "Classification": "Identifier",
            "Risk": "Medium"
        }
    ]

    st.table(data)

    st.success("PII Scanning Completed")
