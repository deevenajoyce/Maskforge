
import streamlit as st

def show_audit():

    st.title("📋 Security Audit Logs")

    data = [
        {
            "User": "Admin01",
            "Role": "Admin",
            "Action": "Viewed Records",
            "Status": "Success"
        },
        {
            "User": "Support01",
            "Role": "Support",
            "Action": "Accessed Email",
            "Status": "Success"
        },
        {
            "User": "Analyst01",
            "Role": "Analyst",
            "Action": "Viewed Data",
            "Status": "Success"
        }
    ]

    st.table(data)
