from abc import ABC, abstractmethod
import pytesseract
import os

class OSPlatform(ABC):
    @abstractmethod
    def get_tesseract_path(self):
        """Abstract method to get the path of Tesseract."""
        pass

    def setup_tesseract(self):
        """Set up pytesseract with the correct executable path."""
        tesseract_path = self.get_tesseract_path()
        if not self.is_tesseract_installed(tesseract_path):
            raise Exception("Tesseract is not installed or the path is incorrect.")
        
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        print(f"Using Tesseract at: {tesseract_path}")

    def is_tesseract_installed(self, tesseract_path):
        """Check if Tesseract is installed by verifying the version."""
        try:
            os.system(f'"{tesseract_path}" --version')
            return True
        except Exception:
            return False
