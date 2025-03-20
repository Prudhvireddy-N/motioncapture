# File Monitoring and Backup Script

This Python script monitors a specified directory for new image files (such as `.jpg` and `.png`) and automatically moves any newly created files to a backup directory. It uses the `watchdog` library to observe file system events.

## Features

- Monitors a specified directory (`/home/pi/Desktop/motion`) for new image files.
- Supports `.jpg` and `.png` file types.
- Moves new files to a backup directory (`/home/pi/Desktop/motion/backup`).
- Can be customized to perform additional actions (such as API calls) when a file is created.

## Requirements

1. **Python 3.x**: Make sure you have Python installed on your system.
2. **watchdog**: This script uses the `watchdog` library for directory monitoring.

   You can install it using pip:

   ```bash
   pip install watchdog
   ```
3. **shutil**: This is part of Python's standard library, so no installation is required.

## Setup and Usage
1. Clone or download the script to your Raspberry Pi or any other Linux-based system.

2. Ensure the following directories exist:

      - /home/pi/Desktop/motion: The directory to be monitored for new files.
      - /home/pi/Desktop/motion/backup: The directory where files will be moved to as backup.
  
If these directories don't exist, create them using:

```bash
mkdir -p /home/pi/Desktop/motion
mkdir -p /home/pi/Desktop/motion/backup
```

1. Run the script:

```bash
python3 file_watcher.py
The script will now begin monitoring the specified directory for new image files.
```

## Customization
You can customize the following in the script:

- Monitored Directory: Change the DIRECTORY_TO_WATCH variable to the directory you wish to monitor.
- Backup Directory: Change the BACKUP_DIRECTORY variable to your desired backup location.
- File Types: Modify the patterns list in the Handler class to monitor additional file types (e.g., .txt, .mp4).
