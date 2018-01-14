# pdf_crawler
This is a readme document for PDF crawler API

** API endpoint that are used:
 * /crawl/api/uploader (POST) receives the PDF document to crawl
 * /crawl/web_upload web for for testing the uploader
 * /crawl/api/docs (GET) - returns all the uploaded documents (ids and names) up to that point
 * /crawl/api/docs/<doc_id>/urls (GET) - returns all the URL's of a specified document (by ID)
 * /crawl/api/urls (GET) - returns all the urls in the system


** Assumptions:
 * The uploaded document is legal PDF document
 * database 'docs.db' has been created (can be done by going to base url '/')
 * i am using PyPDF2 library to deal with PDF files
 * i am checking URL validity with 'requests' library
