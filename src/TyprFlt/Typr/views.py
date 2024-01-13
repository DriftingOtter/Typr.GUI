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
        "/": create_view(Landing, page),
        "/signup": create_view(Signup, page),
        "/login": create_view(Login, page),
        "/lessons": create_view(Lessons, page),
        "/profile": create_view(Profile, page),
        "/homeRow": create_view(HomeTyping, page),
        "/topRow": create_view(TopTyping, page),
        "/bottomRow": create_view(BottomTyping, page),
        "/numberRow": create_view(NumberTyping, page),
        "/punctuationRow": create_view(PunctuationTyping, page),
        "/freeTyping": create_view(FreeTyping, page),
    }

def create_view(page_class, page):
    return ft.View(route=page_class.__name__, controls=[page_class(page)])

