# import PyPDF2
#    # open file
# files=["1.pdf","2.pdf"]
#    # create a pdf file merger object
# merger = PyPDF2.PdfMerger()
#    # add files to merger
# for file in files:
#     pdffile=open(file,'rb')
    
#     merger.append(PyPDF2.PdfReader(pdffile))
    
# pdffile.close()
# merger.write('merged.pdf')    
    
    
import PyPDF2

# Open the PDF files to merge
pdf_files = ['1.pdf', '2.pdf', ...]

# Create a PdfFileMerger object
merger = PyPDF2.PdfMerger()

# Add each PDF file to the merger
for file in pdf_files:
    merger.append(PyPDF2.PdfReader(file))

# Write the merged PDF to a new file
with open('output.pdf', 'wb') as f:
    merger.write(f)    

    
