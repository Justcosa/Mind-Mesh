import flet as ft
from router import views_handler

def main(page: ft.Page):
    page.window_resizable = False
    page.title = "Mind Mesh"

    def route_change(route):
        page.views[-1] = views_handler(page)[page.route]
        page.update()

    page.on_route_change = route_change
    page.go("/startup")

ft.app(target=main, view=ft.FLET_APP)
