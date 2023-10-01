import flet as ft
from pages.home import Home
from pages.typingtest import Typing
from pages.signup import Signup
from pages.login import Login

def views_event_handler(page):
    return {
        "/": ft.View(route="/", controls=[Home(page)]),
        "/typingtest": ft.View(route="/typingtest", controls=[Typing(page)]),
        "/signup": ft.View(route="/signup", controls=[Signup(page)]),
        "/login": ft.View(route="/login", controls=[Login(page)]),
    }
