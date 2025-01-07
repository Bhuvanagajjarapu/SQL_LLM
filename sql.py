import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
''')


cursor.execute('''INSERT INTO STUDENT VALUES ('Bhuvana', 'Full stack', 'A', 100)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Divya', 'Data Science', 'B', 99)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Ganesh', 'Devops', 'A', 60)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudha', 'Data science', 'B', 80)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Satyanarayana', 'Devops', 'A', 99)''')


print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)


connection.commit()
connection.close()
