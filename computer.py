import streamlit as st
import pandas as pd
import re
import os

# Validation functions
def validate_name(name):
    return name.isalpha()

def validate_contact(contact):
    return contact.isdigit()

def validate_email(email):
    return bool(re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email))

# Main application
def main():
    st.title("Welcome to service")

    # Load existing data or create a new DataFrame
    if os.path.exists("customer_problems.csv"):
        df = pd.read_csv("customer_problems.csv")
    else:
        df = pd.DataFrame(columns=["Name", "Contact", "Email", "Problem", "Location"])

    with st.form("customer_form"):
        name = st.text_input("Name", max_chars=100)
        contact = st.text_input("Contact Number", max_chars=15)
        email = st.text_input("Email ID")
        problem = st.text_area("Problem Description")
        location = st.text_input("Location (Enter address or description)")

        submitted = st.form_submit_button("Submit")

        if submitted:
            if not validate_name(name):
                st.error("Invalid name. Only alphabets are allowed.")
            elif not validate_contact(contact):
                st.error("Invalid contact number. Only numbers are allowed.")
            elif not validate_email(email):
                st.error("Invalid email format.")
            else:
                # Append the new problem to the dataframe
                new_row = {"Name": name, "Contact": contact, "Email": email, "Problem": problem, "Location": location}
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

                # Save to CSV
                df.to_csv("customer_problems.csv", index=False)

                st.success(f"Thank you, {name}! We have recorded your problem and will get back to you shortly.")

   

if __name__ == "__main__":
    main()