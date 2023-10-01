from PyPDF2 import PdfReader,PdfWriter
archivor="estudio"
reader=PdfReader(archivor+".pdf")
writer= PdfWriter()
for page in reader.pages:
    writer.add_page (page)
writer.encrypt("pollofrito")
with open(archivor+"1.pdf", "wb") as f:
    writer.write(f)

