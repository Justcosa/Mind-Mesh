import flet as ft
from utils.colors import customTextcolor2

class startup(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        def go_to_log_window(e):
            page.go("/logWindow")

        def go_to_history(e):
            page.go("/history")

        def go_to_resources(e):
            page.go("/resources")

        def go_to_stats(e):
            page.go("/statsPage")

        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,  # Center horizontally
            vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Center vertically
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,  # Center vertically in column
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center horizontally in column
                        controls=[
                            ft.Text("Welcome back!", color=customTextcolor2, size=30, weight=ft.FontWeight.BOLD),
                            ft.ElevatedButton("New Entry", on_click=go_to_log_window),
                            ft.ElevatedButton("History", on_click=go_to_history),
                            ft.ElevatedButton("Resources", on_click=go_to_resources),
                            ft.ElevatedButton("Statistics", on_click=go_to_stats)
                        ]
                    )
                )
            ]
        )
