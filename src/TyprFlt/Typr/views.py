import flet as ft
from pages.landing import Landing
from pages.signup import Signup
from pages.login import Login
from pages.lessons import Lessons
from pages.profile import Profile
from pages.freeTyping import FreeTyping
from pages.homeRow import HomeTyping
from pages.topRow import TopTyping
from pages.bottomRow import BottomTyping
from pages.numberRow import NumberTyping
from pages.punctuation import PunctuationTyping

def views_event_handler(page):
    return {
        "/": ft.View(route="/", controls=[Landing(page)]),
        "/signup": ft.View(route="/signup", controls=[Signup(page)]),
        "/login": ft.View(route="/login", controls=[Login(page)]),
        "/lessons": ft.View(route="/lessons", controls=[Lessons(page)]),
        "/profile": ft.View(route="/profile", controls=[Profile(page)]),
        "/homeRow": ft.View(route="/homeRow", controls=[HomeTyping(page)]),
        "/topRow": ft.View(route="/topRow", controls=[TopTyping(page)]),
        "/bottomRow": ft.View(route="/bottomRow", controls=[BottomTyping(page)]),
        "/numberRow": ft.View(route="/numberRow", controls=[NumberTyping(page)]),
        "/punctuationRow": ft.View(route="/punctuationRow", controls=[PunctuationTyping(page)]),
        "/freeTyping": ft.View(route="/freeTyping", controls=[FreeTyping(page)]),

    }
