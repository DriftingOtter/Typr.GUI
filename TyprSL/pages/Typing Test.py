import streamlit as st
from st_keyup import st_keyup
import string
import random
import time
import threading



#---------------------------------
# Random Challenge Text Generation
#---------------------------------
def generateChallengeText(numOfWords):

    wordList = "C:\\Users\\ShameFul\\Documents\\Typr\\WordLists\\Loki_Word_List_EN.txt" # Change To OS BASED PATH
    challengeText = []

    with open(wordList, "r") as currentText:
        lines = currentText.readlines()
        
    numLines = len(lines)

    for words in range(numOfWords):
        randomLineGen = random.randint(0, numLines - 1)
        challengeText.append(lines[randomLineGen].strip())

    return challengeText


def conv_LTS(lst): # Converts The Generated ChallengeText List -> String
    strText = " ".join([str(elem) for elem in lst])
    strText = strText.translate({ord(c): " " for c in string.whitespace})

    return str(strText)


def load_ChallengeText():
    # Initializes a empty string in session state
    if "internalText" not in st.session_state:
        st.session_state.internalText = ""

    # Check if Cached Challenge Text (aka. internalText)
    if not st.session_state.internalText:
        st.session_state.internalText = conv_LTS(generateChallengeText(10))


def check_completion(user_text):
    if st.session_state.internalText and user_text:
        internal_words = st.session_state.internalText.split()
        user_words = user_text.split()

        if len(internal_words) == len(user_words):

            for i in range(len(internal_words)):

                if internal_words[i] != user_words[i]:
                    return False

            return True

    return False


def retry_Submit_Logic(): # For Checking If the Usr Wants to Retry Or Submit Ans

    global usrAns, progress, progressionBar

    if retryButton:
        challengeText.empty()
        st.session_state.internalText = conv_LTS(generateChallengeText(10))

        usrAns = ""

        progressionBar = st.empty()
        progress = 0

        check_completion_progress(usrAns)

    else:
        if usrAns:
            if len(usrAns) != len(st.session_state.internalText): #type: ignore
                st.toast("You Failed!")
                progressionBar = st.empty()

                progressionBar = st.empty()
                progress = 0

            else:
                if check_completion(usrAns):
                    st.toast("You Did it!")

                    progressionBar = st.empty()

                    progressionBar = st.empty()
                    progress = 0
                else:
                    st.toast("You Failed!")

                    progressionBar = st.empty()
                
                    progressionBar = st.empty()
                    progress = 0

                challengeText.empty()
                st.session_state.internalText = conv_LTS(generateChallengeText(10))
                usrAns = ""


def check_completion_progress(user_text):

    global progressionBar, progress

    if st.session_state.internalText and user_text and user_text != 0:
        internal_words_len = len(st.session_state.internalText.split())
        user_words_len = len(user_text.split())

        if user_words_len <= internal_words_len:
            progress = int((user_words_len/internal_words_len)*100)

        progressionBar.progress(progress)


def capture_user_input():
    
    global usrAns

    while True:
        usrAns = st.session_state.user_input
        time.sleep(0.1)



#-----------------------
# Pages / Sidebar Config
#-----------------------
st.set_page_config(page_title="Typr - Typing Test",
                   page_icon=":keyboard:",
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
#st.markdown("# Typing Test :keyboard:")
st.sidebar.markdown("# Typing Test")

#st.divider()


#------------------
# Page Content
#------------------
with st.container():

    usrAns = st.empty()


    challengeText = st.empty()
    load_ChallengeText()


    usrAns = st_keyup("", key="user_input")


    # Start the thread for capturing user input
    if "user_input_thread" not in st.session_state:
        st.session_state.user_input_thread = threading.Thread(target=usrAns)
        st.session_state.user_input_thread.daemon = True
        st.session_state.user_input_thread.start()


    retryButton = st.button("Retry")
    retry_Submit_Logic()


    # Displaying Challenge Text
    challengeText.markdown(f"## {st.session_state.internalText}")

    progressionBar = st.progress(0)
    progress = 0
    check_completion_progress(usrAns)
    

