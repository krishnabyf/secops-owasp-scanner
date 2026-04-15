import os
import sqlite3

# -----------------------------
# SQL Injection Vulnerability
# -----------------------------
def login(username, password):
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    return conn.execute(query).fetchone()


# -----------------------------
# Command Injection Vulnerability
# -----------------------------
def run_command(user_input):
    os.system("ls " + user_input)  # Unsafe user input


# -----------------------------
# Hardcoded Secret (OWASP)
# -----------------------------
def connect_service():
    password = "admin123"  # Hardcoded secret
    return password


# -----------------------------
# Insecure Deserialization (Simulated)
# -----------------------------
import pickle

def load_data(data):
    return pickle.loads(data)  # Unsafe deserialization