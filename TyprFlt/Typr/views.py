import flet as ft
from pages.home import Home
from pages.typingtest import Typing

def views_event_handler(page):
    return {
        "/": ft.View(route="/", controls=[Home(page)]),
        "/typingtest": ft.View(route="/typingtest", controls=[Typing(page)]),
    }
