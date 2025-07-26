import flet as ft
import requests

class history(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
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
            delete_button.disabled = False  # Enable delete button
            page.update()

        def on_delete_click(e):
            if self.selected_entry and "id" in self.selected_entry:
                entry_id = self.selected_entry["id"]
                try:
                    response = requests.delete(f"http://localhost:8081/journals/{entry_id}")
                    if response.status_code == 200:
                        self.show_alert("Deleted", "Entry deleted successfully.")
                    else:
                        self.show_alert("Error", f"Failed to delete entry: {response.text}")
                except Exception as ex:
                    self.show_alert("Error", "Could not connect to backend.")
                self.selected_entry = None
                delete_button.disabled = True
                refresh_entries()
            else:
                self.show_alert("Error", "No entry selected.")

        def refresh_entries(e=None):
            entries = load_entries()
            if entries:
                entry_widgets = [
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Date")),
                            ft.DataColumn(ft.Text("Mood")),
                            ft.DataColumn(ft.Text("Entry")),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(entry.get('date', ''))),
                                    ft.DataCell(ft.Text(entry.get('mood', ''))),
                                    ft.DataCell(ft.Text(entry.get('entry', ''))),
                                ],
                                data=entry,
                                on_select_changed=on_row_select
                            )
                            for entry in entries
                        ],
                        show_checkbox_column=True
                    )
                ]
            else:
                entry_widgets = [ft.Text("No entries found.", size=16, color="grey")]
            self.content.controls[0].content.controls = [
                ft.Text("Previous Entries", color="black", size=30, weight=ft.FontWeight.BOLD),
                *entry_widgets,
                delete_button,
                ft.ElevatedButton("Refresh", on_click=refresh_entries),
                ft.ElevatedButton("Back to Startup", on_click=go_to_startup)
            ]
            page.update()

        # Delete button (initially disabled)
        delete_button = ft.ElevatedButton("Delete Selected", on_click=on_delete_click, disabled=True)

        # Initial load
        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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


