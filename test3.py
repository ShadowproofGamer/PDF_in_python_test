import fitz
import argparse
from tkinter import Tk, Canvas, Frame, Scrollbar

def open_pdf(filename, url):
    # Wczytaj plik PDF
    with open(filename, 'rb') as f:
        reader = fitz.open(f)
        page = reader.load_page(0)

    # Utwórz okno GUI
    root = Tk()
    root.title('Podgląd PDF')

    # Utwórz kanwę do wyświetlania strony PDF
    canvas = Canvas(root)
    canvas.pack(fill='both', expand=True)

    # Wyświetl pierwszą stronę PDF na kanwie
    xscale = canvas.winfo_width() / page.mediabox.width
    yscale = canvas.winfo_height() / page.mediabox.height
    canvas.create_image(page, transform=(xscale, yscale), page=1)


    # Otwórz podaną stronę w przeglądarce
    import webbrowser
    webbrowser.open_new_tab(url)

    # Uruchom GUI
    root.mainloop()

# Pobierz argumenty z wiersza poleceń
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='Ścieżka do pliku PDF')
parser.add_argument('--url', help='URL do otwarcia w przeglądarce')
args = parser.parse_args()

# Wywołaj funkcję otwierania pliku PDF
open_pdf(args.filename, args.url)
