import flet as ft
import time
import stdfunc


def main(page: ft.Page):
    # ----------------------------------
    # PAGE INITALIZE SETTINGS & CONFIGS
    # ----------------------------------
    page.title = "Typr: Your Typing Tutor"
    page.theme = ft.theme.Theme(color_scheme_seed="blue", font_family="Arial")

    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.scroll = ft.ScrollMode.HIDDEN
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_WORK_ROUNDED, label="Home"),
            ft.NavigationDestination(
                icon=ft.icons.LIBRARY_BOOKS_ROUNDED, label="Lessons"
            ),
            ft.NavigationDestination(
                icon=ft.icons.ACCOUNT_CIRCLE_ROUNDED, label="Profile"
            ),
        ]
    )

    # -------------------------------------------
    # Enabling Haptic Support For Mobile Devices
    # -------------------------------------------
    hapticFeedback = ft.HapticFeedback()
    page.overlay.append(hapticFeedback)
    page.update()

    # --------------------------------------------
    # GLOBAL VARIABLES | IMPORTANT FOR TYPING TEST
    # --------------------------------------------
    global usrIsTyping, timeStartState, timeSTART, timeSTOP
    usrIsTyping = False
    timeStartState = False
    timeSTART = float()
    timeSTOP = float()

    def startTyping():
        global usrIsTyping, timeStartState
        global timeSTART

        timeSTART = time.monotonic()
        usrIsTyping = True
        timeStartState = True
        print("\n###############################")
        print("[COMPELTED] Time Started!")

    def stopTyping():
        global timeStartState, timeSTOP

        timeSTOP = time.monotonic()
        timeStartState = False

        print("[COMPELTED] Time Stopped!")

    def calculateResults(challengeText, usrEntryBox):
        global timeSTAT, timeSTOP

        acc = textAcc(usrEntryBox, challengeText)
        ttk = timeTaken(timeSTOP, timeSTART)
        wpm = wordsPerMinute(ttk, len(challengeText.split()))

        results = [acc, ttk, wpm]
        return results

    def displayResults(results):
        resultsDialogue = ft.AlertDialog(
            title=ft.Text(
                "Here are your results \U0001F9D9",
                style=ft.TextThemeStyle.DISPLAY_LARGE,
            ),
            content=ft.Text(
                f"\U0001F680  Words Per Minute: {results[2]}\n\U0001F3AF  Accuracy: {results[0]}%\n\U0001F551  Time Taken: {results[1]}s",
                style=ft.TextThemeStyle.DISPLAY_MEDIUM,
            ),
            on_dismiss=lambda e: print("\n[EVENT] Results Dialog Dismissed"),
        )
        page.dialog = resultsDialogue
        resultsDialogue.open = True
        page.update()

        print("[COMPELTED] Results Calculated!")

    def resetInputs():
        global challengeText, usrEntryBox
        global timeStartState, usrIsTyping

        if timeStartState is True or usrIsTyping is True:
            timeStartState = False
            usrIsTyping = False

            usrEntryBox.value = ""
            challengeText.value = str(
                stdfunc.conv_LTS(stdfunc.generateChallengeText(10))
            )
            page.add(challengeText)
            page.update()

        if timeStartState is False or usrIsTyping is False:
            usrEntryBox.value = ""
            challengeText.value = str(
                stdfunc.conv_LTS(stdfunc.generateChallengeText(10))
            )
            page.add(challengeText)
            page.update()

        print("[COMPELTED] New Text Generated!")

    def onUserInput(e):
        hapticFeedback.medium_impact()

        global usrEntryBox, challengeText
        global timeStartState, usrIsTyping

        if len(usrEntryBox.value) > 0:
            if not usrIsTyping:
                startTyping()
            elif timeStartState and not usrIsTyping:
                stopTyping()

            if len(usrEntryBox.value) > len(challengeText.value):
                usrEntryBox.error_text = "Incorrect, Text Too Long. Try Again!"
                resetInputs()
                print("[COMPELTED] Test Completed!\n")

            if usrEntryBox.value == challengeText.value:
                stopTyping()
                displayResults(calculateResults(usrEntryBox.value, challengeText.value))
                resetInputs()
                print("[COMPELTED] Test Completed!\n")

            if len(usrEntryBox.value) == len(challengeText.value):
                stopTyping()
                displayResults(calculateResults(usrEntryBox.value, challengeText.value))
                resetInputs()
                print("[COMPELTED] Test Completed!\n")

    def textAcc(usrEntryBox, challengeText):
        if len(usrEntryBox) < len(challengeText):
            textAccuracy = 0
            return textAccuracy

        usrChars = list(usrEntryBox)
        challengeChars = list(challengeText)

        print(f"    |--> User Characters: {usrChars}")
        print(f"    |--> Challenge Characters: {challengeChars}\n")

        correctCharCount = sum(
            usrChar == challengeChar
            for usrChar, challengeChar in zip(usrChars, challengeChars)
        )
        totalCharCount = len(challengeChars)

        print(f"    |--> Correct Character Count: {correctCharCount}")
        print(f"    |--> Total Character Count: {totalCharCount}")

        textAccuracy = round((correctCharCount / totalCharCount) * 100)
        print(f"    |--> Text Accuracy: {textAccuracy}%\n")
        return textAccuracy

    def timeTaken(timeSTOP, timeSTART):
        print(f"    |--> TIME STARTED:{timeSTART}")
        print(f"    |--> TIME STOPED:{timeSTOP}")
        timeTaken = int(timeSTOP - timeSTART)
        print(f"    |--> Time Taken:{timeTaken}s\n")
        return timeTaken

    def wordsPerMinute(timeTaken, wordCount):
        print(f"    |--> Word Count:{wordCount}")
        wpm = round((wordCount / timeTaken * 100))

        if wpm > 400 or wpm < 0:
            wpm = "INVALID SCORE"

        print(f"    |--> WPM:{wpm}")
        return wpm

    def retry_click(e):
        global challengeText, usrEntryBox
        global timeStartState, usrIsTyping

        if timeStartState is True or usrIsTyping is True:
            timeStartState = False
            usrIsTyping = False

            usrEntryBox.value = ""
            challengeText.value = str(
                stdfunc.conv_LTS(stdfunc.generateChallengeText(10))
            )
            page.add(challengeText)
            page.update()

        if timeStartState is False or usrIsTyping is False:
            usrEntryBox.value = ""
            challengeText.value = str(
                stdfunc.conv_LTS(stdfunc.generateChallengeText(10))
            )
            page.add(challengeText)
            page.update()

    # SOON TO BE ADDED PROGRESS BAR
    # ------------------------------
    # def check_completion_progress():
    # global usrEntryBox, challengeText, textCompletionBar

    # if usrEntryBox.value is not None and challengeText.value is not None:

    #   if len(usrEntryBox.value) != 0 and len(challengeText.value) != 0:
    #      internal_words_len = len(challengeText.value.split())
    #     user_words_len = len(challengeText.value.split())

    #    if user_words_len <= internal_words_len:
    #       progress = int((user_words_len/internal_words_len)*100)

    # textCompletionBar.value(progress)

    # textCompletionBar = ft.ProgressBar()
    # textCompletionBar.value = 0
    # page.add(textCompletionBar)
    # page.update()

    global challengeText
    challengeText = ft.Text(
        f"{str(stdfunc.conv_LTS(stdfunc.generateChallengeText(2)))}",
        text_align=ft.TextAlign.CENTER,
        style=ft.TextThemeStyle.DISPLAY_LARGE,
    )
    page.add(challengeText)
    page.update()

    global usrEntryBox
    usrEntryBox = ft.TextField(
        label="Type the following text.",
        autofocus=True,
        autocorrect=False,
        enable_suggestions=False,
        smart_dashes_type=False,
        text_size=20,
        on_change=onUserInput,
    )
    page.add(usrEntryBox)
    page.update()

    retryBtn = ft.ElevatedButton("Retry", on_click=retry_click)
    page.add(retryBtn)
    page.update()


ft.app(main, use_color_emoji=True)
