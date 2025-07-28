import requests
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
import os

def plot_logs_per_month(api_url="http://localhost:8081/journals/"):
    img_path = "statPics/logs_per_month.png"
    # Check if the image already exists
    if os.path.exists(img_path):
        return

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            entries = response.json()
        else:
            print(f"Error: {response.text}")
            return
    except Exception as ex:
        print(f"Failed to connect to the server: {ex}")
        return

    # Extract year-month from each entry's date
    months = []
    for entry in entries:
        date_str = entry.get("date", "")
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            months.append(dt.strftime("%Y-%m"))
        except Exception:
            continue

    # Count logs per month
    month_counts = Counter(months)
    sorted_months = sorted(month_counts.keys())
    counts = [month_counts[month] for month in sorted_months]

    # Plot using matplotlib
    plt.figure(figsize=(8, 4))
    plt.bar(sorted_months, counts, color="skyblue")
    plt.xlabel("Month")
    plt.ylabel("Number of Logs")
    plt.title("Journal Logs per Month")
    plt.xticks(rotation=45)
    plt.tight_layout()
    os.makedirs(os.path.dirname(img_path), exist_ok=True)  # <-- Add this line
    plt.savefig(img_path)
    plt.close()
