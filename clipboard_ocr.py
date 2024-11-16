# main.py
import tkinter as tk
import time
import threading
import pyperclip
from PIL import ImageGrab
from cross_platform_tesseract import CrossPlatformTesseract

class ClipboardWatcher:
    def __init__(self, cross_platform_tesseract):
        self.running = False
        self.previous_text = ""
        self.cross_platform_tesseract = cross_platform_tesseract

    def start(self):
        self.running = True
        self.cross_platform_tesseract.setup_tesseract()  # Ensure Tesseract is set up before use
        self.check_clipboard()

    def stop(self):
        self.running = False

    def check_clipboard(self):
        while self.running:
            current_text = pyperclip.paste()

            if current_text != self.previous_text:
                self.previous_text = current_text
                print(f"Text copied from clipboard: {current_text}")
            else:
                self.extract_text_from_image()

            time.sleep(1)  # Interval is a subject to change (1 second)

    def extract_text_from_image(self):
        try:
            image = ImageGrab.grabclipboard()
            if image is None:
                print("No image found in clipboard.")
                return
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            extracted_text = self.cross_platform_tesseract.extract_text(image)
            print("Extracted text:", extracted_text)
            
            if extracted_text.strip():
                pyperclip.copy(extracted_text.strip())
                print("Text copied to clipboard")
            else:
                print("Extracted text is empty!")
        
        except pytesseract.TesseractError as e:
            print(f"Tesseract error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Snipping Tool Image to Text")

        self.cross_platform_tesseract = CrossPlatformTesseract(platform='macos')
        self.watcher = ClipboardWatcher(self.cross_platform_tesseract)

        self.toggle_button = tk.Button(self.root, text="Start Monitoring", command=self.toggle_monitoring)
        self.toggle_button.pack(pady=30)

        self.status_label = tk.Label(self.root, text="Status: Stopped")
        self.status_label.pack(pady=10)

    def toggle_monitoring(self):
        if not self.watcher.running:
            self.watcher_thread = threading.Thread(target=self.watcher.start)
            self.watcher_thread.start()
            self.toggle_button.config(text="Stop Monitoring")
            self.status_label.config(text="Status: Running")
        else:
            self.watcher.stop()
            self.watcher_thread.join()
            self.toggle_button.config(text="Start Monitoring")
            self.status_label.config(text="Status: Stopped")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
