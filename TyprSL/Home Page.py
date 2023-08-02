#--------
# Imports
#--------
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain



#------------------------
# Init Loading Properties
#------------------------
st.set_page_config(page_title="Typr - Home Page",
                   page_icon=":Keyboard:",
                   initial_sidebar_state="collapsed",
                   layout="centered",
                   menu_items={
                       'About':  

"""# Typr - About Me

Typr was built as my final High-School CS Project. It is
was made to make learning touch typing a less daunting
task.

I personally learned it with some struggles and would have
loved to have a service like this :)

I hope you enjoy using it!"""
    })




#---------------------
# Webpage Header Image
#---------------------
left_co, cent_co,last_co = st.columns(3)

with cent_co:
    st.image("images/Astro_Typing.png", output_format="PNG")

#--------------
# Title Section
#--------------
st.title("Typr")
st.header("Your Personal Typing Tutor :keyboard:.")

# Section Break
st.divider()

#---------------------
# Login / Start Button
#---------------------
topStartButton = st.button(":blue[Start Now] :rocket:",
                           use_container_width=True)

# typing test redirect button logic
if topStartButton:
    switch_page("signup")



#--------------
# Hero Statement
#---------------
st.subheader("Why Use Typr?")


st.markdown("In an era driven by efficient communication and productivity, the mastery of touch typing has become paramount. Enter ___Typr___, an innovative website poised to revolutionize your typing skills. Through immersive interactive lessons and advanced visual feedback, Typr empowers professionals, academia students, & more to unlock their full typing potential like never before!", unsafe_allow_html=True)


st.image("images/Red_Keyboard.jpg", use_column_width="always")


st.subheader("1. Elevate Your Professional Profile")

st.markdown("In the competitive landscape of professionals and academia, possessing impeccable typing skills sets you apart from the rest. With Typr as your trusted companion, bid farewell to the inefficiencies of the hunt-and-peck method, and embrace the realm of touch typing expertise. Enhance your professional profile, boost productivity, and amplify your success with the unrivaled typing proficiency achieved through Typr.")


st.image("images/Computer_Learning.jpg", use_column_width="always")


st.subheader("2. Immersive Interactive Lessons")

st.markdown("Typr offers a transformative learning experience that immerses you in a world of interactive lessons specifically designed for professionals and academia students. Seamlessly blending theory with practice, Typr guides you through a comprehensive curriculum, ensuring a holistic grasp of touch typing fundamentals. Prepare to witness remarkable progress as you engage with immersive exercises, honing your skills under Typr's expert guidance.")


st.image("images/Typing_On_Screen.jpg", use_column_width="always")


st.subheader("3. Advanced Visual Feedback Mechanisms")

st.markdown("At Typr, we understand that visual feedback is a catalyst for growth and improvement. Our state-of-the-art platform provides real-time visual emulation of your typing actions, enabling you to observe your performance with exceptional clarity. From keystroke accuracy to typing speed, every nuance of your progress is meticulously showcased, allowing you to fine-tune your skills and reach new heights of typing proficiency.")



#------
# Pages
#------
st.sidebar.markdown("# Home Page")


#---------
# Page VFX (EXPERIMENTAL)
#---------
rain(emoji="*", font_size=50, falling_speed=20, animation_length="infinite")
