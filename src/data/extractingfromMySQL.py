import pymysql


connectionString = {
    'host': '34.66.111.105',
    'username': 'root',
    'password': 'Iamawesome247',
    'db': 'test_titanic'
}

conn = pymysql.connect(connectionString['host'], connectionString['username'], connectionString['password']
                       , connectionString['db'])

cursor = conn.cursor()

# connection = pymysql.connect("classRoomDB.db")

# cursor = connection.cursor()

# createTable = """
# CREATE TABLE classroom (
# student_id INTEGER PRIMARY KEY,
# name VARCHAR(20),
# gender CHAR(1),
# physicsMarks INTEGER,
# mathsMarks INTEGER,
# chemistryMarks INTEGER
# );
# """
# #
# cursor.execute(createTable)


classRoom_DATA = [(1, "Raj", "M", 70, 45, 99),
                  (2, "Shubh", "M", 70, 45, 99),
                  (3, "Ashish", "M", 70, 45, 99),
                  (4, "Aman", "M", 70, 45, 99)
                  ]

for data in classRoom_DATA:
    insert_Statement = """INSERT INTO classroom (student_id, name, gender, physicsMarks, mathsMarks, chemistryMarks)
    VALUES ({0},"{1}","{2}",{3},{4},{5});""".format(data[0], data[1], data[2], data[3], data[4], data[5])
    cursor.execute(insert_Statement)

conn.commit()
# connection.close()

# select_query = "select * from classroom"
# print(cursor)
# result = cursor.fetchall()
# for row in result:
#     print(row)
#
# connection.close()
