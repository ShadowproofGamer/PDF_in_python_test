import PyPDF2

def otworz_strone(pdf_path, numer_strony):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Sprawdź, czy podany numer strony jest w zakresie poprawnym
            if 0 < numer_strony <= len(pdf_reader.pages):
                # Pobierz obiekt strony PDF
                page = pdf_reader.pages[(numer_strony - 1)]

                # page.original_page;
                # Wydrukuj tekst z danej strony
                print(page.extract_text())

            else:
                print("Podano niepoprawny numer strony.")

    except FileNotFoundError:
        print(f"Plik {pdf_path} nie został znaleziony.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    # Przykładowe użycie
    sciezka_do_pdf = "data/Spr03HD-id266886-Cebula-2024.pdf"
    numer_docelowej_strony = 2

    otworz_strone(sciezka_do_pdf, numer_docelowej_strony)
