import flet as ft


class Lessons(ft.UserControl):
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
                        "Lessons",
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

        self.homeRowCard = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Home Row Lesson"),
                            subtitle=ft.Text(
                                "Learn the basic of typing by learning the row in which your hands lay."
                            ),
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Start Lesson",
                                    on_click=lambda _: self.page.go("/homeRow"),
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )

        self.topRowCard = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Top Row Lesson"),
                            subtitle=ft.Text("Learn the top row and it's intricies."),
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Start Lesson",
                                    on_click=lambda _: self.page.go("/topRow"),
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )

        self.bottomRowCard = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Bottom Row Lesson"),
                            subtitle=ft.Text(
                                "Learn the bottom row. Lets see what you got!"
                            ),
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Start Lesson",
                                    on_click=lambda _: self.page.go("/bottomRow"),
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )

        self.numberRowCard = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Number Row Lesson"),
                            subtitle=ft.Text(
                                "Learn the basic of typing by on the number row, 1..2..3..Lets Go!"
                            ),
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Start Lesson",
                                    on_click=lambda _: self.page.go("/numberRow"),
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )

        self.punctuationRowCard = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Punctuation Row Lesson"),
                            subtitle=ft.Text(
                                "Learn how to utilize punctuation in your typing! Lets see, what you can do."
                            ),
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Start Lesson",
                                    on_click=lambda _: self.page.go("/punctuationRow"),
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )

        self.freeTypingRowCard = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Free Typing / Typing Test"),
                            subtitle=ft.Text(
                                "The final lesson! Let's try out your skills at a whole keyboard test."
                            ),
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Start Lesson",
                                    on_click=lambda _: self.page.go("/freeTyping"),
                                )
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )

        self.LessonContainer = ft.ListView(
            controls=[
                self.homeRowCard,
                ft.Container(padding=10),
                self.topRowCard,
                ft.Container(padding=10),
                self.bottomRowCard,
                ft.Container(padding=10),
                self.numberRowCard,
                ft.Container(padding=10),
                self.punctuationRowCard,
                ft.Container(padding=10),
                self.freeTypingRowCard,
            ]
        )

        self.returnBtn = ft.ElevatedButton(
            "Return",
            on_click=lambda _: self.page.go("/"),
        )

        self.pageContent = ft.ListView(
            controls=[
                ft.Container(self.pageHeader),
                ft.Divider(thickness=10),
                ft.Container(padding=10),
                ft.Container(self.LessonContainer),
                ft.Container(padding=10),
                ft.Container(self.returnBtn),
            ],
        )
        self.pageContent.alignment = ft.alignment.center

    def page_resize(self, e):
        self.pageContent.alignment = ft.alignment.center

    def build(self):
        return self.pageContent
