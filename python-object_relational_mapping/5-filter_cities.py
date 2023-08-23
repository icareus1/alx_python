"""
A script using the module MySQLdb that takes in the name of a state
as an argument and displays all the cities from the database hbtn_0e_4_usa
where name matches the argument and deal with injection
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    city_names = []
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
    query = "SELECT cities.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id \
        WHERE states.name LIKE BINARY %s ORDER BY cities.id"
    cur.execute(query, (name,))
    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    city_list = ", ".join(city_names)
    print(city_list)
    cur.close()
    con.close()
