import pymysql
from pprint import pprint
import getpass

def create_cursor(host_name, user_name, pw, db_name):
    try:
        connection = pymysql.connect(host = host_name, user = user_name, password = pw, db = db_name, \
                                    charset = "utf8mb4", cursorclass = pymysql.cursors.Cursor)
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        print(e)
        print(f"Couldn't log in to MySQL server using this password: {pw}.\n")



def query0(cursor, part_num):
    '''Sample'''
    query = 'SELECT name FROM parts WHERE part_num LIKE %s'
    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query, (part_num,))
    result = cursor.fetchall()
    return result

def query1(cursor):
    '''Fill in the query'''
    query = 'SELECT inventory_id, part_num FROM inventory_parts WHERE color_id = 20'
    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query2(cursor):
    '''Fill in the query'''
    query = 'SELECT name, num_parts FROM sets WHERE num_parts BETWEEN 5000 and 6000'
    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query3(cursor):
    '''Fill in the query'''
    query = 'SELECT name FROM themes WHERE parent_id = 5 ORDER BY id DESC LIMIT 5'
    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query4(cursor, color):
    '''Fill in the query'''
    query = 'SELECT row_id, part_num FROM inventory_parts WHERE color_id = %s AND quantity < 4 ORDER BY inventory_id DESC LIMIT 10'
    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query, (color,))
    result = cursor.fetchall()
    return result

def query5(cursor, year):
    '''Fill in the query'''
    query = 'SELECT year, COUNT(set_num) FROM sets where year >= %s GROUP BY year ORDER BY year'
    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query, (year,))
    result = cursor.fetchall()
    return result

def query6(cursor):
    '''Fill in the query'''
    query = 'SELECT inventory_id, SUM(quantity) FROM inventory_parts GROUP BY inventory_id ORDER BY SUM(quantity) DESC LIMIT 1'
    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query7(cursor):
    '''Fill in the query'''
    query = 'SELECT parent_id, COUNT(parent_id) FROM themes WHERE parent_id LIKE \'4%\' GROUP BY parent_id ORDER BY COUNT(parent_id);'
    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query8(cursor):
    '''Fill in the query'''
    query = 'SELECT inventory_id, COUNT(inventory_id) FROM inventory_sets GROUP BY inventory_id HAVING COUNT(inventory_id) > 5 ORDER BY COUNT(inventory_id) DESC'
    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query9(cursor):
    '''Fill in the query'''
    query = 'SELECT id, ROUND(AVG(num_parts)) AS mean_num_parts, themes.name FROM sets JOIN themes ON sets.theme_id = themes.id where sets.name NOT LIKE \'%Disney%\' GROUP BY id ORDER BY ROUND(AVG(num_parts)) DESC LIMIT 10'
    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query10(cursor):
    '''Fill in the query'''
    query = 'SELECT part_num, SUM(inventory_parts.quantity) FROM inventory_parts JOIN colors ON colors.id = inventory_parts.color_id WHERE rgb LIKE \'A%\' GROUP BY part_num HAVING SUM(inventory_parts.quantity) % 2 = 1 ORDER BY SUM(inventory_parts.quantity) DESC LIMIT 5'
    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def main():

    ######################## Insert MySQL Server password if applicable ########################

    user_password = getpass.getpass('\n# Enter your MySQL Server password: ')
    cursor = create_cursor('localhost', 'root', user_password, 'lego')

    ########################### Test Cases ###########################

    # query0() - cursor.fetchall() output
    print(">>> query0(cursor)")
    pprint(query0(cursor, 10))

    # query1() - cursor.fetchall() output
    print(">>> query1(cursor)")
    # pprint(query1(cursor))

    # query2() - cursor.fetchall() output
    print(">>> query2(cursor)")
    # pprint(query2(cursor))

    # Query 3 - cursor.fetchall() output
    print(">>> query3(cursor)")
    # pprint(query3(cursor))

    # query4() - cursor.fetchall() output
    print(">>> query4(cursor, 72)")
    # pprint(query4(cursor, 72))

    # query5() - cursor.fetchall() output
    print(">>> query5(cursor, 2000)")
    # pprint(query5(cursor, 2000))

    # query6() - cursor.fetchall() output
    print(">>> query6(cursor)")
    # pprint(query6(cursor))

    # query7() - cursor.fetchall() output
    print(">>> query7(cursor)")
    # pprint(query7(cursor))

    # query8() - cursor.fetchall() output
    print(">>> query8(cursor)")
    # pprint(query8(cursor))

    # query9() - cursor.fetchall() output
    print(">>> query9(cursor)")
    # pprint(query9(cursor))

    # query10() - cursor.fetchall() output
    print(">>> query10(cursor)")
    # pprint(query10(cursor))

if __name__ == '__main__':
    main()
