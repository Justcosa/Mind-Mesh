import flet as ft

class startup(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        page.window_width = 800
        page.window_height = 600
        page.update()

        def go_to_log_window(e):
            page.go("/logWindow")

        def go_to_history(e):
            page.go("/history")

        def go_to_resources(e):
            page.go("/resources")

        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Welcome back!", color="black", size=30, weight=ft.FontWeight.BOLD),
                            ft.ElevatedButton("New Entry", on_click=go_to_log_window),
                            ft.ElevatedButton("History", on_click=go_to_history),
                            ft.ElevatedButton("Resources", on_click=go_to_resources)
                        ]
                    )
                )
            ]
        )

    #def route_change(self, route):
        # Handle route changes here if needed
        #pass