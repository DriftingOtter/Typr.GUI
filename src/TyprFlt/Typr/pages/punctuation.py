import logging
import datetime
import pickle
import time

import flet as ft
from pages.stdfunc import conv_lts, generate_challenge_text
from .ottrDBM import OttrDBM

logging.basicConfig(level=logging.INFO)


class PunctuationTyping(ft.UserControl):
    def __init__(self, page):
        super().__init__()

        self.page = page
        self.initialize_page_settings()
        self.initialize_db_manager()
        self.initialize_banners()

        self.time_start_state = False
        self.usr_is_typing = False
        self.time_start = None
        self.time_stop = None

        self.initialize_challenge_text()

        self.usr_entry_box = ft.TextField(
            label="Type the following text",
            autocorrect=False,
            enable_suggestions=False,
            smart_dashes_type=False,
            text_size=20,
            on_change=self.on_user_input,
        )

        self.return_btn = ft.ElevatedButton(
            "Go To Lesson Page",
            on_click=lambda _: self.page.go("/lessons"),
        )

        self.typing_comp = ft.SafeArea(
            self.challenge_text, self.usr_entry_box, self.return_btn
        )

        self.page_content = ft.ListView(
            controls=[
                self.challenge_text,
                ft.Container(padding=10),
                self.usr_entry_box,
                ft.Container(padding=10),
                self.return_btn,
            ]
        )

    def initialize_page_settings(self):
        self.page.title = "Typr: Punctuation Lesson"
        self.page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.scroll = ft.ScrollMode.HIDDEN

    def initialize_db_manager(self):
        self.db_config = {
            "user": "root",
            "password": "",
            "host": "localhost",
            "database": "typr_acc_info",
            "raise_on_warnings": True,
        }
        self.db_manager = OttrDBM(self.db_config)

    def initialize_banners(self):
        self.db_saver_banner_fail = self.create_banner(
            ft.colors.AMBER_100, ft.icons.WARNING_AMBER_ROUNDED, "Oops, could not save user data to database.", self.fail_close_banner
        )
        self.db_saver_banner_pass = self.create_banner(
            ft.colors.GREEN, ft.icons.CHECK, "Great, successfully saved user data to database.", self.pass_close_banner
        )

    def create_banner(self, bgcolor, icon, content_text, close_handler):
        return ft.Banner(
            bgcolor=bgcolor,
            leading=ft.Icon(icon, color=bgcolor, size=40),
            content=ft.Text(content_text),
            actions=[ft.TextButton("Close", on_click=close_handler)],
        )

    def initialize_challenge_text(self):
        self.challenge_text = ft.Text(
            str(conv_lts(generate_challenge_text(10, "/home/daksh/Documents/Typr/src/TyprFlt/Typr/WordLists/Loki_Word_List_EN.txt"))),
            text_align=ft.TextAlign.CENTER,
            style=ft.TextThemeStyle.DISPLAY_LARGE,
        )

    def start_typing(self):
        self.time_start = time.monotonic()
        self.usr_is_typing = True
        self.time_start_state = True
        logging.info("\n###############################")
        logging.info("[COMPLETED] Time Started at %s.", datetime.datetime.now())

    def stop_typing(self):
        self.time_stop = time.monotonic()
        self.time_start_state = False
        logging.info("[COMPLETED] Time Stopped at %s.", datetime.datetime.now())

    def calculate_results(self):
        acc = self.text_acc()
        ttk = self.time_taken()
        wpm = self.words_per_minute(len(self.challenge_text.value.split()))
        results = [acc, ttk, wpm]
        return results

    def display_results(self, results):
        results_dialogue = self.create_results_dialogue(results)
        self.page.dialog = results_dialogue
        results_dialogue.open = True
        self.page.update()
        logging.info("[COMPLETED] Results Calculated!")

        self.send_results_to_db(results[2], results[0], results[1], "PTT")

    def create_results_dialogue(self, results):
        title = ft.Text("Here are your results \U0001F9D9", style=ft.TextThemeStyle.DISPLAY_LARGE)
        content = ft.Text(
            f"\U0001F680  Words Per Minute: {results[2]}\n\U0001F3AF  Accuracy: {results[0]}%\n\U0001F551  Time Taken: {results[1]}s",
            style=ft.TextThemeStyle.DISPLAY_MEDIUM,
        )
        return ft.AlertDialog(title=title, content=content, on_dismiss=lambda e: logging.info("[EVENT] Results Dialog Dismissed"))

    def send_results_to_db(self, wpm, acc, ttk, test_type):
        try:
            with open("data.pkl", "rb") as file:
                self.loaded_data = pickle.load(file)
            self.current_user = self.loaded_data

            self.return_value = self.db_manager.addTestScore(
                self.current_user,
                wpm,
                acc,
                ttk,
                test_type,
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            )

            if self.return_value == 0:
                self.db_saver_banner_pass.open = True
                self.page.update()
            else:
                self.db_saver_banner_fail.open = True
                self.page.update()

        except FileNotFoundError as e:
            logging.error(f"Error: {e}. File 'data.pkl' not found.")
            # Handle the exception, e.g., show an error message to the user.

        except Exception as e:
            logging.error(f"Error: {e}. An unexpected error occurred.")
            # Handle other exceptions as needed.

    def pass_close_banner(self, e):
        self.db_saver_banner_pass.open = False
        self.page.update()

    def fail_close_banner(self, e):
        self.db_saver_banner_fail.open = False
        self.page.update()

    def reset_inputs(self):
        if self.time_start_state or self.usr_is_typing:
            self.time_start_state = False
            self.usr_is_typing = False
            self.usr_entry_box.value = ""
            self.challenge_text.value = str(conv_lts(generate_challenge_text(10, "/home/daksh/Documents/Typr/src/TyprFlt/Typr/WordLists/Loki_Word_List_EN.txt")))

        logging.info("[COMPLETED] New Text Generated and inputs reset at %s.", datetime.datetime.now())

    def on_user_input(self, e):
        if not isinstance(self.usr_entry_box.value, str):
            logging.warning("Unexpected input type received in on_user_input.")
            return

        if len(self.usr_entry_box.value) > 0:
            if not self.usr_is_typing:
                self.start_typing()
            elif self.time_start_state and not self.usr_is_typing:
                self.stop_typing()

            if len(self.usr_entry_box.value) > len(self.challenge_text.value):
                self.usr_entry_box.error_text = "Incorrect, Text Too Long. Try Again!"
                self.reset_inputs()
                logging.info("[COMPLETED] Test Completed!\n")

            if self.usr_entry_box.value == self.challenge_text.value:
                self.stop_typing()
                self.display_results(self.calculate_results())
                self.reset_inputs()
                logging.info("[COMPLETED] Test Completed!\n")

            if len(self.usr_entry_box.value) == len(self.challenge_text.value):
                self.stop_typing()
                self.display_results(self.calculate_results())
                self.reset_inputs()
                logging.info("[COMPLETED] Test Completed!\n")

    def text_acc(self):
        usr_chars = list(self.usr_entry_box.value)
        challenge_chars = list(self.challenge_text.value)

        correct_char_count = sum(
            usr_char == challenge_char
            for usr_char, challenge_char in zip(usr_chars, challenge_chars)
        )
        total_char_count = len(challenge_chars)

        text_accuracy = round((correct_char_count / total_char_count) * 100)
        return text_accuracy

    def time_taken(self):
        time_taken = int(self.time_stop - self.time_start)
        return time_taken

    def words_per_minute(self, word_count):
        wpm = round((word_count / self.time_taken() * 100))
        if not 0 <= wpm <= 400:
            wpm = "INVALID SCORE"
        return wpm

    def retry_click(self, e):
        self.reset_inputs()

    def force_reset(self, e):
        logging.info("[EVENT] On-Tab Reset Initiated")
        self.reset_inputs()

    def build(self):
        return self.page_content

