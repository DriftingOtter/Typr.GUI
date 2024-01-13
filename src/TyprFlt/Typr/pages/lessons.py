import flet as ft

class Lessons(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.initialize_page_settings()

        self.create_page_header("Lessons")

        self.home_row_card = self.create_lesson_card(
            "Home Row Lesson",
            "Learn the basic of typing by learning the row in which your hands lay.",
            "/homeRow"
        )

        self.top_row_card = self.create_lesson_card(
            "Top Row Lesson",
            "Learn the top row and its intricacies.",
            "/topRow"
        )

        self.bottom_row_card = self.create_lesson_card(
            "Bottom Row Lesson",
            "Learn the bottom row. Let's see what you got!",
            "/bottomRow"
        )

        self.number_row_card = self.create_lesson_card(
            "Number Row Lesson",
            "Learn the basics of typing on the number row. 1..2..3.. Let's Go!",
            "/numberRow"
        )

        self.punctuation_row_card = self.create_lesson_card(
            "Punctuation Row Lesson",
            "Learn how to utilize punctuation in your typing! Let's see what you can do.",
            "/punctuationRow"
        )

        self.free_typing_card = self.create_lesson_card(
            "Free Typing / Typing Test",
            "The final lesson! Let's try out your skills with a whole keyboard test.",
            "/freeTyping"
        )

        self.profile_page_card = self.create_card(
            title="Profile Page",
            subtitle="Go To Profile Page",
            on_click=lambda _: self.page.go("/profile"),
            size=20,
            is_profile_card=True
        )

        self.lesson_container = ft.ListView(
            controls=[
                self.home_row_card,
                ft.Container(padding=10),
                self.top_row_card,
                ft.Container(padding=10),
                self.bottom_row_card,
                ft.Container(padding=10),
                self.number_row_card,
                ft.Container(padding=10),
                self.punctuation_row_card,
                ft.Container(padding=10),
                self.free_typing_card,
            ]
        )

        self.return_btn = ft.ElevatedButton(
            "Return",
            on_click=lambda _: self.page.go("/"),
        )

        self.page_content = ft.ListView(
            controls=[
                ft.Container(self.page_header),
                ft.Divider(thickness=10),
                ft.Container(padding=10),
                ft.Container(self.lesson_container),
                ft.Container(padding=10),
                ft.Divider(thickness=5),
                ft.Container(padding=10),
                ft.Container(self.profile_page_card),
                ft.Container(padding=20),
                ft.Container(self.return_btn),
            ],
        )
        self.page_content.alignment = ft.alignment.center

    def initialize_page_settings(self):
        self.page.title = "Typr: Your Personal Typing Tutor"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.scroll = ft.ScrollMode.HIDDEN
        self.page.on_resize = self.page_resize

    def create_page_header(self, title):
        self.page_header = ft.Row(
            controls=[
                ft.Image(
                    src="images/Astro_Typing.png",
                    height=300,
                    fit=ft.ImageFit.FIT_WIDTH,
                ),
                ft.Container(
                    ft.Text(
                        title,
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

    def create_lesson_card(self, title, subtitle, route):
        return self.create_card(
            title=title,
            subtitle=subtitle,
            on_click=lambda _: self.page.go(route)
        )

    def create_card(self, title, subtitle, on_click=None, size=None, is_profile_card=False):
        button_text = "Go To Profile" if is_profile_card else "Start Lesson"
        
        card_content = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text(title, size=size),
                        subtitle=ft.Text(subtitle),
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                button_text,
                                on_click=on_click
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
        return ft.Card(content=card_content)

    def page_resize(self, e):
        self.page_content.alignment = ft.alignment.center

    def build(self):
        return self.page_content

