import flet as ft
import requests
from utils.colors import customBgColor, customTextcolor2

class resources(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.bgcolor = customBgColor

        def go_to_startup(e):
            page.go("/startup")

        def fetch_data():
            base_url = "https://ghoapi.azureedge.net/api/Indicator?$filter=contains(IndicatorName,%20%27Mental%20Health%27)"
            try:
                response = requests.get(base_url)
                data = response.json()
                items = data.get('value', [])
                for item in items:
                    item.pop('Language', None)
                return items
            except Exception as ex:
                return []

        def build_table(items):
            if not items:
                return ft.Text("No data found.", color="red")
            columns = [key for key in items[0].keys() if key != 'IndicatorCode']
            return ft.DataTable(
                columns=[ft.DataColumn(ft.Text(col, color=customTextcolor2)) for col in columns],
                rows=[
                    ft.DataRow(
                        cells=[ft.DataCell(ft.Text(str(item[col]), color=customTextcolor2)) for col in columns]
                    )
                    for item in items
                ],
                show_checkbox_column=False
            )

        items = fetch_data()
        data_table = build_table(items)

        # Wrap the table in a scrollable container
        scrollable_table = ft.Container(
            content=ft.Column(
                controls=[data_table],
                scroll=ft.ScrollMode.AUTO
            ),
            height=500,
            width=900,
            bgcolor=customBgColor,
            border_radius=10,
            padding=10
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
                            ft.Text("Online resources", color=customTextcolor2, size=30, weight=ft.FontWeight.BOLD),
                            scrollable_table,
                            ft.ElevatedButton("Back to Startup", on_click=go_to_startup)
                        ]
                    )
                )
            ]
        )
