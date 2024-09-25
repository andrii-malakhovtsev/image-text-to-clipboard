import tkinter as tk
import time
import threading
import pyperclip
from PIL import ImageGrab
import pytesseract

# Configure the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class ClipboardWatcher:
    def __init__(self):
        self.running = False
        self.previous_text = ""

    def start(self):
        self.running = True
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

            time.sleep(1)  # Check every second, optimize to update from Win Snipping Tool only in the future

    def extract_text_from_image(self):
        try:
            image = ImageGrab.grabclipboard()
            if image is None:
                print("No image found in clipboard.")
                return
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            extracted_text = pytesseract.image_to_string(image)
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
        self.watcher = ClipboardWatcher()

        self.toggle_button = tk.Button(self.root, text="Start Monitoring"
                                       , command=self.toggle_monitoring)
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
            self.watcher_thread.join()  # Wait for the thread to finish
            self.toggle_button.config(text="Start Monitoring")
            self.status_label.config(text="Status: Stopped")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
