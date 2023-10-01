import flet as ft


class Signup(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        page.title = "Typr: Your Personal Typing Tutor"

        page.theme = ft.theme.Theme(
            color_scheme_seed="blue",
            font_family="JetBrainsMono Nerd Font, Arial",
        )

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        page.scroll = ft.ScrollMode.HIDDEN

        page.on_resize = self.page_resize

        # ==============
        # Page Controls
        # ==============
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
        )

        self.signupBtn = ft.ElevatedButton(
            "Signup",
            on_click=lambda _: self.page.go("/typingtest"),
        )

        self.loginBtn = ft.ElevatedButton(
            "Login",
            on_click=lambda _: self.page.go("/login"),
        )

        self.pageContent = ft.ListView(
            controls=[
                ft.Container(self.pageHeader),
                ft.Divider(),
                ft.Container(padding=5),
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
            ],
        )
        self.pageContent.padding = ft.padding.symmetric(
                int(self.page.window_height)/1.5,
                int(self.page.window_width)/1.5,
        )
        self.pageContent.alignment = ft.alignment.center

    def page_resize(self, e):
        self.pageContent.padding = ft.padding.symmetric(
                int(self.page.window_height)/1.5,
                int(self.page.window_width)/1.5,
        )
        self.pageContent.alignment = ft.alignment.center

    def build(self):
        return self.pageContent
