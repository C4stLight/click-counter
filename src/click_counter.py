import tkinter as tk
from tkinter import filedialog
import os
from pynput import mouse
from datetime import datetime
import csv

is_tracking = False
file_path = ""
config_file = "config.txt"

def load_config():
    global file_path
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            saved_path = f.read().strip()
            if saved_path and os.path.exists(os.path.dirname(saved_path)):
                file_path = saved_path
                return True
    return False

def save_config(path):
    with open(config_file, "w") as f:
        f.write(path)

def select_directory():
    global file_path
    folder_selected = filedialog.askdirectory(title="Select Save Folder")
    if folder_selected:
        file_path = os.path.join(folder_selected, "click_log.csv")
        save_config(file_path)
    elif not file_path:
        file_path = "click_log.csv"
        save_config(file_path)
    
    dir_label.config(text=f"Saving to: {file_path}")
    if not os.path.exists(file_path):
        with open(file_path, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Click_Type"])

def on_click(x, y, button, pressed):
    if is_tracking and pressed and file_path:
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

def initialize_app():
    if load_config():
        dir_label.config(text=f"Saving to: {file_path}")
    else:
        select_directory()

root = tk.Tk()
root.title("Click Tracker")
root.geometry("350x250")

status_label = tk.Label(root, text="Status: Not Tracking", fg="red", font=("Helvetica", 12))
status_label.pack(pady=10)

toggle_button = tk.Button(root, text="Start Tracking", command=toggle_tracking, font=("Helvetica", 12))
toggle_button.pack(pady=5)

dir_button = tk.Button(root, text="Change Save Location", command=select_directory, font=("Helvetica", 10))
dir_button.pack(pady=5)

dir_label = tk.Label(root, text="Saving to: Not Selected", font=("Helvetica", 8), wraplength=300)
dir_label.pack(pady=10)

listener = mouse.Listener(on_click=on_click)
listener.start()

root.after(100, initialize_app)
root.mainloop()