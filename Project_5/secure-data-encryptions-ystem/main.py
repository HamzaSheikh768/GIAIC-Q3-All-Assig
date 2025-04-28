import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Generate a Fernet key (symmetric encryption key)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# In-memory database
stored_data = {}  # {"encrypted_text1": {"encrypted_text": "...", "passkey": "hashed"}}
failed_attempts = 0  # Counter for wrong attempts


# 🔐 Function to hash the passkey using SHA-256
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()


# 🔐 Function to encrypt user data
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()


# 🔓 Function to decrypt user data
def decrypt_data(encrypted_text, passkey):
    global failed_attempts
    hashed_passkey = hash_passkey(passkey)

    # Search in all stored entries
    for data in stored_data.values():
        if data["encrypted_text"] == encrypted_text and data["passkey"] == hashed_passkey:
            failed_attempts = 0  # Reset counter on success
            return cipher.decrypt(encrypted_text.encode()).decode()

    failed_attempts += 1
    return None


# 🌐 Streamlit UI
st.set_page_config(page_title="Secure Data Encryption", page_icon="🛡️")
st.title("🛡️ Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigate", menu)

# 🏠 HOME PAGE
if choice == "Home":
    st.subheader("🏠 Welcome")
    st.markdown("""
        This app allows you to **securely store and retrieve data** using a **unique passkey**.
        \n🔐 Encryption: `Fernet (Symmetric Encryption)`
        \n🔑 Passkeys are securely hashed before storing.
    """)

# 📥 STORE DATA
elif choice == "Store Data":
    st.subheader("📥 Store New Data")

    user_data = st.text_area("Enter Data to Encrypt:")
    passkey = st.text_input("Enter a Passkey:", type="password")

    if st.button("Encrypt & Store"):
        if user_data and passkey:
            encrypted = encrypt_data(user_data)
            hashed = hash_passkey(passkey)

            stored_data[encrypted] = {
                "encrypted_text": encrypted,
                "passkey": hashed
            }

            st.success("✅ Data Encrypted & Stored Securely!")
            st.code(encrypted, language="text")
        else:
            st.error("⚠️ Please enter both data and a passkey.")

# 🔓 RETRIEVE DATA
elif choice == "Retrieve Data":
    st.subheader("🔓 Retrieve Encrypted Data")

    encrypted_input = st.text_area("Paste Encrypted Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_input and passkey:
            decrypted = decrypt_data(encrypted_input, passkey)

            if decrypted:
                st.success("✅ Decryption Successful!")
                st.code(decrypted, language="text")
            else:
                st.error(f"❌ Incorrect passkey! Attempts left: {3 - failed_attempts}")

                if failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts. Redirecting to Login...")
                    st.experimental_rerun()
        else:
            st.error("⚠️ Both fields are required.")

# 🔐 LOGIN / REAUTH
elif choice == "Login":
    st.subheader("🔐 Reauthorization Required")

    master_pass = st.text_input("Enter Admin Password:", type="password")

    if st.button("Login"):
        if master_pass == "admin123":  # Demo password, can be changed
            failed_attempts = 0
            st.success("✅ Login Successful. Redirecting to Retrieve Page...")
            st.rerun()  # ✅ Use this instead of experimental_rerun
        else:
            st.error("❌ Wrong admin password!")

