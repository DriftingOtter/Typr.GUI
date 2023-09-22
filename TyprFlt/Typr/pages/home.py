import flet as ft


class Home(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Typr: Your Personal Typing Tutor"),
                            ft.ElevatedButton(
                                "Go To Typing Page",
                                on_click=lambda _: self.page.go("/typingtest"),
                            ),
                        ]
                    )
                )
            ]
        )
