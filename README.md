Client Query Management System

A simple and efficient web-based system to manage client support queries using Python, Streamlit, and MySQL.
Clients can submit and track queries, while support staff can view, update, and close them — all through a clean and interactive dashboard.

Features

Role-based login (Client / Support)

Clients can submit and view their queries

Support team can filter, manage, and close queries

Organized data display using Pandas

Real-time updates and easy navigation

Tech Stack

Frontend: Streamlit

Backend: Python

Database: MySQL

Libraries: Pandas, Datetime, mysql-connector-python


# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

Project Structure
client_query_management/
│
├── app.py               # Main entry point (login/register)
├── auth.py              # Authentication logic
├── client_page.py       # Client dashboard
├── support_page.py      # Support dashboard
├── db_config.py         # Database connection
└── requirements.txt     # Dependencies
