import mysql.connector

conn = mysql.connector.connect(
   user='root', password='password', host='127.0.0.1', database='mydb'
)
cursor = conn.cursor()


def createTable():
    cursor.execute("DROP TABLE IF EXISTS ITEMS")
    sql = '''CREATE TABLE ITEMS(
       CODE INT NOT NULL PRIMARY KEY ,
       INAME VARCHAR(50),
       QTY INT,
       PRICE INT,
       COMPANY VARCHAR(50),
       TCODE VARCHAR(10)
    )'''
    cursor.execute(sql)


def addRecords():
    sql = '''INSERT INTO ITEMS(CODE, INAME, QTY, PRICE, COMPANY, TCODE)
    VALUE (1001, 'DIGITAL PAD 12i', 120, 11000, 'XENITA', 'T01'),
    (1006, 'LED SCREEN 40', 70, 38000, 'SANTORA', 'T02'),
    (1004, 'CAR GPS SYSTEM', 50, 21500, 'GEOKNOW', 'T01'),
    (1003, 'DIGITAL CAMERA 12X', 160, 8000, 'DIGICLICK', 'T02'),
    (1005, 'PEN DRIVE 32GB', 600, 1200, 'STOREHOME', 'T03');
    '''
    cursor.execute(sql)


def updateRecord(code:int, qtyy: int):
    sql = '''UPDATE ITEMS SET QTY={}
    WHERE CODE= {};
    '''.format(qtyy, code)
    cursor.execute(sql)

def deleteRecord(code:int):
    sql = '''DELETE FROM ITEMS WHERE CODE= {}'''.format(code)
    cursor.execute(sql)


def displayRecord():
    sql = "SELECT * FROM ITEMS"
    cursor.execute(sql)
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)
    print("\nPrinting each row")
    for row in records:
        print("CODE= ", row[0], )
        print("INAME = ", row[1])
        print("QTY  = ", row[2])
        print("PRICE  = ", row[3])
        print("COMPANY  = ", row[4])
        print("TCODE = ", row[5], '\n')
        conn.close()

