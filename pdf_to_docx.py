from pdf2docx import Converter

pdf_file = "xxx.pdf"
doc_file = "xxx.docx"

obj = Converter(pdf_file)
obj.convert(doc_file)
obj.close()
