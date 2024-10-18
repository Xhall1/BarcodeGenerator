from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from reportlab.lib.units import mm
import os
import tkinter as tk
from tkinter import messagebox


def create_barcode_pdf(quantity, filename):
    pdf = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    columns = 4
    rows = 12

    barcode_width = 50 * mm
    barcode_height = 15 * mm

    margin_x = 1 * mm
    margin_y = 8 * mm

    x_start = margin_x
    y_start = height - margin_y - barcode_height

    for i in range(1, quantity + 1):
        number = f'{i:05}'

        barcode = code128.Code128(number, barHeight=barcode_height, barWidth=1.4)

        x_pos = x_start + ((i - 1) % columns) * (barcode_width + margin_x)
        y_pos = y_start - ((i - 1) // columns % rows) * (barcode_height + margin_y)

        barcode.drawOn(pdf, x_pos, y_pos)

        pdf.drawString(x_pos + (barcode_width - pdf.stringWidth(number)) / 2, y_pos - 10, number)

        if i % (columns * rows) == 0:
            pdf.showPage()
            x_pos = x_start
            y_pos = y_start

    pdf.save()
    messagebox.showinfo("Success", f"\nScript made by San (Xhall1) :)\n\nPDF document created: {filename}")


def generate_barcodes():
    try:
        quantity = int(entry.get())
        if quantity <= 0:
            raise ValueError("Please enter a positive integer.")

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        output_file = os.path.join(desktop_path, "Barcodes.pdf")

        create_barcode_pdf(quantity, output_file)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


# GUI
root = tk.Tk()
root.title("Barcode Generator")

label = tk.Label(root, text="Enter the number of barcodes you want to generate:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Barcodes", command=generate_barcodes)
generate_button.pack(pady=20)

root.mainloop()
