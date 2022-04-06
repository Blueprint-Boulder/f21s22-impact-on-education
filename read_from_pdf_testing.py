#2 possible ways to get text below in the 2 methods
#Other possibly useful links:
    #https://blog.apilayer.com/build-your-own-resume-parser-using-python-and-nlp/
    #https://www.geeksforgeeks.org/pdf-redaction-using-python/



import PyPDF2
import spacy
from spacy.matcher import Matcher
from spacy.lang.en.examples import sentences

# Code from https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
def read_pdf(filename):
    # creating a pdf file object
    pdfFileObj = open(filename, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    print(pdfReader.numPages)

    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    print(pageObj.extractText())

    #to save the text and run NLP instead of print
    resume_text = pageObj.extractText()

    # closing the pdf file object
    pdfFileObj.close()

#code from - https://stackoverflow.com/questions/55220455/convert-from-pdf-to-text-lines-and-words-are-broken
def extract_with_pdf_miner():
    from io import StringIO
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfpage import PDFPage
    import os
    import sys, getopt

    # converts pdf, returns its text content as a string
    def convert(fname, pages=None):
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)

        output = io.StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        infile = open(fname, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close
        return text

        # converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir

    def convertMultiple(pdfDir, txtDir):
        if pdfDir == "": pdfDir = os.getcwd() + "\\"  # if no pdfDir passed in
        for pdf in os.listdir(pdfDir):  # iterate through pdfs in pdf directory
            fileExtension = pdf.split(".")[-1]
            if fileExtension == "pdf":
                pdfFilename = pdfDir + pdf
                text = convert(pdfFilename)  # get string of text content of pdf
                textFilename = txtDir + pdf + ".txt"
                textFile = open(textFilename, "w")  # make text file
                textFile.write(text)  # write text to text file

    # set paths accordingly:
    pdfDir = "C://your_path_here/"
    txtDir = "C://your_path_here/"
    convertMultiple(pdfDir, txtDir)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass


