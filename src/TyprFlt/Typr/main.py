import flet as ft
from views import views_event_handler

def main(page: ft.Page):
    initialize_page_settings(page)
    set_theme(page)
    setup_page_layout(page)

    # =============================
    # Route Change Event Handling
    # =============================
    def route_change(route):
        print(f"Current Page Route: {page.route}")
        clear_and_load_view(page)

    page.on_route_change = route_change
    page.go("/")

def initialize_page_settings(page):
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.HIDDEN

def set_theme(page):
    page.theme = ft.theme.Theme(
        color_scheme_seed="#33bef4",
    )
    page.theme_mode = ft.ThemeMode.DARK

def setup_page_layout(page):
    theme = ft.Theme()
    page.theme_transitions = ft.PageTransitionTheme.FADE_UPWARDS
    page.theme_mode = ft.ThemeMode.DARK

def clear_and_load_view(page):
    page.views.clear()
    page.views.append(views_event_handler(page)[page.route])

ft.app(target=main)

