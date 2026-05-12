import streamlit as st
from streamlit.components.v1 import html

# 1. Page Config
st.set_page_config(page_title="INDEPENDO", page_icon="*", layout="wide")

# 2. Session State Initialization
if "page" not in st.session_state:
    st.session_state.page = "name"
if "favourites" not in st.session_state:
    st.session_state.favourites = []
if "roadmap_text" not in st.session_state:
    st.session_state.roadmap_text = ""

# 3. Custom CSS
st.markdown("""
<style>
    .main {background:#0b1220;}
    h1, h2, h3, h4, p, li, label {color:#e5e7eb !important;}
    .skill {padding:16px; border-radius:14px; background:#020617; margin:10px; transition:0.4s; text-align:center; border: 1px solid #1e293b;}
    .skill:hover {background:#0f172a; transform:scale(1.06); color:#7dd3fc; border-color: #38bdf8;}
    .tag {font-size:13px; color:#93c5fd;}
    .skill-list {text-align:center; font-size:18px; padding:6px; transition:0.3s;}
    .skill-list:hover {color:#7dd3fc;}
    .popup {background:#020617; padding:12px; border-radius:12px; border:1px solid #38bdf8;}
</style>
""", unsafe_allow_html=True)

# 4. Helper for Rerun (Ensures compatibility with older Streamlit versions)
def safe_rerun():
    try:
        st.rerun()
    except AttributeError:
        st.experimental_rerun()

# 5. Carousel Component
def carousel(height="90vh"):
    html(f"""
    <style>
        .slider {{width:100%; height:{height}; overflow:hidden; border-radius:20px;}}
        .slides {{display:flex; width:700%; animation:slide 14s infinite ease-in-out;}}
        .slides img {{width:100%; height:{height}; object-fit:cover;}}
        @keyframes slide {{
            0%{{margin-left:0%;}} 14%{{margin-left:0%;}} 
            28%{{margin-left:-100%;}} 42%{{margin-left:-200%;}} 
            56%{{margin-left:-300%;}} 70%{{margin-left:-400%;}} 
            84%{{margin-left:-500%;}} 100%{{margin-left:-600%;}} 
        }}
    </style>
    <div class="slider"><div class="slides">
        <img src="https://images.unsplash.com/photo-1518770660439-4636190af475">
        <img src="https://images.unsplash.com/photo-1581090700227-1e37b190418e">
        <img src="https://images.unsplash.com/photo-1526378722484-bd91ca387e72">
        <img src="https://images.unsplash.com/photo-1603575448878-868a20723f5d">
        <img src="https://images.unsplash.com/photo-1535223289827-42f1e9919769">
        <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f">
        <img src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d">
    </div></div>
    """, height=500)

# 6. Sidebar/Header UI
left, mid, right = st.columns([2, 6, 2])
with left:
    if st.button("📩 Contact Info"):
        st.session_state.show_contact = True
    if st.session_state.get("show_contact"):
        st.markdown("""
        <div class="popup">
            <b>Contact INDEPENDO</b><br><br>
            📧 logicloop.independo@gmail.com <br>
            🔗 <a href='https://linkedin.com' style='color:#7dd3fc'>LinkedIn</a> <br>
            🐙 <a href='https://github.com' style='color:#7dd3fc'>GitHub</a>
        </div>
        """, unsafe_allow_html=True)
        if st.button("OK"):
            st.session_state.show_contact = False
            safe_rerun()

with right:
    st.markdown("### 🤍 Favourites")
    for f in st.session_state.favourites:
        st.caption("⭐ " + f)

st.markdown("<h1 style='text-align:center;'>INDEPENDO</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;color:#93c5fd;'>your personalized path to skill, clarity and confidence</h4>", unsafe_allow_html=True)
st.info("🔐 Your data stays only with you. We do NOT store anything.")

# 7. Page Routing Logic
if st.session_state.page == "name":
    st.markdown("### 🌟 “Don’t wait for opportunity. Create it.”")
    name = st.text_input("👤 Enter your name and press ENTER")
    carousel("70vh")
    if name:
        st.session_state.name = name
        st.session_state.page = "skill"
        safe_rerun()

elif st.session_state.page == "skill":
    st.markdown(f"## Welcome, {st
