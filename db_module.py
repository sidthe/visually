import sqlite3

dbname = 'visually.db'

def dbTableCreator():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''CREATE TABLE trello (shortUrl, dateLastActivity, name, id)''')
    conn.commit()



if __name__ == '__main__':
    pass
