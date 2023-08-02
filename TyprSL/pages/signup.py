import streamlit as st
from streamlit_extras.switch_page_button import switch_page



#-----------------------
# Pages / Sidebar Config
#-----------------------
st.set_page_config(page_title="Typr - Sign Up",
                   page_icon=":paper:",
                   initial_sidebar_state="collapsed",
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




#----------------------
# Inital Page Setup
#----------------------
st.markdown("# Signup :paper:")
st.divider()