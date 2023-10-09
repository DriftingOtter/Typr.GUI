import flet as ft
from views import views_event_handler


def main(page: ft.Page):

    theme = ft.Theme()

    page.theme = ft.theme.Theme(
            color_scheme_seed="#33bef4",
        )

    theme.page_transitions = ft.PageTransitionTheme.FADE_UPWARDS
    page.theme_mode = ft.ThemeMode.DARK

    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.scroll = ft.ScrollMode.HIDDEN

    # =============================
    # Route Change Event Handeling
    # =============================
    def route_change(route):
        print(f"Current Page Route:{page.route}")
        page.views.clear()
        page.views.append(views_event_handler(page)[page.route])

    page.on_route_change = route_change
    page.go("/")


ft.app(target=main)
