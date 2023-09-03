import flet as ft
import time
import stdfunc

def main(page: ft.Page):
    page.title = "Typr: Your Typing Tutor"
    page.theme = ft.theme.Theme(color_scheme_seed="blue", 
                                font_family="Arial",

                                )
    page.scroll = ft.ScrollMode.HIDDEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_WORK_ROUNDED, 
                                     label="Home"),

            ft.NavigationDestination(icon=ft.icons.LIBRARY_BOOKS_ROUNDED, 
                                     label="Lessons"),

            ft.NavigationDestination(icon=ft.icons.ACCOUNT_CIRCLE_ROUNDED,
                                     label="Profile",)])


    def checkANS_click(e):

        global challengeText

        if usrEntryBox.value != challengeText.value:
            usrEntryBox.error_text="Incorrect. Try Again!"
            page.update()
        else:
            winText = ft.Text("You Did It!")
            page.show_snack_bar(ft.SnackBar(winText))

    def retry_click(e):
        global challengeText
        challengeText.value = ft.Text(f"{str(stdfunc.conv_LTS(stdfunc.generateChallengeText(1)))}")
        page.update()

    # def check_completion_progress():
        #global usrEntryBox, challengeText, textCompletionBar

        #if usrEntryBox.value is not None and challengeText.value is not None:

         #   if len(usrEntryBox.value) != 0 and len(challengeText.value) != 0:
          #      internal_words_len = len(challengeText.value.split())
           #     user_words_len = len(challengeText.value.split())

            #    if user_words_len <= internal_words_len:
             #       progress = int((user_words_len/internal_words_len)*100)

       # textCompletionBar.value(progress)


    #textCompletionBar = ft.ProgressBar()
    #textCompletionBar.value = 0
    #page.add(textCompletionBar)
    #page.update()

    challengeText = ft.Text(
            f"{str(stdfunc.conv_LTS(stdfunc.generateChallengeText(10)))}",
            style=ft.TextThemeStyle.DISPLAY_MEDIUM)
    page.add(challengeText)
    page.update()

    usrEntryBox = ft.TextField(label="Type the following text.")
    page.add(usrEntryBox)
    page.update()

    checkBtn = ft.ElevatedButton("Check Answer", on_click=checkANS_click)
    page.add(checkBtn)
    page.update()

    retryBtn = ft.ElevatedButton("Retry", on_click=retry_click)
    page.add(retryBtn)
    page.update()


ft.app(main)
