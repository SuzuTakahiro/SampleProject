import sqlite3
import os

def makeTable(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS FRUIT (id integer primary key, name text,num integer,value integer)")
    cursor.execute("CREATE TABLE IF NOT EXISTS RSTC_MEAN (Initial text primary key, Mean text,Mean_J text)")
def insertData(cursor):
    cursor.execute("insert into FRUIT values(1,'orange',3,120)")
    cursor.execute("insert into FRUIT values(2,'Apple',2,180)")
    cursor.execute("insert into FRUIT values(3,'banana',2,100)")

    cursor.execute("insert into RSTC_MEAN values('R','Ritsuan','リツアン')")
    cursor.execute("insert into RSTC_MEAN values('S','Suprise','驚き')")
    cursor.execute("insert into RSTC_MEAN values('T','TeamWork','チームワーク')")
    cursor.execute("insert into RSTC_MEAN values('C','Company','会社')")

def readData(cursor):
    cursor.execute("select * from FRUIT")
    data = cursor.fetchone()
    print(data)
    print(data.keys())

def readTableNames(cursor):
    cursor.execute("select name from sqlite_master where type='table'")
    for data in cursor.fetchall():
        print(data)

def readTableInfo(cursor,table = "FRUIT"):
    cursor.execute("PRAGMA TABLE_INFO(FRUIT)")  ### テーブルmpos_Sのカラム情報を取得
    cols = cursor.fetchall()  ### 1つのカラム情報は6要素を含むタプルで，複数のカラム情報のリストが得られる
    print([item[1] for item in cols])

if __name__ == '__main__':
    db_name = "sample.db"
    workdir = os.path.dirname(__file__)
    db_path = os.path.join(workdir,db_name)
    print(db_path)
    connection = sqlite3.connect(db_path)
    # connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    try:
        makeTable(cursor)
        insertData(cursor)
        # readData(cursor)
        readTableNames(cursor)
        readTableInfo(cursor)
    except sqlite3.Error as e:
        print('sqlite3 Error occurred:', e.args[0])
    connection.commit()
    connection.close()
