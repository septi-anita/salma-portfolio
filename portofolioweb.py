import streamlit as st

# Custom CSS for styling with new color palette
st.markdown(
    """
    <style>
    /* General styling */
    body {
        background-color: #f123f13; /* Soft grey */
    }

    /* Background Landing Page */
    .bg-lp {
        background-color: #262b44; /* White for contrast */
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1);
        margin: 0px 0;
        transition: transform 0.2s ease;
    }

    /* Title landing page styling */
    .title-lp {
        font-size: 50px;
        font-weight: bold;
        color: #ffffff; /* Dark lavender */
        text-align: center;
        margin-top: 110px;
    }

    /* Title styling */
    .title-text {
        font-size: 50px;
        font-weight: bold;
        color: #262b44; /* Dark lavender */
        text-align: center;
        margin-top: 110px;
    }

    /* Subtitle styling */
    .subtitle-text {
        font-size: 20px;
        color: #7c84e4; /* Dark lavender */
        text-align: center;
        margin-bottom: 200px;
    }

    /* Card Styling */
    .card {
        background-color: #7c84e4; /* White for contrast */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
        transition: transform 0.2s ease;
    }

    .card:hover {
        transform: translateY(-10px); /* Card hover effect */
    }

    .card-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #ffffff; /* Calming green */
    }

    .card-description {
        font-size: 16px;
        color: #262b44; /* Dark teal */
        margin-bottom: 10px;
    }

    .button {
        background-color: #262b44; /* Peach */
        color: white;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }

    .button:hover {
        background-color: #eaeaea  ; /* Darker peach on hover */
    }

    /* Contact styling */
    .contact-text {
        font-size: 18px;
        color: #264653; /* Dark teal */
        text-align: center;
        margin-top: 50px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Function to display the landing page
def landing_page():
    st.markdown(
        """
        <div class="bg-lp">
            <h1 class="title-lp" id="landing-page">Hi, I’m Sallima Sylvie Septianita</h1>
            <p class="subtitle-text">I’m a Physics graduate with a passion for data and technology.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
#    st.markdown('<h1 class="title-text" id="landing-page">Hi, I’m Sallima Sylvie Septianita</h1>', unsafe_allow_html=True)
#    st.markdown('<p class="subtitle-text">I’m a Physics graduate with a passion for data and technology.</p>', unsafe_allow_html=True)

# Function to display the about me page
def about_me_page():
    st.markdown('<h1 class="title-text" id="about-me">About Me</h1>', unsafe_allow_html=True)
    about_me_text = """
        I’m Salma, a Physics graduate from Universitas Brawijaya. During my studies, I focused on computational physics, 
        where I worked on various projects involving programming and modeling. Recently, I have developed a strong interest 
        in data and am currently deepening my knowledge while building new projects. Here are some of the projects.
    """
    st.markdown(f'<p class="subtitle-text">{about_me_text}</p>', unsafe_allow_html=True)

# Function to display the projects page
def projects_page():
    st.markdown('<h1 class="title-text" id="projects">Projects</h1>', unsafe_allow_html=True)
    
    # Project 1: Program Jadwal Sholat
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Program Jadwal Sholat</div>
            <div class="card-description">A program designed to calculate prayer times for various regions in Indonesia, 
            using data such as the sun's position, geographical location, and other relevant factors to ensure accurate results.</div>
            <a href="https://lonelylov-program-sholat-programsholat-d0cn3z.streamlit.app/" class="button">View Project</a>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Project 2: CT Simulator
    st.markdown(
        """
        <div class="card">
            <div class="card-title">CT Simulator</div>
            <div class="card-description">A first-generation CT scan simulator with a modified data acquisition system that applies 
            linear interpolation to optimize dose efficiency.</div>
            <a href="https://ctsimulatorbysallimaseptianita.streamlit.app/" class="button">View Project</a>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Project 3: Titanic
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Titanic: Who Survived?</div>
            <div class="card-description">A project aimed at predicting the likelihood of passenger survival in the Titanic disaster 
            based on specific criteria and data analysis.</div>
            <a class="button" style="pointer-events: none; opacity: 0.5;">Coming Soon</a>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Function to display the contact page
def contact_page():
    st.markdown('<h1 class="title-text" id="contact">Contact</h1>', unsafe_allow_html=True)
    st.markdown('<p class="contact-text">Email: <a href="mailto:septianita165@gmail.com">septianita165@gmail.com</a></p>', unsafe_allow_html=True)
    st.markdown('<p class="contact-text">LinkedIn: <a href="https://www.linkedin.com/in/sallima-sylvie-septianita/" target="_blank">Sallima Sylvie Septianita</a></p>', unsafe_allow_html=True)

# Display all sections in one page
landing_page()
about_me_page()
projects_page()
contact_page()
