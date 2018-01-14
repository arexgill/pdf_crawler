import sqlite3
import json

DBNAME = 'docs.db'


def create_db():
    conn = sqlite3.connect(DBNAME)
    print "Opened database successfully"
    conn.execute('CREATE TABLE IF NOT EXISTS documents (doc_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)')
    conn.execute('CREATE TABLE IF NOT EXISTS urls (name TEXT, url TEXT, alive INTEGER)')
    print "Tables created successfully"
    conn.close()


def insert_doc(doc_name):
    try:
        with sqlite3.connect(DBNAME) as con:
            cur = con.cursor()
            cur.execute("REPLACE INTO documents (name) VALUES(?)", (doc_name,))
            con.commit()
    except:
        con.rollback()
    finally:
        con.close()


def insert_url(doc_name, url, is_alive):
    try:
        with sqlite3.connect(DBNAME) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO urls (name, url, alive) VALUES(?, ?, ?)", (doc_name, url, is_alive))
            con.commit()
    except:
        con.rollback()
    finally:
        con.close()


def select_docs():
    con = sqlite3.connect(DBNAME)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT COUNT(url) as 'urls', U.name, D.doc_id FROM 'urls' "
                "as U, 'documents' as D GROUP BY U.name")
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    return json.dumps(r)


def select_urls_for_doc(doc_id):
    con = sqlite3.connect(DBNAME)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT url, documents.doc_id, documents.name FROM 'urls', 'documents' "
                "WHERE doc_id = ? AND documents.name = urls.name GROUP BY url", (doc_id,))
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    return json.dumps(r)


def select_urls():
    con = sqlite3.connect(DBNAME)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT COUNT(name) as 'number of files', url, alive FROM 'urls' GROUP BY url")
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    return json.dumps(r)
