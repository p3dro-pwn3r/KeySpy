# KeySpy - Python Keylogger

KeySpy is a very very simple proof of concept python keylogger that captures keystrokes and sends them to a specified Discord webhook.

## Features

- Logs pressed keys and special key events
- Sends logs to a Discord webhook
- Hidden operation (console window is not visible)
- Startup persistence (adds the keylogger to the startup registry)

## Requirements

- Python
- pynput library (`pip install pynput`)
- dhooks library (`pip install dhooks`)

## Usage

1. Install the required Python packages:
   pip install -r requirements.txt
2. Run the program:
   python keylogger.py

## Configuration
1. Logs File: Set the logs_file variable to the desired path for the logs file.
2. Discord Webhook: Set the webhook_url variable to your Discord webhook URL.

## Disclaimer
This keylogger is intended for educational purposes only. Usage of keyloggers without proper authorization may violate privacy laws.
   
