import fitz  # PyMuPDF
import tkinter as tk
from tkinter import ttk

class PDFViewerApp:
    def __init__(self, master, pdf_path):
        self.master = master
        self.master.title("PDF Viewer")
        self.master.geometry("800x600")

        self.pdf_path = pdf_path

        self.canvas = tk.Canvas(self.master)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.render_pdf()

    def render_pdf(self):
        doc = fitz.open(self.pdf_path)

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap().pil_save()
            img = tk.PhotoImage(data=pix.image_data, master=self.master)
            label = ttk.Label(self.canvas, image=img)
            label.image = img
            label.pack()

        doc.close()

def main():
    pdf_path = "data/pdf.pdf"

    root = tk.Tk()
    app = PDFViewerApp(root, pdf_path)
    root.mainloop()

if __name__ == "__main__":
    main()
