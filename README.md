# Click Tracker

A lightweight, background-running Windows application that logs your physical mouse clicks (Left, Right, and Middle) into a precise, timestamped CSV file. Built with Python and Tkinter, it features a simple graphical interface to toggle tracking and manage your log file destination.

## Getting Started

### Option 1: Running the Executable (Recommended for Windows)

If you have the compiled `.exe` version, no installation is required.

1. Download `click_counter.exe`.

    > It is recommended to save the exe in its own folder as the config file will be saved in the same folder that the exe is run from.

2. Double-click to run. *(Note: Windows Defender may initially flag it; click "More info" -> "Run anyway").*
3. On first launch, select a folder where you want your log data saved.

### Option 2: Running from Source

If you are running the raw Python script, ensure you have Python 3.x installed.

1. Clone or download the repository.
2. Install the required dependency:
   `pip install pynput`

   > Note: `tkinter`, `csv`, `os`, and `datetime` are included in the standard Python library.

3. Run the script:
    `python click_counter.py`

## How to Use

1. **Launch the App:** Upon opening, the app will ask you to select a save folder if it doesn't remember one from a previous session.
2. **Start Tracking:** Click the **Start Tracking** button. The status text will turn green. The app is now silently listening for mouse clicks in the background across all your applications.
3. **Change location:** Need to save the logs somewhere else? Click **Change Save Location** to pick a new folder. This will automatically update your `config.txt` file.
4. **Stop Tracking:** Click **Stop Tracking** (or simply close the application) to halt logging.

    > You can set it to launch on startup from task manager.

## Data Format

The application appends data to `click_log.csv` in the following format:

|Timestamp|Click_Type|
|---|---|
|2026-07-08 14:30:15.123456|Left|
|2026-07-08 14:30:17.654321|Right|
|2026-07-08 14:30:20.987654|Middle|
