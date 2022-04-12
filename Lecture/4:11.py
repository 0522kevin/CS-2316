import pymysql

# What is the difference between DictCursor and Cursor?
# Cursor converts database to tuple of tuples
# DictCursor converts database to list of dictionaries
connection = pymysql.connect(host = 'localhost', user = 'root', password = 'kevin522', db = 'tv', charset = 'utf8mb4', cursorclass = pymysql.cursors.Cursor)

with connection.cursor() as cursor:
    statement = 'show databases;'
    cursor.execute(statement)
    results = cursor.fetchall()
    print(results)
    print(type(results))

    statement = 'select count(*) from shows left join actors on show_id = acts_on where fname like "j%" group by shows.show_id;'
    cursor.execute(statement)
    results = cursor.fetchall()
    print(results)

    connection.commit()
    connection.close()
