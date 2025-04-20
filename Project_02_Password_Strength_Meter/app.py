import re
import streamlit as st

# Function to check password strength
def check_password_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    else:
        return "❌ Password should be at least 8 characters long."
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        return "❌ Include both uppercase and lowercase letters."
    
    if re.search(r"\d", password):
        score += 1
    else:
        return "❌ Add at least one number (0-9)."
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        return "❌ Include at least one special character (!@#$%^&*)."
    
    if score == 4:
        return "✅ Strong Password!"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features."
    else:
        return "❌ Weak Password - Improve it using the suggestions above."


# Streamlit App
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter")
st.write("Check how strong your password is based on standard security practices.")

# Password Input
password = st.text_input("Enter your password", type="password")

# Check & Display Strength
if password:
    strength = check_password_strength(password)
    st.markdown(f"**Result:** {strength}")
