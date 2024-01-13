import flet as ft

class Landing(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.initialize_page_settings()
        self.initialize_page_controls()

    def initialize_page_settings(self):
        self.page.title = "Typr: Your Personal Typing Tutor"
        self.page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.scroll = ft.ScrollMode.HIDDEN

    def initialize_page_controls(self):
        self.page_header = self.create_page_header()
        self.signup_btn = ft.ElevatedButton("Signup", on_click=lambda _: self.page.go("/signup"))
        self.login_btn = ft.ElevatedButton("Login", on_click=lambda _: self.page.go("/login"))
        self.why_use_typr_heading = self.create_heading("Why Use Typr?")
        self.why_use_typr_body = self.create_text(
            "In an era driven by efficient communication and productivity, the mastery of touch typing has become paramount. Enter Typr, an innovative website poised to revolutionize your typing skills. Through immersive interactive lessons and advanced visual feedback, Typr empowers professionals, academia students, & more to unlock their full typing potential like never before!"
        )
        self.keyboard_img = self.create_image("images/Red_Keyboard.jpg")
        self.elevate_profile_heading = self.create_heading("1 | Elevate Your Professional Profile")
        self.elevate_profile_body = self.create_text(
            "In the competitive landscape of professionals and academia, possessing impeccable typing skills sets you apart from the rest. With Typr as your trusted companion, bid farewell to the inefficiencies of the hunt-and-peck method, and embrace the realm of touch typing expertise. Enhance your professional profile, boost productivity, and amplify your success with the unrivaled typing proficiency achieved through Typr."
        )
        self.learning_img = self.create_image("images/Computer_Learning.jpg")
        self.immersive_lessons_heading = self.create_heading("2 | Immersive Interactive Lessons")
        self.immersive_lessons_body = self.create_text(
            "Typr offers a transformative learning experience that immerses you in a world of interactive lessons specifically designed for professionals and academia students. Seamlessly blending theory with practice, Typr guides you through a comprehensive curriculum, ensuring a holistic grasp of touch typing fundamentals. Prepare to witness remarkable progress as you engage with immersive exercises, honing your skills under Typr's expert guidance."
        )
        self.laptop_img = self.create_image("images/Typing_On_Screen.jpg")
        self.visual_feedback_heading = self.create_heading("3 | Advanced Visual Feedback Mechanisms")
        self.visual_feedback_body = self.create_text(
            "At Typr, we understand that visual feedback is a catalyst for growth and improvement. Our state-of-the-art platform provides real-time visual emulation of your typing actions, enabling you to observe your performance with exceptional clarity. From keystroke accuracy to typing speed, every nuance of your progress is meticulously showcased, allowing you to fine-tune your skills and reach new heights of typing proficiency."
        )

    def create_page_header(self):
        return ft.Row(
            controls=[
                self.create_image("images/Astro_Typing.png", height=200, fit=ft.ImageFit.FIT_WIDTH),
                ft.Container(
                    ft.Text(
                        "Typr: Your Personal Typing Tutor",
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

    def create_heading(self, text):
        return ft.Text(
            text,
            style=ft.TextThemeStyle.HEADLINE_LARGE,
            text_align=ft.TextAlign.JUSTIFY,
            weight=ft.FontWeight.BOLD,
            italic=True,
        )

    def create_text(self, text):
        return ft.Text(
            text,
            style=ft.TextThemeStyle.HEADLINE_SMALL,
            text_align=ft.TextAlign.JUSTIFY,
        )

    def create_image(self, src, height=200, fit=ft.ImageFit.FIT_WIDTH):
        return ft.Image(
            src=src,
            height=height,
            fit=fit,
        )

    def build(self):
        return ft.ListView(
            controls=[
                self.page_header,
                ft.Container(padding=10),
                self.signup_btn,
                ft.Divider(),
                self.login_btn,
                ft.Container(padding=15),
                self.why_use_typr_heading,
                ft.Container(padding=10),
                self.why_use_typr_body,
                ft.Container(padding=15),
                self.keyboard_img,
                ft.Container(padding=15),
                self.elevate_profile_heading,
                ft.Container(padding=10),
                self.elevate_profile_body,
                ft.Container(padding=15),
                self.learning_img,
                ft.Container(padding=15),
                self.immersive_lessons_heading,
                ft.Container(padding=10),
                self.elevate_profile_body,
                ft.Container(padding=15),
                self.laptop_img,
                ft.Container(padding=15),
                self.visual_feedback_heading,
                ft.Container(padding=10),
                self.visual_feedback_body,
                ft.Container(padding=15),
            ],
            expand=True,
            padding=ft.padding.only(top=20, bottom=20, left=20, right=20),
        )

