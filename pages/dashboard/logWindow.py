import flet as ft
import requests
from datetime import datetime
from utils.validation import validation

class logWindow(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True

        validator = validation()

        mood_field = ft.TextField(label="Enter your mood here")
        log_field = ft.TextField(label="Journal Entry", multiline=True, min_lines=3, max_lines=10)
        validation_text = ft.Text("", color="red")

        def go_to_startup(e):
            page.go("/startup")

        def submit_entry(e):
            mood_valid = validator.is_valid_mood(mood_field.value)
            log_valid = validator.is_valid_log(log_field.value)
            if not mood_valid and not log_valid:
                validation_text.value = "Please enter your mood and journal entry."
            elif not mood_valid:
                validation_text.value = "Please enter your mood."
            elif not log_valid:
                validation_text.value = "Please enter your journal entry."
            else:
                # Get system date and time
                current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Send data to FastAPI backend
                data = {
                    "mood": mood_field.value,
                    "entry": log_field.value,
                    "date": current_date  # Send system date
                }
                try:
                    response = requests.post("http://localhost:8081/journals/", json=data)
                    if response.status_code == 200:
                        validation_text.value = "Entry submitted successfully!"
                        mood_field.value = ""
                        log_field.value = ""
                    else:
                        validation_text.value = f"Error: {response.text}"
                except Exception as ex:
                    validation_text.value = f"Failed to connect to the database"
            page.update()

        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("New Entry", color="black", size=30, weight=ft.FontWeight.BOLD),
                            mood_field,
                            log_field,
                            ft.ElevatedButton("Submit", on_click=submit_entry),
                            validation_text,
                            ft.ElevatedButton("Back to Startup", on_click=go_to_startup)
                        ]
                    )
                )
            ]
        )
