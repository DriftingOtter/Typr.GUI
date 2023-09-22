import flet as ft
import time
import stdfunc


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
                            ft.Text("Typing Page"),
                            ft.ElevatedButton(
                                "Go To Home Page",
                                on_click=lambda _: self.page.go("/"),
                            ),
                        ]
                    )
                )
            ]
        )
