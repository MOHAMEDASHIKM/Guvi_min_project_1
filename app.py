# import streamlit as st
# from auth import register_user, login_user
# from client_page import client_page
# from support_page import support_page

# # ----------------------------
# # APP CONFIGURATION
# # ----------------------------
# st.set_page_config(page_title="Client Query Management System", layout="centered")

# # ----------------------------
# # SESSION SETUP
# # ----------------------------
# if 'logged_in' not in st.session_state:
#     st.session_state['logged_in'] = False
# if 'username' not in st.session_state:
#     st.session_state['username'] = ""
# if 'role' not in st.session_state:
#     st.session_state['role'] = ""

# # ----------------------------
# # LOGIN + REGISTRATION PAGE
# # ----------------------------
# def login_page():
#     st.sidebar.title("🔐 Navigation")
#     menu = ["Login", "Register"]
#     choice = st.sidebar.selectbox("Select Option", menu)

#     # REGISTER
#     if choice == "Register":
#         st.title(" Register New User")
#         username = st.text_input("Enter Username")
#         password = st.text_input("Enter Password", type="password")
#         role = st.selectbox("Select Role", ["Client", "Support"])

#         if st.button("Register"):
#             result = register_user(username, password, role)
#             if result == True:
#                 st.success("✅ Registration successful! You can now log in.")
#             elif result == "duplicate":
#                 st.warning("⚠️ Username already exists. Try another or log in.")
#             else:
#                 st.error("❌ Registration failed. Please try again.")

#     # # LOGIN
#     # elif choice == "Login":
#     #     st.title("🔑 Login Page")
#     #     username = st.text_input("Username")
#     #     password = st.text_input("Password", type="password")
#     #     role = st.selectbox("Login As", ["Client", "Support"])

#     #     if st.button("Login"):
#     #         user = login_user(username, password, role)
#     #         if user:
#     #             st.session_state['logged_in'] = True
#     #             st.session_state['username'] = username
#     #             st.session_state['role'] = role
#     #             st.success(f"✅ Welcome {username}! Redirecting to {role} page...")
#     #             st.rerun()

#     #         else:
#     #             st.error("❌ Invalid credentials or role mismatch.")
    


# # LOGIN PAGE
#     elif choice == "Login":
#         st.title("Login Page")

#     # --- Custom CSS for styling the buttons ---
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

#     # --- Input fields ---
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     role = st.selectbox("Login As", ["Client", "Support"])

#     # --- Center both buttons in one row ---
#     space1, col1, col2, space2 = st.columns([1, 2, 2, 1])

#     with col1:
#         login_button = st.button("Login")
#     with col2:
#         register_button = st.button("Register New Account")

#     # --- Login logic ---
#     if login_button:
#         user = login_user(username, password, role)
#         if user:
#             st.session_state['logged_in'] = True
#             st.session_state['username'] = username
#             st.session_state['role'] = role
#             st.success(f"✅ Welcome {username}! Redirecting to {role} page...")
#             st.rerun()
#         else:
#             st.error("❌ Invalid credentials or role mismatch.")

#     # --- Register navigation ---
#     if register_button:
#         st.session_state['page'] = "Register"
#         st.rerun()




# # ----------------------------
# # MAIN APP NAVIGATION LOGIC
# # ----------------------------
# if not st.session_state['logged_in']:
#     login_page()
# else:
#     # Role-based routing
#     if st.session_state['role'] == "Client":
#         client_page(st.session_state['username'])
#     elif st.session_state['role'] == "Support":
#         support_page(st.session_state['username'])





import streamlit as st
from auth import register_user, login_user
from client_page import client_page
from support_page import support_page

# ----------------------------
# APP CONFIGURATION
# ----------------------------
st.set_page_config(page_title="Client Query Management System", layout="centered")

# ----------------------------
# SESSION SETUP
# ----------------------------
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""
if 'role' not in st.session_state:
    st.session_state['role'] = ""
if 'page' not in st.session_state:
    st.session_state['page'] = "Login"  # Default page

# ----------------------------
# GLOBAL BUTTON STYLES
# ----------------------------
st.markdown("""
<style>
div.stButton > button {
    background-color: #2E86C1;
    color: white;
    border-radius: 12px;
    font-weight: bold;
    font-size: 18px;
    width: 220px;
    height: 60px;
    transition: all 0.3s ease;
    margin: 10px;
}
div.stButton > button:hover {
    background-color: #1B4F72;
    transform: scale(1.05);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# LOGIN PAGE
# ----------------------------
def login_page():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Login As", ["Client", "Support"])

    # --- Center both buttons ---
    space1, col1, col2, space2 = st.columns([1, 2, 2, 1])
    with col1:
        login_button = st.button("Login")
    with col2:
        register_button = st.button("Register")

    # --- Login logic ---
    if login_button:
        user = login_user(username, password, role)
        if user:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['role'] = role
            st.success(f"✅ Welcome {username}! Redirecting to {role} page...")
            st.rerun()
        else:
            st.error("Invalid credentials or role mismatch.")

    # --- Go to Register page ---
    if register_button:
        st.session_state['page'] = "Register"
        st.rerun()

# ----------------------------
# REGISTER PAGE
# ----------------------------
def register_page():
    st.title("Register New User")

    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    role = st.selectbox("Select Role", ["Client", "Support"])

    # --- Center both buttons ---
    space1, col1, col2, space2 = st.columns([1, 2, 2, 1])
    with col1:
        register_button = st.button("Register")
    with col2:
        back_button = st.button("Back to Login")

    if register_button:
        result = register_user(username, password, role)
        if result == True:
            st.success("Registration successful! You can now log in.")
        elif result == "duplicate":
            st.warning("Username already exists. Try another or log in.")
        else:
            st.error("Registration failed. Please try again.")

    if back_button:
        st.session_state['page'] = "Login"
        st.rerun()

# ----------------------------
# MAIN APP NAVIGATION LOGIC
# ----------------------------
if not st.session_state['logged_in']:
    if st.session_state['page'] == "Login":
        login_page()
    elif st.session_state['page'] == "Register":
        register_page()
else:
    # Role-based routing
    if st.session_state['role'] == "Client":
        client_page(st.session_state['username'])
    elif st.session_state['role'] == "Support":
        support_page(st.session_state['username'])
