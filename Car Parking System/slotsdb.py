import sqlite3
def createdb():
    con=sqlite3.connect(database=r"slots.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS slots(slts text)")
    con.commit()
    
createdb()