from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename

from db_mapper import create_db, select_docs, select_urls, select_urls_for_doc
from parse_pdf import parse_file


app = Flask(__name__)

@app.route("/")
def hello():
    create_db()
    return "This is and entry point for crawler API!"


@app.route('/crawl/web_upload')
def upload_file():
   return render_template('upload.html')


@app.route('/crawl/api/uploader', methods=['POST'])
def upload_doc():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        parse_file(f.filename)
        return 'file uploaded successfully'


@app.route('/crawl/api/docs', methods=['GET'])
def get_docs():
    return jsonify({'documents': select_docs()})


@app.route('/crawl/api/docs/<int:doc_id>/urls', methods=['GET'])
def get_doc_urls(doc_id):
    return jsonify({'urls_for_doc': select_urls_for_doc(doc_id)})


@app.route('/crawl/api/urls', methods=['GET'])
def get_urls():
    return jsonify({'urls': select_urls()})


if __name__ == '__main__':
    app.run(debug=True)