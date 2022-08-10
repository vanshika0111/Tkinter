import sqlite3
def createdb():
    con=sqlite3.connect(database=r"data.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS form(name text,v_no text,p_no text,t_f text,t_t text)")
    con.commit()
    
createdb()