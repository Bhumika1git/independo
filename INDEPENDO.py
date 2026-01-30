import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="INDEPENDO", page_icon="*", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "name"

if "favourites" not in st.session_state:
    st.session_state.favourites = []

if "roadmap_text" not in st.session_state:
    st.session_state.roadmap_text = ""

st.markdown("""
<style>
.main {background:#0b1220;}
h1,h2,h3,h4,p,li,label {color:#e5e7eb !important;}
.skill {padding:16px;border-radius:14px;background:#020617;margin:10px;transition:0.4s;text-align:center;}
.skill:hover {background:#0f172a;transform:scale(1.06);color:#7dd3fc;}
.tag {font-size:13px;color:#93c5fd;}
.skill-list {text-align:center;font-size:18px;padding:6px;transition:0.3s;}
.skill-list:hover {color:#7dd3fc;}
.popup {background:#020617;padding:12px;border-radius:12px;border:1px solid #38bdf8;}
</style>
""", unsafe_allow_html=True)

def carousel(height="90vh"):
    html(f"""
    <style>
    .slider {{width:100%;height:{height};overflow:hidden;border-radius:20px;}}
    .slides {{display:flex;width:700%;animation:slide 14s infinite ease-in-out;}}
    .slides img {{width:100%;height:{height};object-fit:cover;}}
    @keyframes slide {{
      0%{{margin-left:0%;}}14%{{margin-left:0%;}}
      28%{{margin-left:-100%;}}42%{{margin-left:-200%;}}
      56%{{margin-left:-300%;}}70%{{margin-left:-400%;}}
      84%{{margin-left:-500%;}}100%{{margin-left:-600%;}}
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
    """, height=600)

left, mid, right = st.columns([2,6,2])

with left:
    if st.button("📩 Contact Info"):
        st.session_state.show_contact = True

if st.session_state.get("show_contact"):
    st.markdown("""
    <div class="popup">
    <b>Contact INDEPENDO</b><br><br>
    📧 logicloop.independo@gmail.com <br>
    🔗 https://linkedin.com <br>
    🐙 https://github.com
    </div>
    """, unsafe_allow_html=True)
    if st.button("OK"):
        st.session_state.show_contact = False
        st.rerun()

with right:
    st.markdown("### 🤍 Favourites")
    for f in st.session_state.favourites:
        st.caption("⭐ " + f)

st.markdown("<h1 style='text-align:center;'>INDEPENDO</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;color:#93c5fd;'>your personalized path to skill, clarity and confidence</h4>", unsafe_allow_html=True)
st.info("🔐 Your data stays only with you. We do NOT store anything.")

if st.session_state.page == "name":

    st.markdown("### 🌟 “Don’t wait for opportunity. Create it.”")
    name = st.text_input("👤 Enter your name and press ENTER")

    carousel("92vh")

    if name:
        st.session_state.name = name
        st.session_state.page = "skill"
        st.rerun()

elif st.session_state.page == "skill":

    st.markdown(f"## Welcome, {st.session_state.name} 💙")

    level = st.selectbox("📊 Choose your level", ["Beginner", "Intermediate"])
    st.session_state.level = level

    skills = {
        "Coding":"Apps, AI tools, websites",
        "Graphic Design":"Logos, branding, UI",
        "Video Editing":"Reels, YouTube, films",
        "Writing":"Blogs, scripts, copy",
        "Trading":"Markets, finance, strategy",
        "Music Skills":"Beats, production, sound",
        "Others":"Your own special skill"
    }

    cols = st.columns(3)
    for i,(s,d) in enumerate(skills.items()):
        with cols[i%3]:
            st.markdown(f"<div class='skill'><b>{s}</b><br><span class='tag'>{d}</span></div>", unsafe_allow_html=True)
            if st.button(f"Select {s}"):
                st.session_state.skill = s
                st.session_state.page = "roadmap"
                st.rerun()


elif st.session_state.page == "roadmap":

    skill = st.session_state.skill
    level = st.session_state.level

    if st.button("🤍 Add to favourites"):
        if skill not in st.session_state.favourites:
            st.session_state.favourites.append(skill)

    roadmaps = {
        "Coding":{
            "learn":["Python basics","Projects & GitHub","AI & Web apps"],
            "youtube":[
                ("Python Full Course","https://www.youtube.com/watch?v=rfscVS0vtbw"),
                ("Build Projects","https://www.youtube.com/watch?v=8ext9G7xspg"),
                ("AI tools","https://www.youtube.com/watch?v=5MgBikgcWnY")
            ],
            "money":[("Fiverr","https://fiverr.com"),("Upwork","https://upwork.com"),("Internshala","https://internshala.com")],
            "career":["Software Developer","AI Engineer","Startup Founder"]
        },
        "Graphic Design":{
            "learn":["Canva & Photoshop","Brand projects","Portfolio"],
            "youtube":[
                ("Design basics","https://www.youtube.com/watch?v=3GzumUieDPY"),
                ("Photoshop guide","https://www.youtube.com/watch?v=IyR_uYsRdPs"),
                ("Logo design","https://www.youtube.com/watch?v=8C4lK41SX-Q")
            ],
            "money":[("99designs","https://99designs.com"),("Fiverr","https://fiverr.com"),("Canva","https://canva.com")],
            "career":["UI/UX Designer","Brand Strategist","Creative Director"]
        },
        "Video Editing":{
            "learn":["CapCut & Premiere","Short-form mastery","Client workflow"],
            "youtube":[
                ("CapCut editing","https://www.youtube.com/watch?v=3VY8pXfR7rE"),
                ("Premiere pro","https://www.youtube.com/watch?v=1-s2B9pN3rE"),
                ("YouTube edits","https://www.youtube.com/watch?v=O6ERELse_QY")
            ],
            "money":[("Fiverr","https://fiverr.com"),("Upwork","https://upwork.com"),("YouTube jobs","https://youtube.com")],
            "career":["Video Producer","Film Editor","Content Head"]
        },
        "Writing":{
            "learn":["SEO basics","Blog & copy","Personal brand"],
            "youtube":[
                ("SEO writing","https://www.youtube.com/watch?v=hF515-0Tduk"),
                ("Copywriting","https://www.youtube.com/watch?v=mWNYE5yVOzk"),
                ("Blogging","https://www.youtube.com/watch?v=7pH7R1v3K7A")
            ],
            "money":[("Medium","https://medium.com"),("PepperContent","https://peppercontent.io"),("Fiverr","https://fiverr.com")],
            "career":["Content Strategist","Author","Marketing Lead"]
        }
    }

    data = roadmaps.get(skill, roadmaps["Coding"])

    st.markdown(f"## 🎯 {skill} Roadmap ({level})")

    st.markdown("### 🛣 Skill Path")
    for i in data["learn"]:
        st.markdown("✅ "+i)

    st.markdown("### 📺 YouTube Resources")
    for title,link in data["youtube"]:
        st.markdown(f"🔗 [{title}]({link})")

    st.markdown("### 💰 Monetization Platforms")
    for name,link in data["money"]:
        st.markdown(f"💼 [{name}]({link})")

    st.markdown("### 🎓 Career Guide")
    for c in data["career"]:
        st.markdown("🚀 "+c)

    st.session_state.roadmap_text = f"{skill} - {level}\n{data}"

    if st.button("Continue"):
        st.session_state.page = "final"
        st.rerun()

elif st.session_state.page == "final":

    st.success("🎉 Your journey has started.")
    st.markdown("## 🚀 Your independence begins the moment you take action.")

    comment = st.text_area("💬 Leave a comment")

    colx,coly = st.columns([8,2])
    with coly:
        if st.button("Submit"):
            st.session_state.submitted = True

    if st.session_state.get("submitted"):
        st.markdown("<div class='popup'>✅ Response submitted successfully</div>", unsafe_allow_html=True)
        if st.button("OK"):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()

    st.markdown("## 🌐 Other skills you might like")

    c1,c2 = st.columns(2)
    with c1:
        st.markdown("### **Technical Skills**")
        for s in ["AI","Web Development","App Development","Cyber Security","Data Science","Game Dev","Cloud","Robotics","Blockchain","IoT"]:
            st.markdown(f"<div class='skill-list'>{s}</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("### **Non-Technical Skills**")
        for s in ["Public Speaking","Marketing","Psychology","Teaching","Design","Business","Finance","Video Creation","Music","Entrepreneurship"]:
            st.markdown(f"<div class='skill-list'>{s}</div>", unsafe_allow_html=True)

    st.download_button("📥 Download roadmap", st.session_state.roadmap_text, file_name="independo_roadmap.txt")

    carousel("60vh")