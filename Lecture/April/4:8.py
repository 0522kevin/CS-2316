import pymysql
import getpass

mypass = getpass.getpass("Enter your password")
connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    statement = "show databases"
    cursor.execute(statement)
    print(cursor.fetchall())
