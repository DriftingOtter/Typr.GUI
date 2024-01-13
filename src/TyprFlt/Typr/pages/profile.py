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

        try:
            self.userPersonalBestResults = self.find_pb()
            self.userPersonalBestWPM = self.userPersonalBestResults[0]
            self.userPersonalBestACC = self.userPersonalBestResults[1]
            self.userPersonalBestTTK = self.userPersonalBestResults[2]

            self.totalTime = self.find_total_time()

            self.currentUserUID = self.find_uid()
        except TypeError:
            self.userPersonalBestResults = "N/A"
            self.userPersonalBestWPM = "N/A"
            self.userPersonalBestACC = "N/A"
            self.userPersonalBestTTK = "N/A"

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
            "Time Played", f"Time:{self.totalTime}"
        )
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

        self.dbGraphBannerFail = ft.Banner(
            bgcolor=ft.colors.AMBER_100,
            leading=ft.Icon(
                ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40
            ),
            content=ft.Text("Oops, could not create graph from user data to database."),
            actions=[
                ft.TextButton("Close", on_click=self.fail_close_banner),
            ],
        )

        self.dbGraphBannerPass = ft.Banner(
            bgcolor=ft.colors.GREEN,
            leading=ft.Icon(ft.icons.CHECK, color=ft.colors.GREEN, size=40),
            content=ft.Text(
                "Great, successfully created graph from user data to database."
            ),
            actions=[
                ft.TextButton("Close", on_click=self.pass_close_banner),
            ],
        )

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
            with open("data.pkl", "rb") as file:
                self.loaded_data = pickle.load(file)
                self.currentUser = self.loaded_data

            wpm_figure = self.plot_wpm_date(self.currentUser)
            acc_figure = self.plot_acc_date(self.currentUser)
            ttk_figure = self.plot_ttk_date(self.currentUser)

            return wpm_figure, acc_figure, ttk_figure

        except FileNotFoundError:
            # Handle the case where the file is not found
            print("Error: File 'data.pkl' not found.")

        except pickle.UnpicklingError:
            # Handle the case where there is an issue with unpickling (corrupted file)
            print(
                "Error: Unable to unpickle data from 'data.pkl'. File might be corrupted."
            )

        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"An unexpected error occurred: {str(e)}")

        return None, None, None  # Return None for all figures in case of an error

    def find_pb(self):
        try:
            with open("data.pkl", "rb") as file:
                self.loaded_data = pickle.load(file)
                self.currentUser = self.loaded_data

                self.pbScore = self.dbManager.find_personal_best(self.currentUser)

            return self.pbScore

        except FileNotFoundError:
            # Handle the case where the file is not found
            print("Error: File 'data.pkl' not found.")

        except pickle.UnpicklingError:
            # Handle the case where there is an issue with unpickling (corrupted file)
            print(
                "Error: Unable to unpickle data from 'data.pkl'. File might be corrupted."
            )

        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"An unexpected error occurred: {str(e)}")

        return None, None, None

    def find_total_time(self):
        try:
            with open("data.pkl", "rb") as file:
                self.loaded_data = pickle.load(file)
                self.currentUser = self.loaded_data

                self.totalTime = self.dbManager.find_total_time_played(self.currentUser)

            return self.totalTime

        except FileNotFoundError:
            # Handle the case where the file is not found
            print("Error: File 'data.pkl' not found.")

        except pickle.UnpicklingError:
            # Handle the case where there is an issue with unpickling (corrupted file)
            print(
                "Error: Unable to unpickle data from 'data.pkl'. File might be corrupted."
            )

        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"An unexpected error occurred: {str(e)}")

        return None, None, None

    def find_uid(self):
        try:
            with open("data.pkl", "rb") as file:
                self.loaded_data = pickle.load(file)
                self.currentUser = self.loaded_data
            return self.currentUser

        except FileNotFoundError:
            # Handle the case where the file is not found
            print("Error: File 'data.pkl' not found.")

        except pickle.UnpicklingError:
            # Handle the case where there is an issue with unpickling (corrupted file)
            print(
                "Error: Unable to unpickle data from 'data.pkl'. File might be corrupted."
            )

        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"An unexpected error occurred: {str(e)}")

        return None, None, None

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

    def plot_wpm_date(self, uid):
        self.data = self.dbManager.fetch_data_for_plot("wpm", uid)
        if self.data:
            self.fig = px.scatter(self.data, x="date", y="wpm", title="WPM over Time")
            return self.fig

    def plot_acc_date(self, uid):
        self.data = self.dbManager.fetch_data_for_plot("acc", uid)
        if self.data:
            self.fig = px.scatter(
                self.data, x="date", y="acc", title="Accuracy over Time"
            )
            return self.fig

    def plot_ttk_date(self, uid):
        self.data = self.dbManager.fetch_data_for_plot("ttk", uid)
        if self.data:
            self.fig = px.scatter(self.data, x="date", y="ttk", title="TTK over Time")
            return self.fig

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
