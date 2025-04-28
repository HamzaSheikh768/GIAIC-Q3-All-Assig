import re
import streamlit as st

st.set_page_config(page_title="Password Strength Meter", layout="centered")

st.title("🔒 Password Strength Checker By Muhammad Faizan...")
st.write("Enter your password below to check its security level.")

def check_password_strength(password):
    score = 0
    feedback = []
    
    #-------------------------------------- Length Check----------------------------------
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")
    
    #-------------------------------------- Upper & Lowercase Check-----------------------------------
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase and lowercase letters**.")
    
    #-------------------------------------- Digit Check----------------------------------
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add **at least one number (0-9)**.")
    
    #--------------------------------------- Special Character Check---------------------------------
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")
    
    #---------------------------------------- Strength Rating----------------------------
    if score == 4:
        st.success("✅ Strong Password! 🎉")
    elif score == 3:
        st.info("⚠️ Moderate Password - Consider improving security.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")
    
    #----------------------------------------- Display feedback messages--------------------------
    if feedback:
        for msg in feedback:
            st.warning(msg)

#--------------------------------------------- Get user input-----------------------------------
password = st.text_input("Enter your password:", type="password", help="Ensure your password is **strong**.")
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password!")
