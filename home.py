import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Pavel Kim Portfolio",
    page_icon="📊",
)


def home_page():
    # ----- Left menu -----
    with st.sidebar:
        st.image("C:/Users/chere/OneDrive/Desktop/IPLDEAE/eae_ipld_project/eae_img.png", width=200)
        st.header("Introduction to Programming Languages for Data")
        st.write("###")
        st.write("***Final Project - Feb 2025***")
        st.write("**Author:** Pavel Kim")
        st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


    # ----- Top title -----
    st.html("""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Pavel Kim</h1></div>""")


    # ----- Profile image file -----
    profile_image_file_path = "C:/Users/chere/OneDrive/Desktop/IPLDEAE/eae_ipld_project/profile.png"

    with open(profile_image_file_path, "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


    # ----- Your Profile Image -----
    st.html(f"""
    <div style="display: flex; justify-content: center;">
        <img src="{img}" alt="Pavel Kim" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    </div>
    """)


    # ----- Personal title or short description -----
    current_role = "Student at EAE Business School"

    st.html(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""")

    st.write("##")


    # ----- About me section -----
    st.subheader("About Me")

    # TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
    st.write("""
    - 🧑‍💻 I am a student

    - 🛩️ prev: Economics bachelor, data analyst experience

    - ❤️ Education

    - 🤖 This one

    - 🏂 Skis

    - 📫 How to reach me: 4erepasha02@gmail.comm

    - 🏠 Barcelona
    """)

    # Feel free to add other points like your Linkedin, Github, Social Media, etc.


# This is ensambling the entire app with the different pages and the navigation menu
pg = st.navigation([
    st.Page(home_page, title="Home", icon="👋"),
    st.Page("C:/Users/chere/OneDrive/Desktop/IPLDEAE/eae_ipld_project/development/01_image_cropper.py", title="Image Cropper", icon="🖼️"),
    st.Page("C:/Users/chere/OneDrive/Desktop/IPLDEAE/eae_ipld_project/development/02_netflix_data_analysis.py", title="Netflix Data Analysis", icon="🎬"),
    st.Page("C:/Users/chere/OneDrive/Desktop/IPLDEAE/eae_ipld_project/development/03_temperatures_dashboard.py", title="Temperatures Dashboard", icon="🌦️"),
])
pg.run()