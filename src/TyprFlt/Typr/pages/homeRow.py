import flet as ft
import pages.stdfunc
import time


class HomeTyping(ft.UserControl):
    def __init__(self, page):
        super().__init__()

        self.page = page
        self.page.title = "Typr: Home Row Lesson"

        self.page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.page.scroll = ft.ScrollMode.HIDDEN

        self.timeStartState = False
        self.usrIsTyping = False
        self.timeSTART = float()
        self.timeSTOP = float()

        self.challengeText = ft.Text(
            f"{str(pages.stdfunc.conv_LTS(pages.stdfunc.generateChallengeText(10)))}",
            text_align=ft.TextAlign.CENTER,
            style=ft.TextThemeStyle.DISPLAY_LARGE,
        )

        self.usrEntryBox = ft.TextField(
            label="Type the following text",
            autocorrect=False,
            enable_suggestions=False,
            smart_dashes_type=False,
            text_size=20,
            on_change=self.onUserInput,
        )

        self.returnBtn = ft.ElevatedButton(
            "Go To Lesson Page",
            on_click=lambda _: self.page.go("/lessons"),
        )

        self.typingComp = ft.SafeArea(
            self.challengeText, self.usrEntryBox, self.returnBtn
        )

        self.pageContent = ft.ListView(
            controls=[
                self.challengeText,
                ft.Container(padding=10),
                self.usrEntryBox,
                ft.Container(padding=10),
                self.returnBtn,
            ]
        )

        # -----------------------
        # Enables On 'Tab' Reset
        # -----------------------
        self.page.on_keyboard_event = self.onTabReset

    def startTyping(self):
        self.timeSTART = time.monotonic()
        self.usrIsTyping = True
        self.timeStartState = True
        print("\n###############################")
        print("[COMPLETED] Time Started!")

    def stopTyping(self):
        self.timeSTOP = time.monotonic()
        self.timeStartState = False
        print("[COMPLETED] Time Stopped!")

    def calculateResults(self, challengeText, usrEntryBox):
        acc = self.textAcc(usrEntryBox, challengeText)
        ttk = self.timeTaken(self.timeSTOP, self.timeSTART)
        wpm = self.wordsPerMinute(ttk, len(challengeText.split()))
        results = [acc, ttk, wpm]
        return results

    def displayResults(self, results):
        resultsDialogue = ft.AlertDialog(
            title=ft.Text(
                "Here are your results \U0001F9D9",
                style=ft.TextThemeStyle.DISPLAY_LARGE,
            ),
            content=ft.Text(
                f"\U0001F680  Words Per Minute: {results[2]}\n\U0001F3AF  Accuracy: {results[0]}%\n\U0001F551  Time Taken: {results[1]}s",
                style=ft.TextThemeStyle.DISPLAY_MEDIUM,
            ),
            on_dismiss=lambda e: print("[EVENT] Results Dialog Dismissed"),
        )
        self.page.dialog = resultsDialogue
        resultsDialogue.open = True
        self.page.update()
        print("[COMPLETED] Results Calculated!")

    def resetInputs(self):
        global usrEntryBox, challengeText

        if self.timeStartState is True or self.usrIsTyping is True:
            self.timeStartState = False
            self.usrIsTyping = False
            self.usrEntryBox.value = ""

            buffer: str = str(
                pages.stdfunc.conv_LTS(pages.stdfunc.generateChallengeText(10))
            )

            self.challengeText.value = str(buffer)
            self.page.add(self.challengeText)
            self.page.update()

        if self.timeStartState is False or self.usrIsTyping is False:
            self.usrEntryBox.value = ""
            self.challengeText.value = str(
                pages.stdfunc.conv_LTS(pages.stdfunc.generateChallengeText(10))
            )
            self.page.add(self.challengeText)
            self.page.update()

        print("[COMPLETED] New Text Generated!")

    def onUserInput(self, e):
        if len(self.usrEntryBox.value) > 0:
            if not self.usrIsTyping:
                self.startTyping()
            elif self.timeStartState and not self.usrIsTyping:
                self.stopTyping()

            if len(self.usrEntryBox.value) > len(self.challengeText.value):
                self.usrEntryBox.error_text = "Incorrect, Text Too Long. Try Again!"
                self.resetInputs()
                print("[COMPLETED] Test Completed!\n")

            if self.usrEntryBox.value == self.challengeText.value:
                self.stopTyping()
                self.displayResults(
                    self.calculateResults(
                        self.usrEntryBox.value, self.challengeText.value
                    )
                )
                self.resetInputs()
                print("[COMPLETED] Test Completed!\n")

            if len(self.usrEntryBox.value) == len(self.challengeText.value):
                self.stopTyping()
                self.displayResults(
                    self.calculateResults(
                        self.usrEntryBox.value, self.challengeText.value
                    )
                )
                self.resetInputs()
                print("[COMPLETED] Test Completed!\n")

    def textAcc(self, usrEntryBox, challengeText):
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

    def timeTaken(self, timeSTOP, timeSTART):
        print(f"    |--> TIME STARTED:{timeSTART}")
        print(f"    |--> TIME STOPED:{timeSTOP}")
        timeTaken = int(timeSTOP - timeSTART)
        print(f"    |--> Time Taken:{timeTaken}s\n")
        return timeTaken

    def wordsPerMinute(self, timeTaken, wordCount):
        print(f"    |--> Word Count:{wordCount}")
        wpm = round((wordCount / timeTaken * 100))

        if wpm > 400 or wpm < 0:
            wpm = "INVALID SCORE"

        print(f"    |--> WPM:{wpm}")
        return wpm

    def retry_click(self, e):
        if self.timeStartState is True or self.usrIsTyping is True:
            self.timeStartState = False
            self.usrIsTyping = False

            self.usrEntryBox.value = ""
            self.challengeText.value = str(
                pages.stdfunc.conv_LTS(pages.stdfunc.generateChallengeText(10))
            )
            self.page.add(self.challengeText)
            self.page.update()

        if self.timeStartState is False or self.usrIsTyping is False:
            self.usrEntryBox.value = ""
            self.challengeText.value = str(
                pages.stdfunc.conv_LTS(pages.stdfunc.generateChallengeText(10))
            )
            self.page.add(self.challengeText)
            self.page.update()

    def onTabReset(self, e: ft.KeyboardEvent):
        if str(e.key) == "Tab":
            print("[EVENT] On-Tab Reset Initiated")
            self.resetInputs()

    def build(self):
        return self.pageContent
