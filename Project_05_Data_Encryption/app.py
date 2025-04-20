import streamlit as st
import hashlib
import os
import json
from cryptography.fernet import Fernet

# Utility Functions

def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as f:
            f.write(key)
    else:
        with open("secret.key", "rb") as f:
            key = f.read()
    return key

def save_data():
    with open("data.json", "w") as f:
        json.dump(stored_data, f)

def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return {}

# Key and Cipher
KEY = load_key()
cipher = Fernet(KEY)

# Persistent storage
stored_data = load_data()

# Session State Setup
if "failed_attempts" not in st.session_state:
    st.session_state["failed_attempts"] = 0
if "authorized" not in st.session_state:
    st.session_state["authorized"] = True

# Hashing Function
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt Function
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# Decrypt Function
def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)
    if encrypted_text in stored_data and stored_data[encrypted_text]["passkey"] == hashed_passkey:
        st.session_state.failed_attempts = 0
        return cipher.decrypt(encrypted_text.encode()).decode()
    st.session_state.failed_attempts += 1
    return None

# Streamlit App
st.title("🔒 Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login", "Admin"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data)
            stored_data[encrypted_text] = {"passkey": hashed_passkey}
            save_data()
            st.success("✅ Data stored securely!")
            st.write("🔐 Encrypted Text:", encrypted_text)
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Retrieve Data":
    if not st.session_state.authorized:
        st.warning("🔐 Please login first.")
        st.stop()

    st.subheader("🔍 Retrieve Your Data")
    encrypted_text = st.text_area("Enter Encrypted Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            decrypted_text = decrypt_data(encrypted_text, passkey)

            if decrypted_text:
                st.success(f"✅ Decrypted Data: {decrypted_text}")
            else:
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts remaining: {attempts_left}")
                if st.session_state.failed_attempts >= 3:
                    st.session_state.authorized = False
                    st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                    st.experimental_rerun()
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":
            st.session_state.failed_attempts = 0
            st.session_state.authorized = True
            st.success("✅ Reauthorized successfully! Redirecting to Retrieve Data...")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect password!")

elif choice == "Admin":
    st.subheader("🔐 Admin View: Encrypted Entries")
    if stored_data:
        for i, key in enumerate(stored_data.keys(), start=1):
            st.write(f"{i}. 🔐 {key[:30]}...")
    else:
        st.info("No data stored yet.")