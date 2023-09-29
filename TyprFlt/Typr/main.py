import flet as ft
from views import views_event_handler


def main(page: ft.Page):
    # =============================
    # Route Change Event Handeling
    # =============================
    def route_change(route):
        print(f"Current Page Route:{page.route}")
        page.views.clear()
        page.views.append(views_event_handler(page)[page.route])

    page.on_route_change = route_change
    page.go("/")


ft.app(target=main, use_color_emoji=True)
