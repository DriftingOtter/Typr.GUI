import flet as ft
from .ottrDBM import OttrDBM


class Signup(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        self.dbConfig = {
            "user": "root",
            "password": "",
            "host": "localhost",
            "database": "typr_acc_info",
            "raise_on_warnings": True,
        }
        self.signupManager = OttrDBM(self.dbConfig)

        page.title = "Typr: Your Personal Typing Tutor"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.scroll = ft.ScrollMode.HIDDEN
        page.on_resize = self.page_resize

        # Page Controls
        self.pageHeader = ft.Row(
            controls=[
                ft.Image(
                    src="images/Astro_Typing.png",
                    height=300,
                    fit=ft.ImageFit.FIT_WIDTH,
                ),
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

        self.emailHeading = ft.Text(
            "Email Address",
            style=ft.TextThemeStyle.HEADLINE_SMALL,
            text_align=ft.TextAlign.JUSTIFY,
        )

        self.emailIcon = ft.Icon(
            name=ft.icons.EMAIL_ROUNDED,
            color=ft.colors.BLUE,
        )

        self.emailField = ft.TextField(
            label="Enter Email Address",
            autocorrect=False,
            enable_suggestions=False,
            smart_dashes_type=False,
            text_size=20,
        )

        self.pwdHeading = ft.Text(
            "Password",
            style=ft.TextThemeStyle.HEADLINE_SMALL,
            text_align=ft.TextAlign.JUSTIFY,
        )

        self.pwdIcon = ft.Icon(
            name=ft.icons.PASSWORD_ROUNDED,
            color=ft.colors.BLUE,
        )

        self.pwdField = ft.TextField(
            label="Enter A Secure Password",
            autocorrect=False,
            enable_suggestions=False,
            smart_dashes_type=False,
            text_size=20,
            password=True,
            can_reveal_password=True,
        )

        self.signupBtn = ft.ElevatedButton(
            "Signup",
            on_click=self.signup_event,
        )

        self.loginBtn = ft.ElevatedButton(
            "Login",
            on_click=lambda _: self.page.go("/login"),
        )

        self.loginFrame = ft.ListView(
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                self.emailIcon,
                                self.emailHeading,
                            ]
                        ),
                        self.emailField,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                ),
                ft.Container(padding=5),
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                self.pwdIcon,
                                self.pwdHeading,
                            ]
                        ),
                        self.pwdField,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                ),
                ft.Column(
                    controls=[
                        ft.Container(padding=5),
                        self.signupBtn,
                        self.loginBtn,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                ),
            ]
        )

        self.pageContent = ft.ListView(
            controls=[
                ft.Container(self.pageHeader),
                ft.Divider(),
                ft.Container(padding=5),
                ft.Container(self.loginFrame),
            ],
        )
        self.pageContent.alignment = ft.alignment.center

    def signup_event(self, e):
        # Gather User Information
        self.email = str(self.emailField.value).strip()
        self.pwd = str(self.pwdField.value).strip()

        # Validate & Create New User In DB along with personal DB
        self.returnValue = self.signupManager.createUser(self.email, self.pwd)

        if self.returnValue == 0:
            self.page.go("/lessons")
        else:
            # Add Error Notification During Error Code
            pass

    def page_resize(self, e):
        self.pageContent.alignment = ft.alignment.center

    def build(self):
        return self.pageContent

