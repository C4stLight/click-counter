import tkinter as tk
from pynput import mouse
from datetime import datetime
import csv
is_tracking = False
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = f"click_log_{timestamp}.csv"
with open(file_path, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Click_Type"])
def on_click(x, y, button, pressed):
    if is_tracking and pressed:
        click_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        click_type = "Unknown"
        if button == mouse.Button.left:
            click_type = "Left"
        elif button == mouse.Button.right:
            click_type = "Right"
        elif button == mouse.Button.middle:
            click_type = "Middle"
        with open(file_path, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([click_time, click_type])
def toggle_tracking():
    global is_tracking
    is_tracking = not is_tracking
    if is_tracking:
        status_label.config(text="Status: Tracking", fg="green")
        toggle_button.config(text="Stop Tracking")
    else:
        status_label.config(text="Status: Not Tracking", fg="red")
        toggle_button.config(text="Start Tracking")
listener = mouse.Listener(on_click=on_click)
listener.start()
root = tk.Tk()
root.title("Click Tracker")
root.geometry("250x150")
status_label = tk.Label(root, text="Status: Not Tracking", fg="red", font=("Helvetica", 12))
status_label.pack(pady=20)
toggle_button = tk.Button(root, text="Start Tracking", command=toggle_tracking, font=("Helvetica", 12))
toggle_button.pack(pady=10)
root.mainloop()