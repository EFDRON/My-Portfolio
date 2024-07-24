import streamlit as st
import pandas as pd
import google.generativeai as genai
import time
from streamlit_option_menu import option_menu
import os

api_key=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')



def text_generator(text):
    # response = "Sanadek is a user-friendly geospatial data platform designed to make complex data accessible and actionable. Through interactive maps, charts, and graphs, users can explore datasets with ease, uncovering trends and patterns that drive informed decision-making."
    for word in text.split():
        yield word + " "
        time.sleep(0.05)



def main():
    global response
    i = 0
    st.set_page_config(
        page_title="Personal Portfolio",
        page_icon="images/logo.png",
        layout="wide",
        initial_sidebar_state="expanded")
    c1,c2,c3=st.columns([1,3,1])
    #c2.image("images/cv.jpeg")

    st.markdown("""
    <style>
    .st-emotion-cache-1p1m4ay.e3g6aar0{
        visibility: hidden;
    }
    .st-emotion-cache-czk5ss.e16jpq800{
        visibility: hidden;
    }

    .styles_terminalButton__JBj5T{
        visibility: hidden;
    
    }
    .viewerBadge_container__r5tak styles_viewerBadge__CvC9N{
        visibility: hidden;
        
    }
    .st-emotion-cache-h4xjwg.ezrtsby2{
        height: 0rem;
    }
    .st-emotion-cache-1jicfl2 {
        width: 100%;
        
        padding-top: 0rem;
        padding-right: 1rem;
        padding-bottom: 10rem;
        padding-left: 1rem;
        min-width: auto;
        max-width: initial;
}

    .st-emotion-cache-7tauuy {
        width: 100%;
        padding-top: 0rem;
        padding-right: 1rem;
        padding-bottom: 1rem;

        min-width: auto;
        max-width: initial;
}

    .st-emotion-cache-ocqkz7 {
        display: flex;
        flex-wrap: wrap;
        flex-grow: 1;
        align-items: stretch;
        gap: 1rem;
    }

 


    .st-emotion-cache-ocqkz7 img {
        width: 300px;
        height: 200px;
        object-fit: cover;
        border-radius: 5px;
}

    .st-emotion-cache-ocqkz7 {
    display: flex;
    flex-wrap: wrap;
    flex-grow: 1;
    align-items: self-end;
    gap: 1rem;
}
    
    
    </style>
    """, unsafe_allow_html=True)

    if "status" not in st.session_state:
        st.session_state.status="Home"

    selected = option_menu(menu_title=None,
                           options=["Me", "Projects", "Ask AI","Contact Me"],
                           icons=["person-vcard", "book", "robot","chat-dots"],
                           orientation="horizontal"
                           )
    if selected=="Me":

        col1, col2 = st.columns(2)
        with col1:
            st.subheader(" ")
            st.subheader(" ")
            st.subheader("Hi :wave:")
            st.title("I am Efa Kedir ")
            st.text("Electrical Engineering Student,")
            st.text("Higher College Of Technology(HCT)")
            st.text("UAE")


        with col2:
            st.image("images/profile3.png")
            # Define the CSS for the hover effect

            # Inject the CSS into the Streamlit app
            st.markdown("""
    <style>
    img {
        cursor: pointer;
        transition: all .3s ease-in-out;
    }
    img:hover {
        transform: scale(1.1);
    }
    </style>
    """, unsafe_allow_html=True)




        st.write("")  # Add a single line of space
        st.write("")  # Add a single line of space
        st.title("My Skills")
        st.write("Programming")
        st.progress(70)
        st.write("Computer Vision")
        st.progress(60)
        st.write("Arduino")
        st.progress(60)
        st.write("Communication")
        st.progress(85)
        st.write("Leadership")
        st.progress(85)



        st.write("")  # Add a single line of space
        st.write("")  # Add a single line of space

    elif selected=="Projects":
        image_path=[]
        for i in range(6):
            image_path.append(f"images/p{i+1}.jpeg")


        st.title("Computer Vision Projects")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(image_path[0])
            st.write("Face Detection")
            st.image(image_path[1])
            st.write("Object Detection & Recognition")
            st.markdown("""
               <style>
               img {
                   cursor: pointer;
                   transition: all .3s ease-in-out;
               }
               img:hover {
                   transform: scale(1.1);
               }
               </style>
               """, unsafe_allow_html=True)
        with col2:
            st.image(image_path[2])
            st.write("Object Tracking")
            st.image(image_path[3])
            st.write("Pose Estimation")
        with col3:
            st.image(image_path[4])
            st.write("Face Mesh & Application")
            st.image(image_path[5])
            st.write("Face Recognition")




    elif selected=="Ask AI":

        persona="""
        You are Efa Kedir AI bot. You help people answer questions about Efa Kedir.
        Answer as if you are responding directly. If you don't know the answer, simply say "That's a secret."If you are asked who created you simply say i was created by Efa kedir.

        Efa Kedir is currently an electrical engineering student at Higher College of Technology in Sharjah, UAE. He is passionate about computer vision, AI, robotics, and embedded systems.
        Efa has completed several impactful computer vision projects including face detection and recognition,object detection and reognition,pose estimationo and object tracking that have honed his skills in the field. 
        Known for his strong programming, communication, and leadership abilities, Efa showcased his talents by securing a top ten position in the UAE hackathon. 

        Efa Kedir's Social Media:
        YouTube: http://www.youtube.com/@efakedir955
        LinkedIn: https://www.linkedin.com/in/efa-kedir-534bbb2aa
        Email: efakedir1@gmail.com

        """
        if "messages" not in st.session_state:
            st.session_state.messages = []
            # st.session_state.chat_engine = chat_engine
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
            # st.chat_message(msg["role"]).write(msg["content"])
        if prompt := st.chat_input("please enter your prompt"):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            response=model.generate_content(persona+'Here is the question:'+prompt)
            with st.chat_message("assistant"):
                # response = prompt_engine.chat(prompt)
                st.write_stream(text_generator(response.text))
                st.session_state.messages.append({"role": "assistant", "content": response.text})


    elif selected == "Contact Me":
        st.markdown(
            """
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css">
            """,
            unsafe_allow_html=True,
        )

        st.title("My Contatcts")
        st.markdown(
            """
            <h2>
                <i class="bi bi-linkedin" style="font-size: 1.2em;"></i>
                <a href="https://www.linkedin.com/in/efa-kedir-534bbb2aa" target="_blank">LinkedIn: efa-kedir-534bbb2aa</a>
            </h2>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <h2>
                <i class="bi bi-envelope-fill" style="font-size: 1.2em;"></i>
                <a href="mailto:efakedir1@gmail.com">Email: efakedir1@gmail.com</a>
            </h2>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <h2>
                <i class="bi bi-instagram" style="font-size: 1.2em;"></i>
                <a href="https://www.instagram.com/efkd_12?igsh=MXJ4djBzcWMxMzZjMQ==" target="_blank">Instagram: efkd_12</a>
            </h2>
            """,
            unsafe_allow_html=True,
        )

        # Telegram Contact
        st.markdown(
            """
            <h2>
                <i class="bi bi-telegram" style="font-size: 1.2em;"></i>
                <a href="https://t.me/efdron_12" target="_blank">Telegram: efdron_12</a>
            </h2>
            """,
            unsafe_allow_html=True,
        )

        #YouTube

        st.markdown(
            """
            <h2>
                <i class="bi bi-youtube" style="font-size: 1.2em;"></i>
                <a href="https://youtube.com/@efakedir955?si=8xbQcgQ66ntN6jPe" target="_blank">YouTube: @efakedir955</a>
            </h2>
            """,
            unsafe_allow_html=True,
        )



if __name__ == '__main__':
    main()


