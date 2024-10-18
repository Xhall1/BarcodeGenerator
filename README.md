# Barcode Generator

## Description
The Barcode Generator is a simple Python application that allows users to create PDF documents containing a specified number of barcodes. Currently, the application supports generating Code 128 barcodes, which are commonly used in various industries for inventory and tracking purposes. The user-friendly graphical interface simplifies the process of entering the desired number of barcodes, making it accessible for anyone to use.

## Features
- Generate a specified number of barcodes.
- Save the generated barcodes in a PDF file on the user's desktop.
- Easy-to-use graphical user interface (GUI) built with Tkinter.
- Customizable barcode dimensions and layout.

## Requirements
- Python 3.x
- ReportLab library
- Tkinter library (included with Python)

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Xhall1/Barcode-Generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Barcode-Generator
   ```
3. Install the required libraries:
   ```bash
   pip install reportlab
   ```

## Usage
1. Run the application:
   ```bash
   python QrCode.py
   ```
2. Enter the number of barcodes you want to generate in the input field.
3. Click the "Generate Barcodes" button.
4. The generated PDF file will be saved on your desktop with the name `Barcodes.pdf`.

## Author
Script made by San (Xhall1)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
