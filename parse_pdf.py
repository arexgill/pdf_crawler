import PyPDF2
import re
import requests

from db_mapper import insert_doc, insert_url


def parse_file(filename):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    insert_doc(filename)
    for page_num in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page_num)
        store_urls(filename, pageObj.extractText())


def store_urls(filename, page):
    print page
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', page)
    for url in urls:
        try:
            request = requests.get(url)
            if request.status_code == 200:
                is_alive = 1
            else:
                is_alive = 0
        except:
            is_alive = 0
        insert_url(filename, url, is_alive)

