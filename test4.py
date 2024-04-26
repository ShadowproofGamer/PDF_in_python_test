from tkinter import Tk, filedialog, Label, PhotoImage, Button
from pdf2image import convert_from_path

def show_pdf_page():
    # Open file dialog to select PDF
    pdf_path = filedialog.askopenfilename(title="Select PDF", filetypes=[("PDF Files", "*.pdf")])
    if not pdf_path:
        return

    # Extract first page (index 0) as image
    pages = convert_from_path(pdf_path, dpi=200, first_page=1, last_page=1)
    img = pages[0]

    # Convert image to format compatible with Tkinter
    img = PhotoImage(image=img)

    # Create a window to display the image
    window = Tk()
    window.title("PDF Page Preview")

    # Create a label to hold the image
    label = Label(window, image=img)
    label.pack()

    window.mainloop()

# Create a button to trigger the function
button = Tk()
button.title("Select PDF")
button = Button(button, text="Show PDF Page", command=show_pdf_page)
button.pack()
button.mainloop()
