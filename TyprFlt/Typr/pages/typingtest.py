import flet as ft
import pages.stdfunc


class Typing(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            # ===========
                            # Page Title
                            # ===========
                            ft.Text(
                                "Typing Page",
                                style=ft.TextThemeStyle.DISPLAY_LARGE,
                                weight=ft.FontWeight.BOLD,
                            ),
                            # =======================
                            # Challenge Text Display
                            # =======================
                            ft.Text(
                                f"{str(pages.stdfunc.conv_LTS(pages.stdfunc.generateChallengeText(10)))}",
                                text_align=ft.TextAlign.CENTER,
                                style=ft.TextThemeStyle.DISPLAY_LARGE,
                            ),
                            #===============
                            # User Entry Box
                            #===============
                            ft.TextField(
                                label="Type the following text",
                                autofocus=True,
                                autocorrect=False,
                                enable_suggestions=False,
                                smart_dashes_type=False,
                                text_size=20,
                                #on_change=onUserInput,
                            ),
                            # ======================
                            # Return To Home Button
                            # ======================
                            ft.ElevatedButton(
                                "Go To Home Page",
                                on_click=lambda _: self.page.go("/"),
                            ),
                        ]
                    )
                )
            ]
        )
