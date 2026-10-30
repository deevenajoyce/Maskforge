
import streamlit as st

def show_policy():

    st.title("🛡️ Role Based Masking Simulator")

    role = st.selectbox(
        "Select User Role",
        ["Admin", "Customer Support", "Data Analyst"]
    )

    st.subheader("Customer Record")

    if role == "Admin":

        st.write("Name: Rahul Kumar")
        st.write("Email: rahul@gmail.com")
        st.write("Phone: 9876543210")

    elif role == "Customer Support":

        st.write("Name: Rahul Kumar")
        st.write("Email: r****@gmail.com")
        st.write("Phone: ******3210")

    else:

        st.write("Name: HIDDEN")
        st.write("Email: HIDDEN")
        st.write("Phone: HIDDEN")

    st.write("City: Hyderabad")

