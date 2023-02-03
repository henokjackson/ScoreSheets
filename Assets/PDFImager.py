import sys
import PIL
import PyPDF2
import pdf2image as PDF
import multiprocessing

path=sys.argv[1]
reader=PyPDF2.PdfFileReader(open(path,mode='rb'),strict=False)
pages=PDF.convert_from_path(path,thread_count=multiprocessing.cpu_count(),dpi=200,strict=False)
num=reader.getNumPages()-1
print(pages[num])
pages[num].save("out.jpg","JPEG")
