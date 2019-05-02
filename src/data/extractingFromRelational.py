import sqlite3

connection = sqlite3.connect("classRoomDB.db")

cursor = connection.cursor()

# createTable = """
# CREATE TABLE classroom (
# student_id INTEGER PRIMARY_KEY,
# name VARCHAR,
# gender CHAR(1),
# physicsMarks INTEGER,
# mathsMarks INTEGER,
# chemistryMarks INTEGER
# )
# """
#
# cursor.execute(createTable)

#
# classRoom_DATA = [(1, "Raj", "M", 70, 45, 99),
#                   (1, "Shubh", "M", 70, 45, 99),
#                   (1, "Ashish", "M", 70, 45, 99),
#                   (1, "Aman", "M", 70, 45, 99)
#                   ]
#
# for data in classRoom_DATA:
#     insert_Statement = """INSERT INTO classroom (student_id, name, gender, physicsMarks, mathsMarks, chemistryMarks)
#     VALUES ({0},"{1}","{2}",{3},{4},{5});""".format(data[0], data[1], data[2], data[3], data[4], data[5])
#     cursor.execute(insert_Statement)
#
# connection.commit()
# connection.close()

select_query = "select * from classroom"
print(cursor)
result = cursor.fetchall()
for row in result:
    print(row)

connection.close()
