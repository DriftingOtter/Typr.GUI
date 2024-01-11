import logging
import flet as ft
from pages.stdfunc import conv_LTS, generateChallengeText
import time

logging.basicConfig(level=logging.INFO)

class FreeTyping(ft.UserControl):
    def __init__(self, page):
        super().__init__()

        self.page = page
        self.initialize_page_settings()

        self.timeStartState = False
        self.usrIsTyping = False
        self.timeSTART = None
        self.timeSTOP = None

        self.challengeText = ft.Text(
            str(conv_LTS(generateChallengeText(10))),
            text_align=ft.TextAlign.CENTER,
            style=ft.TextThemeStyle.DISPLAY_LARGE,
        )

        self.usrEntryBox = ft.TextField(
            label="Type the following text",
            autocorrect=False,
            enable_suggestions=False,
            smart_dashes_type=False,
            text_size=20,
            on_change=self.on_user_input,
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

        self.page.on_keyboard_event = self.on_tab_reset

    def initialize_page_settings(self):
        self.page.title = "Typr: Free Typing / Typing Test"
        self.page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.scroll = ft.ScrollMode.HIDDEN

    def start_typing(self):
        self.timeSTART = time.monotonic()
        self.usrIsTyping = True
        self.timeStartState = True
        logging.info("\n###############################")
        logging.info("[COMPLETED] Time Started!")

    def stop_typing(self):
        self.timeSTOP = time.monotonic()
        self.timeStartState = False
        logging.info("[COMPLETED] Time Stopped!")

    def calculate_results(self):
        acc = self.text_acc()
        ttk = self.time_taken()
        wpm = self.words_per_minute(len(self.challengeText.value.split()))
        results = [acc, ttk, wpm]
        return results

    def display_results(self, results):
        results_dialogue = ft.AlertDialog(
            title=ft.Text(
                "Here are your results \U0001F9D9",
                style=ft.TextThemeStyle.DISPLAY_LARGE,
            ),
            content=ft.Text(
                f"\U0001F680  Words Per Minute: {results[2]}\n\U0001F3AF  Accuracy: {results[0]}%\n\U0001F551  Time Taken: {results[1]}s",
                style=ft.TextThemeStyle.DISPLAY_MEDIUM,
            ),
            on_dismiss=lambda e: logging.info("[EVENT] Results Dialog Dismissed"),
        )
        self.page.dialog = results_dialogue
        results_dialogue.open = True
        self.page.update()
        logging.info("[COMPLETED] Results Calculated!")

    def reset_inputs(self):
        if self.timeStartState or self.usrIsTyping:
            self.timeStartState = False
            self.usrIsTyping = False
            self.usrEntryBox.value = ""
            self.challengeText.value = str(conv_LTS(generateChallengeText(10)))

        logging.info("[COMPLETED] New Text Generated!")

    def on_user_input(self, e):
        if len(self.usrEntryBox.value) > 0:
            if not self.usrIsTyping:
                self.start_typing()
            elif self.timeStartState and not self.usrIsTyping:
                self.stop_typing()

            if len(self.usrEntryBox.value) > len(self.challengeText.value):
                self.usrEntryBox.error_text = "Incorrect, Text Too Long. Try Again!"
                self.reset_inputs()
                logging.info("[COMPLETED] Test Completed!\n")

            if self.usrEntryBox.value == self.challengeText.value:
                self.stop_typing()
                self.display_results(self.calculate_results())
                self.reset_inputs()
                logging.info("[COMPLETED] Test Completed!\n")

            if len(self.usrEntryBox.value) == len(self.challengeText.value):
                self.stop_typing()
                self.display_results(self.calculate_results())
                self.reset_inputs()
                logging.info("[COMPLETED] Test Completed!\n")

    def text_acc(self):
        usr_chars = list(self.usrEntryBox.value)
        challenge_chars = list(self.challengeText.value)

        correct_char_count = sum(
            usr_char == challenge_char
            for usr_char, challenge_char in zip(usr_chars, challenge_chars)
        )
        total_char_count = len(challenge_chars)

        text_accuracy = round((correct_char_count / total_char_count) * 100)
        return text_accuracy

    def time_taken(self):
        time_taken = int(self.timeSTOP - self.timeSTART)
        return time_taken

    def words_per_minute(self, word_count):
        wpm = round((word_count / self.time_taken() * 100))
        if not 0 <= wpm <= 400:
            wpm = "INVALID SCORE"
        return wpm

    def retry_click(self, e):
        self.reset_inputs()

    def on_tab_reset(self, e: ft.KeyboardEvent):
        if str(e.key) == "Tab":
            logging.info("[EVENT] On-Tab Reset Initiated")
            self.reset_inputs()

    def build(self):
        return self.pageContent

