#Day 7 Assignment by Krish Sharma, email: ksysknp@gmail.com

import mysql.connector as sqlcon        #impoted it as sqlcon

db = sqlcon.connect(host = "localhost", user = "root", passwd = "system", database = 'essentials')

cur = db.cursor()

cur.execute("update student set mark = 98 where sname = 'Krish Sharma'")        #updated database with new marks and name
cur.execute("select * from student")        #dsiplayed table

for i in cur:               #printed table values
	print(i)

cur.close()         #closed database connection 
db.commit()           #saved all data to database