import sqlite3 as sql
import pandas as pd
import databases

with sql.connect("database\\data.sqlite") as con:
    cur = con.cursor()
    
    cur.execute("INSERT INTO Category (CategoryID, CategoryDesc) VALUES (?,?)",('03', 'Kupon') )
    
    con.commit()
    msg = "Record successfully added"
# DATABASE_URL = "sqlite:///database/data.sqlite?check_same_thread=False"
# database = databases.Database(DATABASE_URL)

# uvicorn app.main:app --reload