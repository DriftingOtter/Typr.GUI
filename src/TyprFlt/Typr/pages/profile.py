import flet as ft
import plotly.express as px
from flet.plotly_chart import PlotlyChart
from .ottrDBM import OttrDBM
import pickle


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

        self.dbConfig = {
            "user": "root",
            "password": "",
            "host": "localhost",
            "database": "typr_acc_info",
            "raise_on_warnings": True,
        }
        self.dbManager = OttrDBM(self.dbConfig)

        self.load_user_data()

    def load_user_data(self):
        try:
            with open("data.pkl", "rb") as file:
                self.loaded_data = pickle.load(file)
                self.currentUser = self.loaded_data

            self.userPersonalBestResults = self.find_pb()
            self.userPersonalBestWPM, self.userPersonalBestACC, self.userPersonalBestTTK = self.userPersonalBestResults
            self.totalTime = self.find_total_time()
            self.currentUserUID = self.find_uid()

        except (FileNotFoundError, pickle.UnpicklingError) as e:
            self.handle_file_or_unpickling_error(e)

        except Exception as e:
            self.handle_unexpected_error(e)

    def handle_file_or_unpickling_error(self, error):
        print(f"Error: {error}")
        self.userPersonalBestResults = "N/A", "N/A", "N/A"
        self.userPersonalBestWPM, self.userPersonalBestACC, self.userPersonalBestTTK = self.userPersonalBestResults
        self.totalTime = "N/A"
        self.currentUserUID = self.find_uid()

    def handle_unexpected_error(self, error):
        print(f"An unexpected error occurred: {str(error)}")
        self.userPersonalBestResults = "N/A", "N/A", "N/A"
        self.userPersonalBestWPM, self.userPersonalBestACC, self.userPersonalBestTTK = self.userPersonalBestResults
        self.totalTime = "N/A"
        self.currentUserUID = self.find_uid()

    def create_page_controls(self):
        self.pageHeader = self.create_page_header()
        self.personalBestsBoard = self.create_personal_bests_board(
            self.userPersonalBestWPM, self.userPersonalBestACC, self.userPersonalBestTTK
        )
        self.wpm_figure, self.acc_figure, self.ttk_figure = self.create_figures()
        self.profile_figure_container = self.create_profile_figure_container()
        self.player_name_card = self.create_player_card(
            "Typist, welcome back!", f"{self.currentUserUID}"
        )
        self.time_played_card = self.create_player_card(
            "Time Played", f"Time: {self.totalTime}"
        )
        self.return_btn = ft.ElevatedButton(
            "Return", on_click=lambda _: self.page.go("/lessons")
        )
        self.logout_btn = ft.ElevatedButton(
            "Logout", on_click=lambda _: self.page.go("/")
        )

        self.dbGraphBannerFail = ft.Banner(
            bgcolor=ft.colors.AMBER_100,
            leading=ft.Icon(
                ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40
            ),
            content=ft.Text("Oops, could not create a graph from user data to the database."),
            actions=[
                ft.TextButton("Close", on_click=self.fail_close_banner),
            ],
        )

        self.dbGraphBannerPass = ft.Banner(
            bgcolor=ft.colors.GREEN,
            leading=ft.Icon(ft.icons.CHECK, color=ft.colors.GREEN, size=40),
            content=ft.Text(
                "Great, successfully created a graph from user data to the database."
            ),
            actions=[
                ft.TextButton("Close", on_click=self.pass_close_banner),
            ],
        )

        self.pageContent = ft.ListView(
            controls=[
                self.pageHeader,
                ft.Divider(thickness=10),
                ft.Container(padding=20),
                self.player_name_card,
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

    def create_personal_bests_board(self, wpm="N/A", acc="N/A", ttk="N/A"):
        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Words Per Minute"), numeric=True),
                ft.DataColumn(ft.Text("Accuracy"), numeric=True),
                ft.DataColumn(ft.Text("Time Taken"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(wpm)),
                        ft.DataCell(ft.Text(acc)),
                        ft.DataCell(ft.Text(ttk)),
                    ]
                ),
            ],
        )

    def create_figures(self):
        try:
            wpm_figure = self.plot_figure("wpm", "WPM over Time")
            acc_figure = self.plot_figure("acc", "Accuracy over Time")
            ttk_figure = self.plot_figure("ttk", "TTK over Time")

            return wpm_figure, acc_figure, ttk_figure

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

        return None, None, None  # Return None for all figures in case of an error

    def find_pb(self):
        try:
            self.pbScore = self.dbManager.find_personal_best(self.currentUser)
            return self.pbScore

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

        return "N/A", "N/A", "N/A"

    def find_total_time(self):
        try:
            self.totalTime = self.dbManager.find_total_time_played(self.currentUser)
            return self.totalTime

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

        return "N/A"

    def find_uid(self):
        return self.currentUser

    def create_profile_figure_container(self):
        return ft.Container(
            ft.Row(
                controls=[
                    self.create_plot_container("wpm", "WPM over Time", 800, 500),
                    ft.Container(padding=10),
                    self.create_plot_container("acc", "Accuracy over Time", 800, 500),
                    ft.Container(padding=10),
                    self.create_plot_container("ttk", "TTK over Time", 800, 500),
                ]
            )
        )

    def create_plot_container(self, feature, title, width, height):
        data = self.dbManager.fetch_data_for_plot(feature, self.currentUser)
        if data:
            fig = px.scatter(data, x="date", y=feature, title=title)
            return ft.Container(
                PlotlyChart(fig, expand=False, original_size=False),
                width=width,
                height=height,
            )

        return ft.Container()

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

    def plot_figure(self, feature, plot_title):
        data = self.dbManager.fetch_data_for_plot(feature, self.currentUser)
        if data:
            fig = px.scatter(data, x="date", y=feature, title=plot_title)
            return fig

        return None

    def pass_close_banner(self, e):
        self.dbGraphBannerPass.open = False
        self.page.update()

    def fail_close_banner(self, e):
        self.dbGraphBannerFail.open = False
        self.page.update()

    def page_resize(self, e):
        self.pageContent.alignment = ft.alignment.center

    def build(self):
        return self.pageContent

