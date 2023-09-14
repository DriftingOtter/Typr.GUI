import flet as ft
import time
import stdfunc


def main(page: ft.Page):
    page.title = "Typr: Your Typing Tutor"
    page.theme = ft.theme.Theme(color_scheme_seed="blue", font_family="Arial")
    page.scroll = ft.ScrollMode.HIDDEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_WORK_ROUNDED, label="Home"),
            ft.NavigationDestination(
                icon=ft.icons.LIBRARY_BOOKS_ROUNDED, label="Lessons"
            ),
            ft.NavigationDestination(
                icon=ft.icons.ACCOUNT_CIRCLE_ROUNDED,
                label="Profile",
            ),
        ]
    )

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
        f"{str(stdfunc.conv_LTS(stdfunc.generateChallengeText(10)))}",
        style=ft.TextThemeStyle.DISPLAY_MEDIUM,
    )
    page.add(challengeText)
    page.update()

    usrIsTyping = False
    timeStartState = False

    def runtimeCheck(e):
        global usrEntryBox, challengeText, usrIsTyping, timeStartState

        usrIsTyping = False
        timeStartState = False

        if len(usrEntryBox.value) > 0:
            if usrIsTyping is False:
                usrIsTyping = True

            if usrIsTyping is True and timeStartState is False:
                timeSTART = time.time()
                timeStartState = True

                print("Time Started!")

            if timeStartState is True and usrIsTyping is False:
                if len(usrEntryBox.value) == len(challengeText.value):
                    timeSTOP = time.time()
                    timeStartState = False

                    print("Time Stoped!")

                    results = [None] * 2

                    results[1] = textAcc(
                        usrEntryBox.value, challengeText.value, len(challengeText.value)
                    )
                    results[2] = timeTaken(timeSTOP, timeSTART)
                    results[3] = wordsPerMinute(
                        timeTaken(timeSTOP, timeSTART), len(challengeText.value)
                    )

                    resultRow = ft.Text(
                        f"RESULTS | WPM:{results[2]}, ACC:{results[1]}, TTK:{results[0]}"
                    )
                    page.show_snack_bar(ft.SnackBar(resultRow))

                    print("Results Calculated!")

                    # Creating New Text For Usr
                    usrEntryBox.value = ""
                    challengeText.value = str(
                        stdfunc.conv_LTS(stdfunc.generateChallengeText(10))
                    )
                    page.add(challengeText)
                    page.update()

                    print("New Text Generated!")

                if len(usrEntryBox.value) > len(challengeText.value):
                    usrEntryBox.error_text = "Incorrect. Try Again!"
                    usrEntryBox.value = ""
                    page.update()

                    # Creating New Text For Usr
                    usrEntryBox.value = ""
                    challengeText.value = str(
                        stdfunc.conv_LTS(stdfunc.generateChallengeText(10))
                    )
                    page.add(challengeText)
                    page.update()

                    print("Too long :|")

    def textAcc(plyr_text, displayText, word_count):
        # Calculates Text Acc
        textACC = len(set(plyr_text.split()) & set(displayText.split()))

        textACC = int((textACC / word_count) * 100)

        return textACC

    def timeTaken(time_STOP, time_START):
        # Gather Time Taken
        timetaken = int(time_STOP - time_START)

        return timetaken

    def wordsPerMinute(timeTaken, word_Count):
        # Calculates Words Per Minute
        wordsPerMinute = round((word_Count / timeTaken * 100))

        return wordsPerMinute

    global usrEntryBox
    usrEntryBox = ft.TextField(label="Type the following text.", on_change=runtimeCheck)
    page.add(usrEntryBox)
    page.update()

    def checkANS_click(e):
        global userEntryBox, challengeText, usrIsTyping, timeTaken

        if usrEntryBox.value != challengeText.value:
            usrEntryBox.error_text = "Incorrect. Try Again!"
            usrEntryBox.value = ""
            page.update()

            timeTaken = False
            usrIsTyping = False
        else:
            usrEntryBox.value = ""
            winText = ft.Text("You Did It!")
            page.show_snack_bar(ft.SnackBar(winText))

            timeTaken = False
            usrIsTyping = False

    checkBtn = ft.ElevatedButton("Check Answer", on_click=checkANS_click)
    page.add(checkBtn)
    page.update()

    def retry_click(e):
        global challengeText, usrEntryBox, timeStartState, usrIsTyping

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

    retryBtn = ft.ElevatedButton("Retry", on_click=retry_click)
    page.add(retryBtn)
    page.update()


ft.app(main)
