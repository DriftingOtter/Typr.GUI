import flet as ft
import logging
import pickle
from .ottrDBM import OttrDBM


class Signup(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.login_manager = self.initialize_database()
        self.initialize_page_settings()
        self.initialize_page_controls()

    def initialize_database(self):
        db_config = {
            "user": "root",
            "password": "",
            "host": "localhost",
            "database": "typr_acc_info",
            "raise_on_warnings": True,
        }
        return OttrDBM(db_config)

    def initialize_page_settings(self):
        self.db_config = {
            "user": "root",
            "password": "",
            "host": "localhost",
            "database": "typr_acc_info",
            "raise_on_warnings": True,
        }
        self.signup_manager = OttrDBM(self.db_config)
        logging.basicConfig(level=logging.INFO)
        self.page.title = "Typr: Your Personal Typing Tutor"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.scroll = ft.ScrollMode.HIDDEN
        self.page.on_resize = self.page_resize

    def initialize_page_controls(self):
        self.page_header = self.create_page_header()
        self.email_heading = self.create_heading("Email Address")
        self.email_icon = ft.Icon(name=ft.icons.EMAIL_ROUNDED, color=ft.colors.BLUE)
        self.email_field = self.create_text_field("Enter Email Address")

        self.pwd_heading = self.create_heading("Password")
        self.pwd_icon = ft.Icon(name=ft.icons.PASSWORD_ROUNDED, color=ft.colors.BLUE)
        self.pwd_field = self.create_text_field("Enter A Secure Password", password=True, can_reveal_password=True)

        self.signup_btn = ft.ElevatedButton("Signup", on_click=self.signup_event)
        self.login_btn = ft.ElevatedButton("Login", on_click=lambda _: self.page.go("/login"))

        self.login_frame = ft.ListView(
            controls=[
                self.create_column([self.create_row([self.email_icon, self.email_heading]), self.email_field]),
                ft.Container(padding=5),
                self.create_column([self.create_row([self.pwd_icon, self.pwd_heading]), self.pwd_field]),
                self.create_column([ft.Container(padding=5), self.signup_btn, self.login_btn]),
            ]
        )

        self.page_content = ft.ListView(
            controls=[
                ft.Container(self.page_header),
                ft.Divider(),
                ft.Container(padding=5),
                ft.Container(self.login_frame),
            ],
        )
        self.page_content.alignment = ft.alignment.center

    def create_page_header(self):
        return ft.Row(
            controls=[
                self.create_image("images/Astro_Typing.png", height=300, fit=ft.ImageFit.FIT_WIDTH),
                ft.Container(
                    ft.Text(
                        "Signup",
                        style=ft.TextThemeStyle.DISPLAY_LARGE,
                        size=48,
                        color="white",
                        weight="bold",
                        opacity=0.8,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    alignment=ft.alignment.bottom_center,
                ),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def create_heading(self, text):
        return ft.Text(
            text,
            style=ft.TextThemeStyle.HEADLINE_SMALL,
            text_align=ft.TextAlign.JUSTIFY,
        )

    def create_text_field(self, label, password=False, can_reveal_password=False):
        return ft.TextField(
            label=label,
            autocorrect=False,
            enable_suggestions=False,
            smart_dashes_type=False,
            text_size=20,
            password=password,
            can_reveal_password=can_reveal_password,
        )

    def create_image(self, src, height=200, fit=ft.ImageFit.FIT_WIDTH):
        return ft.Image(
            src=src,
            height=height,
            fit=fit,
        )

    def create_row(self, controls):
        return ft.Row(controls=controls)

    def create_column(self, controls):
        return ft.Column(controls=controls, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.STRETCH)

    def signup_event(self, e):
        # Gather User Information
        self.email = str(self.email_field.value).strip()
        self.pwd = str(self.pwd_field.value).strip()

        # Validate & Create New User In DB along with personal DB
        self.return_value = self.signup_manager.create_user(self.email, self.pwd)

        if self.return_value[0] == 0:
            with open("data.pkl", "wb") as file:
                pickle.dump(str(self.return_value[1]), file)

            self.page.go("/lessons")
        else:
            # Add Error Notification During Error Code
            pass

    def page_resize(self, e):
        self.page_content.alignment = ft.alignment.center

    def build(self):
        return self.page_content

