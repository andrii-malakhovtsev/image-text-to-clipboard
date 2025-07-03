# Image Text To Clipboard

## Dependencies

- This project uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract), an open-source Optical Character Recognition engine, licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## About

Usage of a clipboard (for example Win + Shift + S in Windows OS for snipping tool) to convert text from the screenshot to the symbolic text back to the clipboard overriding the screenshot.

## Tesseract Installation Instructions

To use the OCR functionality in this application, you need to have Tesseract OCR installed on your system. 

Below are the instructions to install Tesseract on both **Windows** and **macOS** platforms.

### Windows

1. **Download Tesseract Installer**:
   - Visit the official Tesseract GitHub releases page:  
     [Tesseract at GitHub](https://github.com/tesseract-ocr/tesseract/releases)
   - Download the latest **Windows installer** (`.exe`).

2. **Run the Installer**:
   - Launch the installer and follow the installation steps.
   - During installation, make sure the option to add Tesseract to your system's **PATH** is selected (this will make it accessible from everywhere in the command line).

3. **Verify Installation**:
   - After installation, open **Command Prompt** and type the following to check if Tesseract is installed correctly:

     ```bash
     tesseract --version
     ```

   - If Tesseract is installed correctly, you will see the version number displayed.

### MacOS

1. **Install Homebrew** (if you don't have it installed):
   - Open **Terminal** and run the following command to install Homebrew:

     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

  - OR [Homebrew package at GitHub](https://github.com/Homebrew/brew/releases)

2. **Install Tesseract Using Homebrew**:
   - Once Homebrew is installed, run the following command in the **Terminal**:

     ```bash
     brew install tesseract
     ```

3. **Verify Installation**:
   - After the installation completes, verify the installation by typing the following command in **Terminal**:

     ```bash
     tesseract --version
     ```

   - If installed correctly, you should see the Tesseract version information.

4. **Optional**: Install Additional Languages:
   - If you need language support for OCR, you can install additional language packs using the following command:

     ```bash
     brew install tesseract-lang
     ```

5. **Path to Tesseract**:
   - By default, Tesseract is installed in `/usr/local/bin/tesseract`. You can verify the path by typing:

     ```bash
     which tesseract
     ```

---

### Using Tesseract in Your Application

Tesseract PATHs for this applications are set to default and are NOT detected by default.


## Installation

Go to <a href="https://github.com/andrii-malakhovtsev/clipboard-image-to-text/releases">Releases</a>, choose the latest release and choose the corresponding file for your OS.
