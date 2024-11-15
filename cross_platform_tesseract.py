import pytesseract
import os
from macos_os import MacOS
from windows_os import Windows

class CrossPlatformTesseract:
    def __init__(self, platform='windows'):
        self.platform = platform
        self.tesseract_path = self.set_tesseract_path()

    def set_tesseract_path(self):
        if self.platform == 'windows':
            return Windows.get_tesseract_path()
        elif self.platform == 'macos':
            return MacOS.get_tesseract_path()
        else:
            raise ValueError("Unsupported platform")

    def setup_tesseract(self):
        if not self.is_tesseract_installed(self.tesseract_path):
            raise Exception(f"Tesseract not installed or incorrect path: {self.tesseract_path}")
        
        pytesseract.pytesseract.tesseract_cmd = self.tesseract_path
        print(f"Tesseract set up at: {self.tesseract_path}")

    def is_tesseract_installed(self, tesseract_path):
        """Check if Tesseract is installed by verifying the version."""
        try:
            os.system(f'"{tesseract_path}" --version')
            return True
        except Exception:
            return False

    def extract_text(self, image):
        """Use pytesseract to extract text from an image."""
        return pytesseract.image_to_string(image)
