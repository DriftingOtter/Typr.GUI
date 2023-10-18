import streamlit as st
from st_keyup import st_keyup
import string
import random
import time
import threading


# ---------------------------------
# Random Challenge Text Generation
# ---------------------------------
def generateChallengeText(numOfWords):
    wordList = "/home/daksh/Documents/Typr/WordLists/Loki_Word_List_EN.txt"
    challengeText = []

    with open(wordList, "r") as currentText:
        lines = currentText.readlines()

    numLines = len(lines)

    for words in range(numOfWords):
        randomLineGen = random.randint(0, numLines - 1)
        challengeText.append(lines[randomLineGen].strip())

    return challengeText


def conv_LTS(lst):  # Converts The Generated ChallengeText List -> String
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

        if len(internal_words) != len(user_words):
            return False

        for i in range(len(internal_words)):
            if internal_words[i] != user_words[i]:
                return False

        return True


def retry_Logic():
    global usrAns, progress, progressionBar, usrAnsText

    if retryButton:
        progressionBar = st.empty()
        progress = 0

        challengeText.empty()
        st.session_state.internalText = conv_LTS(generateChallengeText(10))

        usrAnsText = ""

        check_completion_progress(usrAns)

    else:
        submit_Logic()


def submit_Logic():
    global usrAns, progress, progressionBar

    if usrAns and (len(usrAns) >= len(st.session_state.internalText)):
        if len(usrAns) != len(st.session_state.internalText):  # type: ignore
            st.toast("You Failed!")

            progressionBar = st.empty()
            progress = 0
            # progressionBar.progress(progress)

        else:
            if check_completion(usrAns):
                st.toast("You Did it!")

                progressionBar = st.empty()
                progress = 0
                # progressionBar.progress(progress)
            else:
                st.toast("You Failed!")

                progressionBar = st.empty()
                progress = 0
                # progressionBar.progress(progress)

                challengeText.empty()
                st.session_state.internalText = conv_LTS(generateChallengeText(10))
                usrAns = ""

                check_completion_progress(usrAns)


def check_completion_progress(user_text):
    global progressionBar, progress

    if st.session_state.internalText and user_text and user_text != 0:
        internal_words_len = len(st.session_state.internalText.split())
        user_words_len = len(str(user_text).split())

        if user_words_len <= internal_words_len:
            progress = int((user_words_len / internal_words_len) * 100)

        progressionBar.progress(progress)


def capture_user_input():
    global usrAns

    while True:
        usrAns = st.session_state.user_input
        time.sleep(0.1)


def handle_user_input():
    global usrAns

    while True:
        user_text = usrAns
        check_completion_progress(user_text)

        time.sleep(0.1)


# -----------------------
# Pages / Sidebar Config
# -----------------------
st.set_page_config(
    page_title="Typr - Typing Test",
    page_icon=":keyboard:",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": """# Typr - About Me

Typr was built as my final High-School CS Project. It is
was made to make learning touch typing a less daunting
task.

I personally learned it with some struggles and would have
loved to have a service like this :)

I hope you enjoy using it!"""
    },
)


# ----------------------
# Inital Page Setup
# ----------------------
# st.markdown("# Typing Test :keyboard:")
st.sidebar.markdown("# Typing Test")

# st.divider()


# ------------------
# Page Content
# ------------------
with st.container():
    progressionBar = st.progress(0)
    progress = 0

with st.container():
    usrAns = st.empty()

    challengeText = st.empty()
    load_ChallengeText()

    usrAnsText = ""

    if "user_input" not in st.session_state:
        st.session_state["user_input"] = usrAnsText

    usrAns = st_keyup("", key="user_input")

    # Start the thread for capturing user input
    if "user_input_thread" not in st.session_state:
        st.session_state.user_input_thread = threading.Thread(
            target=st.session_state.user_input
        )
        st.session_state.user_input_thread.daemon = True
        st.session_state.user_input_thread.start()

    retryButton = st.button("Retry")
    retry_Logic()

    # Displaying Challenge Text
    challengeText.markdown(f"## {st.session_state.internalText}")

    check_completion_progress(usrAns)
