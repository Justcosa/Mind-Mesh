import flet as ft
import os
from mplib.stats import plot_logs_per_month
from utils.colors import customBgColor, customTextcolor2

class statsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.bgcolor = customBgColor

        def go_to_startup(e):
            page.go("/startup")

        # Generate and save the plot as an image
        img_path = "statPics/logs_per_month.png"
        plot_logs_per_month()  # This will save the image to img_path

        # Check if the image exists before displaying
        image_control = (
            ft.Image(src=img_path, width=600, height=300, fit=ft.ImageFit.CONTAIN)
            if os.path.exists(img_path)
            else ft.Text("No statistics available.", color="red")
        )

        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Logs per Month", color=customTextcolor2, size=30, weight=ft.FontWeight.BOLD),
                            image_control,
                            ft.ElevatedButton("Back to Startup", on_click=go_to_startup)
                        ]
                    )
                )
            ]
        )
