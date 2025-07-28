import flet as ft
import requests
from utils.colors import customBgColor, customTextcolor2

class history(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.bgcolor = customBgColor
        self.selected_entry = None
        self.alert_dialog = ft.AlertDialog(title=ft.Text(""), content=ft.Text(""))

        def go_to_startup(e):
            page.go("/startup")

        def load_entries():
            try:
                response = requests.get("http://localhost:8081/journals/")
                if response.status_code == 200:
                    entries = response.json()
                else:
                    entries = []
            except Exception as ex:
                entries = []
            return entries

        def on_row_select(e):
            self.selected_entry = e.control.data  # Store selected entry
            page.update()

        def refresh_entries(e=None):
            entries = load_entries()
            if entries:
                entry_widgets = [
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Date", color=customTextcolor2)),
                            ft.DataColumn(ft.Text("Mood", color=customTextcolor2)),
                            ft.DataColumn(ft.Text("Entry", color=customTextcolor2)),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(entry.get('date', ''), color=customTextcolor2)),
                                    ft.DataCell(ft.Text(entry.get('mood', ''), color=customTextcolor2)),
                                    ft.DataCell(ft.Text(entry.get('entry', ''), color=customTextcolor2)),
                                ],
                                data=entry,
                                on_select_changed=on_row_select
                            )
                            for entry in entries
                        ],
                    )
                ]
            else:
                entry_widgets = [ft.Text("No entries found.", size=16, color="grey")]
            # Center all UI elements
            self.content.controls[0].content.controls = [
                ft.Text("Previous Entries", color=customTextcolor2, size=30, weight=ft.FontWeight.BOLD),
                *entry_widgets,
                ft.ElevatedButton("Refresh", on_click=refresh_entries),
                ft.ElevatedButton("Back to Startup", on_click=go_to_startup)
            ]
            page.update()

        # Initial load, center everything
        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,           # Center horizontally
            vertical_alignment=ft.CrossAxisAlignment.CENTER, # Center vertically
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,           # Center vertically in column
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER, # Center horizontally in column
                        controls=[]
                    )
                )
            ]
        )
        refresh_entries()

    def show_alert(self, title, content):
        self.alert_dialog.title = ft.Text(title)
        self.alert_dialog.content = ft.Text(content)
        self.alert_dialog.open = True
        self.page.dialog = self.alert_dialog
        self.page.update()
