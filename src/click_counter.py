from pynput import mouse
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = f"click_log_{timestamp}.txt"
clicks = {
    "left": 0,
    "right": 0,
    "middle": 0
}
total_clicks = 0
def on_click(x, y, button, pressed):
    global total_clicks
    if pressed:
        total_clicks += 1
        if button == mouse.Button.left:
            clicks["left"] += 1
        elif button == mouse.Button.right:
            clicks["right"] += 1
        elif button == mouse.Button.middle:
            clicks["middle"] += 1
        log_content = (
            f"Left Clicks: {clicks['left']}\n"
            f"Right Clicks: {clicks['right']}\n"
            f"Middle Clicks: {clicks['middle']}\n"
            f"-------------------\n"
            f"Total Clicks: {total_clicks}\n"
        )
        with open(file_path, "w") as f:
            f.write(log_content)
listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()