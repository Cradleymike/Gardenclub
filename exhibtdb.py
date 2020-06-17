import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS exhibitors (num INTEGER PRIMARY KEY, fname text, lname text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM exhibitors")
        rows = self.cur.fetchall()
        return rows

    def insert(self,fname,lname):
        self.cur.execute("INSERT INTO exhibitors VALUES (NULL,?,?)",(fname,lname))
        self.conn.commit()

    def remove(self,num):
        self.cur.execute("DELETE FROM exhibitors WHERE num=?",(num,))
        self.conn.commit()

    def update(self, num, fname, lname):
        self.cur.execute("UPDATE exhibitors SET fname = ?, lname = ? WHERE id = ?",(fname,lname,num))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


#db = Database('exhibitor.db')
#db.insert("Mike", "Hollis")
#db.insert("Jean", "Hollis")