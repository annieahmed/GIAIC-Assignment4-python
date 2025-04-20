# annie_website.py

import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Annie Ahmed | Portfolio", page_icon="👩‍💻", layout="wide")

# Custom CSS for full-page layout, darker green theme, and mobile friendly design
st.markdown("""
    <style>
        body, .main {
            background-color: #003300;
            color: #000000;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3, h4 {
            color: #66ff66;
        }
        .st-bx {
            background-color: #ccffcc !important;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 30px;
        }
        ul, p {
            font-size: 18px;
        }
        a {
            color: #003300;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
            color: #009900;
        }
        .footer {
            background-color: #000000;
            color: #ffffff;
            text-align: center;
            padding: 20px;
            font-size: 14px;
        }
        @media only screen and (max-width: 768px) {
            .st-bx {
                padding: 20px;
            }
            ul, p {
                font-size: 16px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation (mobile-friendly layout)
st.sidebar.title("📚 Navigate")
selection = st.sidebar.radio("Go to", ["Home", "About Me", "Skills", "Projects", "Contact"])

if selection == "Home":
    st.markdown("""
    <div class='st-bx'>
        <h1>👩‍💻 Annie Ahmed</h1>
        <h3>Welcome to my Streamlit Website!</h3>
    </div>
    """, unsafe_allow_html=True)

elif selection == "About Me":
    st.markdown("""
    <div class='st-bx'>
        <h2>📘 About Me</h2>
        <p>Hi! I'm <b>Annie Ahmed</b>, a passionate Python developer and tech enthusiast. I love building cool projects with Python and exploring AI, data science, and web development.</p>
    </div>
    """, unsafe_allow_html=True)

elif selection == "Skills":
    st.markdown("""
    <div class='st-bx'>
        <h2>🛠️ My Skills</h2>
        <ul>
            <li>✅ Python Programming</li>
            <li>✅ Web Apps with Streamlit</li>
            <li>✅ Data Analysis with Pandas</li>
            <li>✅ Machine Learning Basics</li>
            <li>✅ Problem Solving and Algorithms</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif selection == "Projects":
    st.markdown("""
    <div class='st-bx'>
        <h2>💡 My Projects</h2>
        <ul>
            <li>🔢 <a href="#">BMI Calculator App</a></li>
            <li>🎮 <a href="#">Guess the Number Game</a></li>
            <li>📋 <a href="#">To-Do App in Streamlit</a></li>
            <li>🧠 <a href="#">Rock, Paper, Scissors Game</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif selection == "Contact":
    st.markdown("""
    <div class='st-bx'>
        <h2>📬 Contact Me</h2>
        <p>Feel free to connect with me if you have any questions or project ideas!</p>
        <ul>
            <li>📧 Email: annie.ahmed@example.com</li>
            <li>🕊️ Twitter: <a href="https://twitter.com/" target="_blank">@anniecodes</a></li>
            <li>💼 LinkedIn: <a href="https://linkedin.com/" target="_blank">Annie Ahmed</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    <hr>
    ❤️ 2025 Annie Ahmed
</div>
""", unsafe_allow_html=True)
