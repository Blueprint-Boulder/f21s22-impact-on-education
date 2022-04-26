import stanza
# stanza.download('en')
import re
import json
import pandas as pd
import sys
import io

nlp = stanza.Pipeline('en')  # initialize English neural pipeline
import PyPDF2


# ----------
# PDF stuff (will need later)
# ----------

#
# # Code from https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
# def read_pdf(filename):
#     # creating a pdf file object
#     pdfFileObj = open(filename, 'rb')
#
#     # creating a pdf reader object
#     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
#     # printing number of pages in pdf file
#     print(pdfReader.numPages)
#
#     # creating a page object
#     pageObj = pdfReader.getPage(0)
#
#     # extracting text from page
#     print(pageObj.extractText())
#
#     # to save the text and run NLP instead of print
#     resume_text = pageObj.extractText()
#
#     # closing the pdf file object
#     pdfFileObj.close()
#
#
# # code from - https://stackoverflow.com/questions/55220455/convert-from-pdf-to-text-lines-and-words-are-broken
# def extract_with_pdf_miner():
#     from io import StringIO
#     from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
#     from pdfminer.converter import TextConverter
#     from pdfminer.layout import LAParams
#     from pdfminer.pdfpage import PDFPage
#     import os
#     import sys, getopt
#
#     # converts pdf, returns its text content as a string
#     def convert(fname, pages=None):
#         if not pages:
#             pagenums = set()
#         else:
#             pagenums = set(pages)
#
#         output = io.StringIO()
#         manager = PDFResourceManager()
#         converter = TextConverter(manager, output, laparams=LAParams())
#         interpreter = PDFPageInterpreter(manager, converter)
#
#         infile = open(fname, 'rb')
#         for page in PDFPage.get_pages(infile, pagenums):
#             interpreter.process_page(page)
#         infile.close()
#         converter.close()
#         text = output.getvalue()
#         output.close
#         return text
#
#         # converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
#
#     def convertMultiple(pdfDir, txtDir):
#         if pdfDir == "": pdfDir = os.getcwd() + "\\"  # if no pdfDir passed in
#         for pdf in os.listdir(pdfDir):  # iterate through pdfs in pdf directory
#             fileExtension = pdf.split(".")[-1]
#             if fileExtension == "pdf":
#                 pdfFilename = pdfDir + pdf
#                 text = convert(pdfFilename)  # get string of text content of pdf
#                 textFilename = txtDir + pdf + ".txt"
#                 textFile = open(textFilename, "w")  # make text file
#                 textFile.write(text)  # write text to text file
#
#     # set paths accordingly:
#     pdfDir = "./"
#     txtDir = "./"
#     convertMultiple(pdfDir, txtDir)
#

# ----------
# End PDF stuff
# ----------

def core_nlp(input_paragraph, looking_for=None):
    # First, handle pronoun replacement
    replacements = {'he': ' [THEY]',
                    'him': ' [THEM]',
                    'his': ' [THEIR]',
                    'she': ' [THEY]',
                    'her': ' [THEM]',
                    'hers': ' [THEIR]',
                    'man': '[PERSON]',
                    'woman': '[PERSON]',
                    'men': '[PEOPLE]',
                    'women': '[PEOPLE]'
                    }

    def replace_pronouns(match):
        return replacements[match.group(0)]

    regex = '|'.join(r'\b%s\b' % re.escape(s) for s in replacements)
    input_paragraph = re.sub(regex, replace_pronouns, input_paragraph)

    # Redact Emails (disabled for now)
    # regex_email = '[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+'
    # lst_emails = re.findall(regex_email, input_paragraph)
    # for email in lst_emails:
    #     input_paragraph = input_paragraph.replace(email, "[EMAIL]")

    # Redact Phone numbers
    regex_phone = '\d{3}[-\.\s]+\d{3}[-\.\s]+\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]+\d{4}'
    lst_phones = re.findall(regex_phone, input_paragraph)
    for phone in lst_phones:
        input_paragraph = input_paragraph.replace(phone, "[PHONE]")

    # Redact Dates
    # regex_date = "((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2},\s+\d{4})"
    # regex_date = '[\d]{1,2}[/-][\d]{1,2}[/-][\d]{4}'
    regex_date = "([\d]{1,2}[/-][\d]{1,2}[/-][\d]{4})|((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2},\s+\d{4})|((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s?[\d{1,2}]?[,]?\s+\d{4})|(\d{4}[-]+\d{4})"
    lst_dates = re.findall(regex_date, input_paragraph)
    for date in lst_dates:
        date = max(date, key=len)
        input_paragraph = input_paragraph.replace(date, "[DATE]")

    # Redact Address/Location, Company/Organization, and Names using stanza
    try:
        doc = nlp(input_paragraph)
        lst_entities = {
            'FAC': '[ADDRESS]',
            'GPE': '[LOCATION]',
            'PERSON': '[PERSON]',
            'ORG': '[ORGANIZATION]',
            'LOC': '[LOCATION]'
        }
        for sentence in doc.sentences:
            for i in sentence.ents:
                if i.type in lst_entities and i.text not in ['PERSON', 'EMAIL']:
                    input_paragraph = input_paragraph.replace(i.text, lst_entities[i.type])
    except:
        print("corenlp didn't work...")

    return input_paragraph


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    directory = "./sample_cover_letter.pdf.txt"
    extract_with_pdf_miner()
    f = open(directory)
    text = f.read()
    input_paragraph = ""
    redacted = core_nlp(input_paragraph)
