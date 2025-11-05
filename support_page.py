# import streamlit as st
# import pandas as pd
# from db_config import get_connection
# from datetime import datetime

# def support_page(username):
#     st.subheader(f"Support Dashboard - Logged in as {username}")

#     filter_status = st.selectbox("Filter by Status", ["All", "Open", "Closed"])
#     conn = get_connection()
#     cursor = conn.cursor(dictionary=True)

#     query = "SELECT * FROM queries"
#     if filter_status != "All":
#         query += f" WHERE status='{filter_status}'"
#     cursor.execute(query)
#     rows = cursor.fetchall()
#     conn.close()

#     if rows:
#         df = pd.DataFrame(rows)
#         st.dataframe(df)

#         open_queries = [q['query_id'] for q in rows if q['status'] == 'Open']
#         selected_query = st.selectbox("Select Query to Close", open_queries)

#         if st.button("Close Selected Query"):
#             conn = get_connection()
#             cursor = conn.cursor()
#             close_time = datetime.now()
#             cursor.execute("UPDATE queries SET status=%s, query_closed_time=%s WHERE query_id=%s",
#                            ("Closed", close_time, selected_query))
#             conn.commit()
#             conn.close()
#             st.success(f"✅ Query {selected_query} closed successfully!")
#     else:
#         st.info("No queries found.")

# ===========================================================================================================================



# import streamlit as st
# import pandas as pd
# from db_config import get_connection
# from datetime import datetime

# def support_page(username):
#     st.title("Support Team Dashboard")
#     st.markdown(f"### Welcome, **{username}**!")

#     # --- Custom Styles for Table and Buttons ---
#     st.markdown("""
#     <style>
#     /* Make dataframe wider */
#     [data-testid="stDataFrame"] {
#         width: 100% !important;
#     }
#     /* Center button and add style */
#     div.stButton > button {
#         background-color: #2E86C1;
#         color: white;
#         border-radius: 10px;
#         font-weight: bold;
#         font-size: 16px;
#         width: 220px;
#         height: 50px;
#         transition: all 0.3s ease;
#         margin-top: 10px;
#     }
#     div.stButton > button:hover {
#         background-color: #1B4F72;
#         transform: scale(1.05);
#         color: white;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # --- Filter Section ---
#     st.subheader("Query Filter & Management")
#     filter_status = st.selectbox("Filter by Status", ["All", "Open", "Closed"])

#     conn = get_connection()
#     cursor = conn.cursor(dictionary=True)

#     query = "SELECT * FROM queries"
#     if filter_status != "All":
#         query += f" WHERE status='{filter_status}'"
#     cursor.execute(query)
#     rows = cursor.fetchall()
#     conn.close()

#     # --- Display Table ---
#     if rows:
#         df = pd.DataFrame(rows)
#         st.dataframe(df, use_container_width=True)

#         # --- Close Query Section ---
#         open_queries = [q['query_id'] for q in rows if q['status'] == 'Open']
#         if open_queries:
#             selected_query = st.selectbox("Select Open Query to Close", open_queries)
#             col1, col2, col3 = st.columns([1, 2, 1])
#             with col2:
#                 if st.button("✅ Close Selected Query"):
#                     conn = get_connection()
#                     cursor = conn.cursor()
#                     close_time = datetime.now()
#                     cursor.execute("""
#                         UPDATE queries 
#                         SET status=%s, query_closed_time=%s 
#                         WHERE query_id=%s
#                     """, ("Closed", close_time, selected_query))
#                     conn.commit()
#                     conn.close()
#                     st.success(f"✅ Query {selected_query} closed successfully!")
#                     st.rerun()
#         else:
#             st.info("All queries are already closed.")
#     else:
#         st.info("No queries found.")

#     # --- Logout Button ---
    
#     col_space, col_logout, col_empty = st.columns([2, 1, 2])
#     with col_logout:
#         if st.button("Logout"):
#             st.session_state.clear()
#             st.rerun()








import streamlit as st
import pandas as pd
from db_config import get_connection
from datetime import datetime

def support_page(username):
    # --- Page Configuration ---
    st.set_page_config(layout="wide")  # ✅ Makes the entire app full-width

    st.title("Support Team Dashboard")
    st.markdown(f"### Welcome, **{username}**!")

    # --- Custom Styles for Table and Buttons ---
    st.markdown("""
    <style>
    /* Make the entire content area wider */
    .main {
        max-width: 95%;
        padding: 2rem;
        margin: auto;
    }

    /* Make dataframe container fill page width */
    [data-testid="stDataFrame"] {
        width: 100% !important;
        min-width: 95vw !important;
    }

    /* Improve table readability */
    table {
        font-size: 16px !important;
    }

    /* Style buttons */
    div.stButton > button {
        background-color: #2E86C1;
        color: white;
        border-radius: 12px;
        font-weight: bold;
        font-size: 18px;
        width: 240px;
        height: 55px;
        transition: all 0.3s ease;
        margin-top: 10px;
    }
    div.stButton > button:hover {
        background-color: #1B4F72;
        transform: scale(1.05);
        color: white;
    }

    /* Style select boxes and headers */
    .stSelectbox label {
        font-size: 18px;
        font-weight: 600;
    }

    h1, h2, h3 {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- Filter Section ---
    st.subheader("Query Filter & Management")
    filter_status = st.selectbox("Filter by Status", ["All", "Open", "Closed"])

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM queries"
    if filter_status != "All":
        query += f" WHERE status='{filter_status}'"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    # --- Display Table ---
    if rows:
        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True)

        # --- Close Query Section ---
        open_queries = [q['query_id'] for q in rows if q['status'] == 'Open']
        if open_queries:
            selected_query = st.selectbox("Select Open Query to Close", open_queries)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("Close Selected Query"):
                    conn = get_connection()
                    cursor = conn.cursor()
                    close_time = datetime.now()
                    cursor.execute("""
                        UPDATE queries 
                        SET status=%s, query_closed_time=%s 
                        WHERE query_id=%s
                    """, ("Closed", close_time, selected_query))
                    conn.commit()
                    conn.close()
                    st.success(f"Query {selected_query} closed successfully!")
                    st.rerun()
        else:
            st.info("All queries are already closed.")
    else:
        st.info("No queries found.")

    # --- Logout Button ---
    st.markdown("---")
    col_space, col_logout, col_empty = st.columns([2, 1, 2])
    with col_logout:
        if st.button("Logout"):
            st.session_state.clear()
            st.rerun()

