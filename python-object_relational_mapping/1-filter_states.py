"""
A script using the module MySQLdb to list all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    con = MySQLdb.connect(
                            host='localhost',
                            port=3306,
                            user=username,
                            passwd=password,
                            db=db_name
                        )
    cur = con.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()
