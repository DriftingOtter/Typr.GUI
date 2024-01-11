import flet as ft
import plotly.express as px
from flet.plotly_chart import PlotlyChart


class Profile(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.initialize_page_settings()
        self.create_page_controls()

    def initialize_page_settings(self):
        self.page.title = "Typr: Profile"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.scroll = ft.ScrollMode.HIDDEN
        self.page.on_resize = self.page_resize

    def create_page_controls(self):
        self.pageHeader = self.create_page_header()
        self.personalBestsBoard = self.create_personal_bests_board()
        self.tests_data_file = px.data.gapminder().query("continent=='Oceania'")
        self.wpm_figure, self.acc_figure, self.ttk_figure = self.create_figures()
        self.profile_figure_container = self.create_profile_figure_container()
        self.player_name_card = self.create_player_card("N/A", "N/A")
        self.player_level_card = self.create_player_card("Typist Level", "Level: N/A")
        self.time_played_card = self.create_player_card("Time Played", "Time: N/A")
        self.return_btn = ft.ElevatedButton(
            "Return", on_click=lambda _: self.page.go("/lessons")
        )
        self.logout_btn = ft.ElevatedButton(
            "Logout", on_click=lambda _: self.page.go("/")
        )

        self.pageContent = ft.ListView(
            controls=[
                self.pageHeader,
                ft.Divider(thickness=10),
                ft.Container(padding=20),
                self.player_name_card,
                ft.Container(padding=20),
                self.player_level_card,
                ft.Container(padding=20),
                self.time_played_card,
                ft.Container(padding=20),
                ft.Container(
                    self.personalBestsBoard, padding=ft.padding.only(bottom=20)
                ),
                ft.Container(padding=10),
                self.profile_figure_container,
                ft.Container(padding=20),
                ft.Container(self.return_btn),
                ft.Container(padding=10),
                ft.Container(self.logout_btn),
            ]
        )
        self.pageContent.alignment = ft.alignment.center

    def create_page_header(self):
        return ft.Row(
            controls=[
                ft.Image(
                    src="images/Astro_Typing.png", height=300, fit=ft.ImageFit.FIT_WIDTH
                ),
                ft.Container(
                    ft.Text(
                        "Profile",
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

    def create_personal_bests_board(self):
        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Words Per Minute"), numeric=True),
                ft.DataColumn(ft.Text("Accuracy"), numeric=True),
                ft.DataColumn(ft.Text("Time Taken"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("N/A")),
                        ft.DataCell(ft.Text("N/A")),
                        ft.DataCell(ft.Text("N/A")),
                    ]
                ),
            ],
        )

    def create_figures(self):
        wpm_figure = px.line(self.tests_data_file, x="pop", y="year", color="iso_num")
        acc_figure = px.line(self.tests_data_file, x="pop", y="year", color="iso_num")
        ttk_figure = px.line(self.tests_data_file, x="pop", y="year", color="iso_num")
        return wpm_figure, acc_figure, ttk_figure

    def create_profile_figure_container(self):
        return ft.Container(
            ft.Row(
                controls=[
                    ft.Container(
                        PlotlyChart(self.wpm_figure, expand=False, original_size=False),
                        width=800,
                        height=500,
                    ),
                    ft.Container(padding=10),
                    ft.Container(
                        PlotlyChart(self.acc_figure, expand=False, original_size=False),
                        width=800,
                        height=500,
                    ),
                    ft.Container(padding=10),
                    ft.Container(
                        PlotlyChart(self.ttk_figure, expand=False, original_size=False),
                        width=800,
                        height=500,
                    ),
                ]
            )
        )

    def create_player_card(self, title, subtitle):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text(title, size=40),
                            subtitle=ft.Text(subtitle, size=20),
                        ),
                    ]
                ),
                width=800,
                padding=10,
            )
        )

    def page_resize(self, e):
        self.pageContent.alignment = ft.alignment.center

    def build(self):
        return self.pageContent
