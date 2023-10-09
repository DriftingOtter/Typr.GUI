import flet as ft


class Login(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        page.title = "Typr: Your Personal Typing Tutor"

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
                        "Welcome, back! Let's Get Ready To Type.",
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

        self.pageContent = ft.ListView(
            controls=[
                self.pageHeader
                    ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH
        )

        self.pageContent.alignment = ft.alignment.center

    def page_resize(self, e):
        self.pageContent.alignment = ft.alignment.center

    def build(self):
        return self.pageContent
