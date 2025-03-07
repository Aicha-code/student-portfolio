import streamlit as st
import urllib.parse

st.set_page_config(page_title="Aichetou ABARI | AI & Software Engineer", page_icon="🎓")
# sidebar navigation
st.sidebar.title("📌 navigation")
page = st.sidebar.radio("Go To", ["Home", "projects", "Skills & achievements", "Contact", "Edit profile"])


#Session initialization:
if 'location' not in st.session_state:
    st.session_state.location= "Musanze"
if 'formation' not in st.session_state:
    st.session_state.formation= "BSc Computer Science, Year 3, option: Software Engineering💻"
if 'university' not in st.session_state:
    st.session_state.university="INES Ruhengeri"
if 'about_me' not in st.session_state:
    st.session_state.about_me="I am an AI enthusiast, passionate about our ability to create solutions to real-world problems and challenges using technology and artificial intelligence. I am particularly fascinated by building systems that have human-like responses and functions. I am a rigorous worker, almost a perfectionist, and I look forward to becoming a software engineer."

# Home section
if page == "Home":
    st.title("Personal Profile 👩🏽‍💻")
    col1, col2 = st.columns([1, 2])  # Left column (2/3 width) and Right column (1/3 width)

    # Profile Image on the Side
    with col1:
        st.image("myProfile_picture.jpg", width=250, caption="Aichetou Abari Ilior", use_container_width=True)

    with col2:
        name = st.text_input("Name:", "ABARI ILIOR Aichetou")
        st.text_input("Location:", f"{st.session_state.location}")
        st.text_input("Formation:", f"{st.session_state.formation}")
        st.text_input("University:", f"{st.session_state.university}")
    st.write(f"📍 {st.session_state.location} | 📚 {st.session_state.formation} | 🎓 {st.session_state.university}")

    # Resume Download Button
    st.subheader("Click the button below to download my resume")
    with open('resume.pdf', 'rb') as file:
         resume_bytes = file.read()
    st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume.pdf", mime="application/pdf")

    st.markdown('----')
    st.subheader("About Me")
    st.markdown(
        f"""
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); text-align: justify;">
            {st.session_state.about_me}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Testimonials Section
    #st.header(" Testimonials")
    st.subheader("🗣️ What People Say About Me")
    def display_testimonial(author, text):
        st.markdown(
            f"""
            <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; 
                        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); text-align: center; 
                        max-width: 700px; margin: 15px auto;">
                <div style="font-size: 18px; font-weight: bold; color: #2b7a78; margin-bottom: 5px;">{author}</div>
                <p style="font-style: italic; color: #555; background-color: #f8f9fa; padding: 10px; border-radius: 8px;">"{text}"</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    display_testimonial("Abesolo Flora", "Aichetou is one of the most dedicated and hardworking people I know. She is always ready to help, share advice, and uplift those around her. Her determination and attention to detail make her an inspiring classmate to work with.")
    display_testimonial("Emanuel Ntamack", "Aichetou is a highly motivated and detail-oriented student with a strong passion for AI and software engineering. She consistently demonstrates dedication and excellence in her academic projects")


# pprojects section
elif page=="projects":
        st.title("My Projects 👩🏽‍💻")
        projects = [
        {
            "title": "Rwd-Travel Agency",
            "type": "Group Project",
            "description": "A travel agency webApp built using HTML, CSS, JS, Flask, SQL, and tkinter.",
            "details": "The Rwd-Travel website provides a seamless platform for travelers to book activities, flights, and accommodations while exploring Rwanda’s rich cultural heritage.",
            "report": "Rw_Travel_Technicalreport.pdf",
            "download_label": "📄 Download Report"

        },

        {
            "title": "Student Management System",
            "type": "Class Project",
            "description": "A desktop Application developed using .NET with WinForm and an SQLite database.",
            "details": "The system is a student management system application (SMS) whose core features are its ability to communicate with a database and allow the user to perform CRUD operations.",
            "github": [

                "https://github.com/Aicha-code/Student-Management-System-with-.NET-DesktopApp-",
                "https://github.com/Aicha-code/Student-management-System-with-.NET"

            ]

        },

        {

            "title": "Plagiarism Proctor",
            "type": "Individual Project",
            "description": "This is my final year project on the topic 'Machine Learning-Based Similarities Checker System for Enhancing Examination Quality in Academic Institutions'.",
            "details": "I am thrilled to be working on it and will be posting about it soon, stay tuned to know more...",
            "report": "PLAGIARISM_PROCTOR.pdf",
            "download_label": "📄 Download SNEEKPEAK"

        }

    ]
        
         # Filter options
        project_types = list(set(project["type"] for project in projects))
        selected_type = st.selectbox("Select project type to filter:", ["All"] + project_types)

        # Display projects based on selected type
        for project in projects:
            if selected_type == "All" or project["type"] == selected_type:
                with st.expander(f"{project['title']} | type: {project['type']}"):
                    st.write(project["description"])
                    st.markdown(project["details"])
                    # Download button if report exists
                    if "report" in project:

                        with open(project["report"], 'rb') as file:
                            report_bytes = file.read()
                            st.download_button(
                                label=project["download_label"],
                                data=report_bytes,
                                file_name=project["report"],
                                mime="application/pdf",
                                key=f"download_{project['title'].replace(' ', '_')}"  # Unique key for each button
                            )
                    # GitHub links if they exist

                    if "github" in project:
                        for link in project["github"]:
                            st.markdown(f"🖇️ [GitHub Repository]({link})")


#skills section
elif page =="Skills & achievements":
    st.title("💻Skils and archievements ")
    st.subheader("Programming languages")
    skill_python = st.slider("python", 0,100,75)
    skill_js = st.slider("Javascript", 0,100,55)
    st.progress(skill_python)

    st.subheader("Machine Learning / Data Science")
    skill_AI = st.slider("Artificial Intelligence", 0,100,70)
    skill_DA = st.slider("Data Analytics", 0,100,55)
    st.progress(skill_AI)

    st.subheader("Web Development")
    skill_AI = st.slider("HTML", 0,100,90)
    skill_AI = st.slider("CSS", 0,100,95)
    skill_AI = st.slider("JS", 0,100,55)
    st.progress(skill_python)
    
    st.subheader("Certifcates & Archievements")
    st.write("✔Completed AI&ML in business Certification")
    st.write("✔Completed AI in Research Certification")
    st.write("✔Completed CS50P")

#customize profile page
elif page == "Edit profile":
    st.title("🎨 Edit Your Profile")
    
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        
        .section-title {
            font-size: 24px;
            font-weight: bold;
            color: #ff6b6b;
            text-align: center;
            margin: auto;
            background-color: #ffffff;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.1);
            width: 60%;
        }
        .update-button {
            background-color: #ff6b6b;
            color: white;
            font-weight: bold;
            padding: 12px;
            border-radius: 8px;
            border: none;
            transition: 0.3s;
            width: 100%;
            font-size: 16px;
            cursor: pointer;
            display: block;
            text-align: center;
        }
        .update-button:hover {
            background-color: #ff4757;
            transform: scale(1.05);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Profile Editing Form Inside a Box
    #st.markdown('<div class="cute-box">', unsafe_allow_html=True)
    
    st.markdown('<p class="section-title, cute-box">✨ Edit Your Informations ✨</p>', unsafe_allow_html=True)
    
    with st.form("edit_profile_form"):
        location = st.text_input("📍 Location:", st.session_state.location)
        about_me = st.text_area("💬 Bio:", st.session_state.about_me, height=100)
        formation = st.text_input("🎓 Formation:", st.session_state.formation)
        university = st.text_input("🏫 University:", st.session_state.university)

        # Submit button inside the box
        submitted = st.form_submit_button("🚀 Update Info")
        if submitted:
            # Update session state with new values
            st.session_state.location = location
            st.session_state.formation = formation
            st.session_state.about_me = about_me
            st.session_state.university = university
            st.success("✅ Information updated successfully!")

    st.markdown('</div>', unsafe_allow_html=True)

#contact page
elif page == "Contact":
    st.title("📞 Contact Me")

    # Contact Form
    with st.form("Contact Form"):
        st.subheader("📬 Get in Touch")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Write Your Message Here")
        
        submit_button = st.form_submit_button("📩 Send Message")
        if submit_button:
            if name and email and message:
                # Generate the mailto link
                recipient_email = "ug2321291@ines.ac.rw"
                subject = f"Portfolio Inquiry from {name}"
                body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                
                mailto_link = f"mailto:{recipient_email}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"

                # Open the mail client
                st.markdown(f'<meta http-equiv="refresh" content="0; url={mailto_link}">', unsafe_allow_html=True)
            else:
                st.warning("⚠️ Please fill in all the fields before sending.")

    # Contact Information Section with Styling
    st.markdown("""
    <style>
        .contact-box {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-top: 20px;
        }
        .contact-box a {
            text-decoration: none;
            font-weight: bold;
            color: #2b7a78;
        }
        a:hover{
                color: black;
        }
        .contact-box p {
            font-size: 16px;
            margin: 5px 0;
        }
    </style>
    <div class="contact-box">
        <p>☎️ <strong>Phone:</strong> +241 655 685 68 | 📧 <strong>Email:</strong> <a href="mailto:ug2321291@ines.ac.rw">ug2321291@ines.ac.rw</a></p>
        <p>🔗 <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/a%C3%AFchetou-abari-ilior-317449296/" target="_blank">Click Here</a> | 💻 <strong>GitHub:</strong> <a href="https://github.com/Aicha-code" target="_blank">Click Here</a>
        | 🌐 <strong>Portfolio:</strong> <a href="https://student-portfolio-5u8dxcmcod4a2vev4vgdqe.streamlit.app/" target="_blank">Visit My Website</a></p>
    </div>
    """, unsafe_allow_html=True)


st.sidebar.write("----")
st.sidebar.write("© ABARI ILIOR Aichetou March 2025")
