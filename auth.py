import mysql.connector
import hashlib
from db_config import get_connection

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, role):
    """Register a new user in the database."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        hashed_pw = hash_password(password)
        query = "INSERT INTO users (username, hashed_password, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, hashed_pw, role))
        conn.commit()
        conn.close()
        return True
    except mysql.connector.errors.IntegrityError:
        # Duplicate username
        return "duplicate"
    except Exception as e:
        print("Error:", e)
        return False

def login_user(username, password, role):
    """Validate username, password, and role."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    hashed_pw = hash_password(password)
    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND hashed_password=%s AND role=%s",
        (username, hashed_pw, role)
    )
    user = cursor.fetchone()
    conn.close()
    return user
