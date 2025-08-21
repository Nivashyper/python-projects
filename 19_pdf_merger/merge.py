from pypdf import PdfWriter
import sys

def merge(out_path, *pdfs):
    writer = PdfWriter()
    for p in pdfs:
        writer.append(p)
    with open(out_path, "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    merge("merged.pdf", *sys.argv[1:])
