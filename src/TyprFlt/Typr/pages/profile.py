import flet as ft
import plotly.express as px
from flet.plotly_chart import PlotlyChart


class Profile(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        page.title = "Typr: Profile"

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

        self.personalBestsBoard = ft.DataTable(
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
                    ],
                ),
            ],
        )

        self.testsDataFile = px.data.gapminder().query("continent=='Oceania'")

        self.wpmFigure = px.line(self.testsDataFile, x="pop", y="year", color="iso_num")
        self.accFigure = px.line(self.testsDataFile, x="pop", y="year", color="iso_num")
        self.ttkFigure = px.line(self.testsDataFile, x="pop", y="year", color="iso_num")

        self.profileFigureContainer = ft.Container(
            ft.Row(
                controls=[
                    ft.Container(
                        PlotlyChart(self.wpmFigure, expand=False, original_size=False),
                        width=800,
                        height=500,
                    ),
                    ft.Container(padding=10),
                    ft.Container(
                        PlotlyChart(self.accFigure, expand=False, original_size=False),
                        width=800,
                        height=500,
                    ),
                    ft.Container(padding=10),
                    ft.Container(
                        PlotlyChart(self.ttkFigure, expand=False, original_size=False),
                        width=800,
                        height=500,
                    ),
                ]
            )
        )

        self.playerNameCard = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("N/A", size=40),
                        ),
                    ]
                ),
                width=800,
                padding=10,
            )
        )

        self.playerLevelCard = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Typist Level", size=40),
                            subtitle=ft.Text(
                                "Level: N/A",
                                size=20,
                            ),
                        ),
                    ]
                ),
                width=800,
                padding=10,
            )
        )

        self.timePlayedCard = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Time Played", size=40),
                            subtitle=ft.Text(
                                "Time: N/A",
                                size=20,
                            ),
                        ),
                    ]
                ),
                width=800,
                padding=10,
            )
        )

        self.returnBtn = ft.ElevatedButton(
            "Return",
            on_click=lambda _: self.page.go("/lessons"),
        )

        self.logoutBtn = ft.ElevatedButton(
            "Logout",
            on_click=lambda _: self.page.go("/"),
        )

        self.pageContent = ft.ListView(
            controls=[
                ft.Container(self.pageHeader),
                ft.Divider(thickness=10),
                ft.Container(padding=20),
                ft.Container(self.playerNameCard),
                ft.Container(padding=20),
                ft.Container(self.playerLevelCard),
                ft.Container(padding=20),
                ft.Container(self.timePlayedCard),
                ft.Container(padding=20),
                ft.Container(
                    self.personalBestsBoard, padding=ft.padding.only(bottom=20)
                ),
                ft.Container(padding=10),
                ft.Container(self.profileFigureContainer),
                ft.Container(padding=20),
                ft.Container(self.returnBtn),
                ft.Container(padding=10),
                ft.Container(self.logoutBtn),
            ],
        )
        self.pageContent.alignment = ft.alignment.center

    def page_resize(self, e):
        self.pageContent.alignment = ft.alignment.center

    def build(self):
        return self.pageContent
