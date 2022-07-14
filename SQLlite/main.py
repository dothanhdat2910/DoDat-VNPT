import sqlite3

conn = sqlite3.connect("member.db")
cursor = conn.cursor()

table = """CREATE TABLE STUDENT (NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255));"""
cursor.execute(table)

cursor.execute('''INSERT INTO STUDENT VALUES ('Đạt', 'IT3', 'A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Lâm', 'IT3', 'B')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Minh', 'IT3', 'C')''')
data = cursor.execute('''SELECT *FROM STUDENT''')
for row in data:
    print(row)

conn.commit()
conn.close()