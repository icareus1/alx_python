"""
A script using the module MySQLdb that takes in an argument
and displays all values in the states from the database
hbtn_0e_0_usa where name matches the argument 
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    name = argv[4]
    con = MySQLdb.connect(
                            host='localhost',
                            port=3306,
                            user=username,
                            passwd=password,
                            db=db_name
                        )
    cur = con.cursor()
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(name)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()
