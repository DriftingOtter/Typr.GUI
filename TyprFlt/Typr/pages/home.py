import flet as ft

class Home(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        page.title = "Typr: Your Personal Typing Tutor"

        page.theme = ft.theme.Theme(
            color_scheme_seed="blue",
            font_family="JetBrainsMono Nerd Font, Arial",
        )

        page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.scroll = ft.ScrollMode.HIDDEN

        # ==============
        # Page Controls
        # ==============
        self.pageHeader = ft.Row(
            controls=[
                ft.Image(
                    src="images/Astro_Typing.png",
                    height=200,
                    fit=ft.ImageFit.FIT_WIDTH,
                ),
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

        #self.typingForwarderBtn = ft.ElevatedButton(
            #"Go To Typing Page",
            #on_click=lambda _: self.page.go("/typingtest"),
        #)

        self.signupBtn = ft.ElevatedButton(
            "Signup",
            on_click=lambda _: self.page.go("/signup"),
        )

        self.loginBtn = ft.ElevatedButton(
            "Login",
            on_click=lambda _: self.page.go("/login"),
        )

        self.whyUseTyprHeading = ft.Text(
            "Why Use Typr?",
            style=ft.TextThemeStyle.HEADLINE_LARGE,
            text_align=ft.TextAlign.JUSTIFY,
            weight=ft.FontWeight.BOLD,
            italic=True,
        )

        self.whyUseTyprBody = ft.Text(
            "In an era driven by efficient communication and productivity, the mastery of touch typing has become paramount. Enter Typr, an innovative website poised to revolutionize your typing skills. Through immersive interactive lessons and advanced visual feedback, Typr empowers professionals, academia students, & more to unlock their full typing potential like never before!",
            style=ft.TextThemeStyle.HEADLINE_SMALL,
            text_align=ft.TextAlign.JUSTIFY,
        )

        self.keyboardIMG = ft.Image(
            src="images/Red_Keyboard.jpg",
            height=200,
            fit=ft.ImageFit.FIT_WIDTH,
        )

        self.elevateProfileHeading = ft.Text(
            "1 | Elevate Your Professional Profile",
            style=ft.TextThemeStyle.HEADLINE_LARGE,
            text_align=ft.TextAlign.JUSTIFY,
            weight=ft.FontWeight.BOLD,
        )

        self.elevateProfileBody = ft.Text(
            "In the competitive landscape of professionals and academia, possessing impeccable typing skills sets you apart from the rest. With Typr as your trusted companion, bid farewell to the inefficiencies of the hunt-and-peck method, and embrace the realm of touch typing expertise. Enhance your professional profile, boost productivity, and amplify your success with the unrivaled typing proficiency achieved through Typr.",
            style=ft.TextThemeStyle.HEADLINE_SMALL,
            text_align=ft.TextAlign.JUSTIFY,
        )

        self.learningIMG = ft.Image(
            src="images/Computer_Learning.jpg",
            height=200,
            fit=ft.ImageFit.FIT_WIDTH,
        )

        self.immersiveLessonsHeading = ft.Text(
            "2 | Immersive Interactive Lessons",
            style=ft.TextThemeStyle.HEADLINE_LARGE,
            text_align=ft.TextAlign.JUSTIFY,
            weight=ft.FontWeight.BOLD,
        )

        self.immersiveLessonsHeadingBody = ft.Text(
            "Typr offers a transformative learning experience that immerses you in a world of interactive lessons specifically designed for professionals and academia students. Seamlessly blending theory with practice, Typr guides you through a comprehensive curriculum, ensuring a holistic grasp of touch typing fundamentals. Prepare to witness remarkable progress as you engage with immersive exercises, honing your skills under Typr's expert guidance.",
            style=ft.TextThemeStyle.HEADLINE_SMALL,
            text_align=ft.TextAlign.JUSTIFY,
        )

        self.laptopIMG = ft.Image(
            src="images/Typing_On_Screen.jpg",
            height=200,
            fit=ft.ImageFit.FIT_WIDTH,
        )

        self.visualFeedbackHeading = ft.Text(
            "3 | Advanced Visual Feedback Mechanisms",
            style=ft.TextThemeStyle.HEADLINE_LARGE,
            text_align=ft.TextAlign.JUSTIFY,
            weight=ft.FontWeight.BOLD,
        )

        self.visualFeedbackBody = ft.Text(
            "At Typr, we understand that visual feedback is a catalyst for growth and improvement. Our state-of-the-art platform provides real-time visual emulation of your typing actions, enabling you to observe your performance with exceptional clarity. From keystroke accuracy to typing speed, every nuance of your progress is meticulously showcased, allowing you to fine-tune your skills and reach new heights of typing proficiency.",
            style=ft.TextThemeStyle.HEADLINE_SMALL,
            text_align=ft.TextAlign.JUSTIFY,
        )

    def build(self):
        return ft.ListView(
            controls=[
                self.pageHeader,
                ft.Container(padding=10),
                self.signupBtn,
                ft.Divider(),
                self.loginBtn,
                ft.Container(padding=15),
                self.whyUseTyprHeading,
                ft.Container(padding=10),
                self.whyUseTyprBody,
                ft.Container(padding=15),
                self.keyboardIMG,
                ft.Container(padding=15),
                self.elevateProfileHeading,
                ft.Container(padding=10),
                self.elevateProfileBody,
                ft.Container(padding=15),
                self.learningIMG,
                ft.Container(padding=15),
                self.immersiveLessonsHeading,
                ft.Container(padding=10),
                self.elevateProfileBody,
                ft.Container(padding=15),
                self.laptopIMG,
                ft.Container(padding=15),
                self.visualFeedbackHeading,
                ft.Container(padding=10),
                self.visualFeedbackBody,
                ft.Container(padding=15),
            ],
            expand=True,
            padding=ft.padding.only(top=20, bottom=20, left=20, right=20),
        )
