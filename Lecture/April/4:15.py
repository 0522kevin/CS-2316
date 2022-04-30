import pymysql
import getpass

mypass = getpass.getpass("Enter your password")
connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, db = 'tv', charset = 'utf8mb4', cursorclass = pymysql.cursors.Cursor)

with connection.cursor() as cursor:
    with open('create_hogwarts.txt', 'r') as infile:
        while True:
            statement = infile.readline().strip()
            if len(statement) == 0:
                break
            cursor.execute(statement)
    statement = 'select * from students'
    cursor.execute(statement)
    results = cursor.fetchall()
    print(results)
    connection.commit()
    connection.close()
