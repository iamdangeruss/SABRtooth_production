import os
import MySQLdb

# connect
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="m@rl0we",
db="SABR")
cursor = db.cursor()
for filename in os.listdir('static/img/profile/'):
     filename
     player =  os.path.splitext(filename)[0]
     
     
     
     sql = "UPDATE Master SET image='profile/" + filename + "' WHERE playerid= '" + player + "';" 
     
     cursor.execute(sql)
     
     print sql
     
	