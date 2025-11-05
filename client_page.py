# import streamlit as st
# from db_config import get_connection
# from datetime import datetime
# import pandas as pd

# def client_page(username):
#     """Client dashboard: submit new query & view all queries."""
    
#     st.title(" Client Query Dashboard")
#     st.write(f"Hello, **{username}**! Submit a new query or track your previous ones below.")

#     tab1, tab2 = st.tabs([" Submit Query", " My Queries"])

#     # TAB 1: SUBMIT NEW QUERY
#     with tab1:
#         with st.form("submit_query_form"):
#             email = st.text_input("Email ID")
#             mobile = st.text_input("Mobile Number")
#             heading = st.text_input("Query Heading")
#             description = st.text_area("Query Description")

#             submitted = st.form_submit_button("Submit Query")
#             if submitted:
#                 if not all([email, mobile, heading, description]):
#                     st.warning("Please fill all fields before submitting.")
#                 else:
#                     conn = get_connection()
#                     cursor = conn.cursor()
#                     created_time = datetime.now()
#                     cursor.execute("""
#                         INSERT INTO queries 
#                         (mail_id, mobile_number, query_heading, query_description, status, query_created_time)
#                         VALUES (%s, %s, %s, %s, %s, %s)
#                     """, (email, mobile, heading, description, "Open", created_time))
#                     conn.commit()
#                     conn.close()
#                     st.success("Query submitted successfully!")

#     # TAB 2: VIEW QUERIES
#     with tab2:
#         conn = get_connection()
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute("SELECT * FROM queries ORDER BY query_created_time DESC")
#         data = cursor.fetchall()
#         conn.close()

#         if data:
#             df = pd.DataFrame(data)
#             st.dataframe(df[['query_id', 'query_heading', 'status', 'query_created_time', 'query_closed_time']])
#         else:
#             st.info("No queries found yet.")

#     # LOGOUT BUTTON
#     st.markdown("---")
#     if st.button("Logout"):
#         st.session_state.clear()
#         st.experimental_rerun()

# =============================================================================================================================

# import streamlit as st
# from db_config import get_connection
# from datetime import datetime
# import pandas as pd

# def client_page(username):
#     """Client dashboard: submit new query & view all queries."""

#     # --- Page Header ---
#     st.title("💬 Client Query Dashboard")
#     st.write(f"Welcome, **{username}**! Use the buttons below to submit a new query or view your previous ones.")

#     # --- Add Custom Button Style ---
#     st.markdown("""
#     <style>
#     div.stButton > button {
#         background-color: #2E86C1;
#         color: white;
#         border-radius: 12px;
#         font-weight: bold;
#         font-size: 18px;
#         width: 220px;
#         height: 60px;
#         transition: all 0.3s ease;
#         margin: 10px;
#     }
#     div.stButton > button:hover {
#         background-color: #1B4F72;
#         transform: scale(1.05);
#         color: white;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # --- Session variable to track which section is active ---
#     if "client_section" not in st.session_state:
#         st.session_state["client_section"] = "submit"  # default section

#     # --- Navigation Buttons ---
#     space1, col1, col2, space2 = st.columns([1, 2, 2, 1])
#     with col1:
#         submit_btn = st.button("📝 Submit Query")
#     with col2:
#         view_btn = st.button("📄 View My Queries")

#     # --- Change section based on button click ---
#     if submit_btn:
#         st.session_state["client_section"] = "submit"
#     if view_btn:
#         st.session_state["client_section"] = "view"

#     # --- SUBMIT QUERY SECTION ---
#     if st.session_state["client_section"] == "submit":
#         st.subheader("📝 Submit a New Query")

#         with st.form("submit_query_form"):
#             email = st.text_input("Email ID")
#             mobile = st.text_input("Mobile Number")
#             heading = st.text_input("Query Heading")
#             description = st.text_area("Query Description")

#             submitted = st.form_submit_button("Submit Query")
#             if submitted:
#                 if not all([email, mobile, heading, description]):
#                     st.warning("⚠️ Please fill all fields before submitting.")
#                 else:
#                     conn = get_connection()
#                     cursor = conn.cursor()
#                     created_time = datetime.now()
#                     cursor.execute("""
#                         INSERT INTO queries 
#                         (mail_id, mobile_number, query_heading, query_description, status, query_created_time)
#                         VALUES (%s, %s, %s, %s, %s, %s)
#                     """, (email, mobile, heading, description, "Open", created_time))
#                     conn.commit()
#                     conn.close()
#                     st.success("✅ Query submitted successfully!")

#     # --- VIEW QUERIES SECTION ---
#     elif st.session_state["client_section"] == "view":
#         st.subheader("📋 My Submitted Queries")

#         conn = get_connection()
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute("SELECT * FROM queries ORDER BY query_created_time DESC")
#         data = cursor.fetchall()
#         conn.close()

#         if data:
#             df = pd.DataFrame(data)
#             st.dataframe(df[['query_id', 'query_heading', 'status', 'query_created_time', 'query_closed_time']])
#         else:
#             st.info("No queries found yet.")

#     # --- Logout Button ---
    
#     col_space, col_logout, col_empty = st.columns([2, 1, 2])
#     with col_logout:
#         logout = st.button("🚪 Logout")
#     if logout:
#         st.session_state.clear()
#         st.rerun()

# ==========================================================================================================


import streamlit as st
from db_config import get_connection
from datetime import datetime
import pandas as pd

def client_page(username):
    """Client dashboard: submit new query & view all queries."""

    # --- Page Configuration ---
    st.set_page_config(layout="wide")  # ✅ Makes the entire page wide

    # --- Page Header ---
    st.title("Client Query Dashboard")
    st.markdown(f"### Welcome, **{username}**! Use the buttons below to submit a new query or view your previous ones.")

    # --- Custom Styles for Buttons & Layout ---
    st.markdown("""
    <style>
    /* Make main page area wider */
    .main {
        max-width: 95%;
        padding: 2rem;
        margin: auto;
    }

    /* Make dataframe container full width */
    [data-testid="stDataFrame"] {
        width: 100% !important;
        min-width: 95vw !important;
    }

    /* Improve readability of table text */
    table {
        font-size: 16px !important;
    }

    /* Style all buttons */
    div.stButton > button {
        background-color: #2E86C1;
        color: white;
        border-radius: 12px;
        font-weight: bold;
        font-size: 18px;
        width: 240px;
        height: 60px;
        transition: all 0.3s ease;
        margin: 10px;
    }
    div.stButton > button:hover {
        background-color: #1B4F72;
        transform: scale(1.05);
        color: white;
    }

    /* Improve section headings */
    h1, h2, h3 {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- Session variable to track which section is active ---
    if "client_section" not in st.session_state:
        st.session_state["client_section"] = "submit"  # default section

    # --- Navigation Buttons ---
    space1, col1, col2, space2 = st.columns([1, 2, 2, 1])
    with col1:
        submit_btn = st.button("Submit Query")
    with col2:
        view_btn = st.button("View My Queries")

    # --- Change section based on button click ---
    if submit_btn:
        st.session_state["client_section"] = "submit"
    if view_btn:
        st.session_state["client_section"] = "view"

    # --- SUBMIT QUERY SECTION ---
    if st.session_state["client_section"] == "submit":
        st.subheader("Submit a New Query")

        with st.form("submit_query_form"):
            email = st.text_input("Email ID")
            mobile = st.text_input("Mobile Number")
            heading = st.text_input("Query Heading")
            description = st.text_area("Query Description", height=150)

            submitted = st.form_submit_button("Submit Query")
            if submitted:
                if not all([email, mobile, heading, description]):
                    st.warning(" Please fill all fields before submitting.")
                else:
                    conn = get_connection()
                    cursor = conn.cursor()
                    created_time = datetime.now()
                    cursor.execute("""
                        INSERT INTO queries 
                        (mail_id, mobile_number, query_heading, query_description, status, query_created_time)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (email, mobile, heading, description, "Open", created_time))
                    conn.commit()
                    conn.close()
                    st.success("Query submitted successfully!")

    # --- VIEW QUERIES SECTION ---
    elif st.session_state["client_section"] == "view":
        st.subheader("My Submitted Queries")

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM queries ORDER BY query_created_time DESC")
        data = cursor.fetchall()
        conn.close()

        if data:
            df = pd.DataFrame(data)
            st.dataframe(df[['query_id', 'query_heading', 'status', 'query_created_time', 'query_closed_time']],
                         use_container_width=True)
        else:
            st.info("No queries found yet. Submit one to get started!")

    # --- Logout Button ---
    

    col_space, col_logout, col_empty = st.columns([1, 2, 2])
    with col_logout:
        logout = st.button("Logout")
    if logout:
        st.session_state.clear()
        st.rerun()
