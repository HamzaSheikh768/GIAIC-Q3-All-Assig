import streamlit as st
from PIL import Image
import os

# Page config
st.set_page_config(page_title="Muhammad Faizan | Portfolio", page_icon="💼", layout="wide")

# Try to load image if available
image_path = "profile.png"
if os.path.exists(image_path):
    profile_pic = Image.open(image_path)
    st.image(profile_pic, width=200)

# Header
st.title("👨‍💻 Muhammad Faizan")
st.subheader("Front-End Developer | Python Developer | Tech Enthusiast")
st.markdown("📍 Karachi, Pakistan")

# --- About Section ---
st.markdown("## 🧑‍💼 About Me")
st.markdown("""
I'm a passionate front-end developer with strong skills in HTML, CSS, Tailwind CSS, JavaScript, TypeScript, React, and Next.js.  
I also work with back-end tools like Node.js, Firebase, Supabase, and Sanity CMS.  
Currently learning Python and working on AI-related projects in GIAIC.
""")

# --- Skills ---
st.markdown("## 🚀 Skills")
cols = st.columns(4)
skills = [
    "HTML", "CSS", "TailwindCSS", "JavaScript",
    "React", "Next.js", "TypeScript", "Python",
    "Firebase", "Supabase", "Sanity CMS", "MongoDB"
]
for i, skill in enumerate(skills):
    cols[i % 4].markdown(f"- {skill}")

# --- Projects ---
st.markdown("## 🧩 Projects")
st.markdown("### 🔹 Media Mart (E-commerce Website)")
st.markdown("""
Built a dynamic e-commerce platform with Next.js, Sanity CMS, and Stripe integration.  
Features include product listings, dynamic cart, and secure checkout.
""")

st.markdown("### 🔹 Streamlit Apps")
st.markdown("""
- BMI Calculator  
- Python Guessing Games  
- Mad Libs Generator  
- Countdown Timer  
All built in Python using Streamlit.
""")

# --- Contact ---
st.markdown("## 📬 Contact")
st.markdown("""
- 📧 Email: [muhammadf4060@gmail.com](mailto:muhammadf4060@gmail.com)  
- 💼 LinkedIn: [linkedin.com/in/muhammadfaizan](https://linkedin.com)  
- 🌐 Website: [muhammadfaizan.site](http://muhammadfaizan.site)  
""")

# Footer
st.markdown("---")
st.markdown("© 2025 Muhammad Faizan — All Rights Reserved.")
