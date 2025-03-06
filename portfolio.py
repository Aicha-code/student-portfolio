import streamlit as st

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
    st.session_state.university=st.text_input("University: ", "INES Ruhengeri")
if 'about_me' not in st.session_state:
    st.session_state.about_me="I am an AI enthusiast, passionate about our ability to create solutions to real-world problems and challenges using technology and artificial intelligence. I am particularly fascinated by building systems that have human-like responses and functions. I am a rigorous worker, almost a perfectionist, and I look forward to becoming a software engineer."

# Home section
if page == "Home":
    st.title("Personal Profile 👩🏽‍💻")
    # profile image
    st.image("myProfile_picture.jpg", width=150, caption="Aichetou Abari Ilior")
    #my details
    
    name=st.text_input("Name: ", "ABARI ILIOR Aichetou")
    st.text_input(f"Location: {st.session_state.location}")
    st.text_input(f"formation: {st.session_state.formation}")
    st.text_input(f"university: {st.session_state.university}")
    st.write(f"📍{st.session_state.location} | 📚{st.session_state.formation} | 🎓{st.session_state.university}")
    
    #resume download button
    st.subheader("click the button below to download my resume")
    with open('resume.pdf', 'rb') as file:
        resume_bytes=file.read()
    st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume.pdf",mime="application/pdf")
    st.markdown('----')
    st.write("About Me")
    st.markdown(st.session_state.about_me)

    # Testimonials Section
    st.header("🗣️Testimonials")
    st.subheader("What People Say About Me")

    # Testimonial from Abesolo 
    with st.container():
        st.markdown("**Abesolo Flora**")
        st.write('"She\'s one of the most inspiring student I have met, a very nice classmate and friend."')


    # Testimonial from Emanuel Nsengiyumva

    with st.container():

        st.markdown("**Emanuel Ntamack**")
        st.write('"One of the most serious students of this promotion."')

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
    skill_python = st.slider("python", 0,100,90)
    skill_js = st.slider("Javascript", 0,100,75)
    st.progress(skill_python)

    st.subheader("Machine Learning / Data Science")
    skill_AI = st.slider("Artificial Intelligence", 0,100,65)
    skill_AI = st.slider("Data Analytics", 0,100,55)
    st.progress(skill_python)

    st.subheader("Web Development")
    skill_AI = st.slider("HTML", 0,100,90)
    skill_AI = st.slider("CSS", 0,100,93)
    skill_AI = st.slider("JS", 0,100,60)
    st.progress(skill_python)
    
    st.subheader("Certifcates & Archievements")
    st.write("✔Completed AI&ML in business Certification")
    st.write("✔Completed AI in Research Certification")
    st.write("✔Completed CS50P")

#customize profile page
elif page=="Edit profile":
    st.title("✍Customize your profile")
    st.subheader("upload a profile picture")
    uploaded_image = st.file_uploader(
        "uploaded profile picture", type=["jpeg", "png", "jpg"]
    )
    if uploaded_image is not None:
        st.image(uploaded_image, width=150, caption="")
    st.subheader("Edit your profile information")
    name = st.text_input("Name: ")
    location = st.text_input("Enter your location:", st.session_state.location)
    about_me = st.text_input("Enter your bio:", st.session_state.about_me)
    formation = st.text_input("Enter your formation:", st.session_state.formation)
    university = st.text_input("Enter your university:", st.session_state.university)
    
    if st.button("Update Info"):
        # Update session state with new values
        st.session_state.location = location
        st.session_state.formation = formation
        st.session_state.about_me = about_me
        st.session_state.university = university
        st.success("Information updated successfully!")

#contact page
elif page=="Contact":
    st.title("📞Contact Me")
    with st.form("Contact Form"):
        name = st.text_input("Your name")
        email = st.text_input("your Email")
        message = st.text_input("Write your message here")
        submit_button= st.form_submit_button("send")
        if submit_button:
            st.success("✅Message sent successfully")
        st.write("☎️phone: +24165568568")
        st.write("📧Email: ug2321291@ines.ac.rw")
        st.write("linkedin (https://www.linkedin.com/in/a%C3%AFchetou-abari-ilior-317449296/)")
        st.write("github (https://github.com/Aicha-code)")
        st.write("Portfolio Website (https...)")


st.sidebar.write("----")
st.sidebar.write("© ABARI ILIOR Aichetou March 2025")
