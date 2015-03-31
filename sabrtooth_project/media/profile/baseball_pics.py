#!/usr/bin/python
import MySQLdb
import os
import urllib2

# connect
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="",
db="Baseball")

cursor = db.cursor()

#build listbox for selecting line ID

# execute SQL select statement
cursor.execute("Select Master.playerId,nameFirst,nameLast from Master INNER JOIN Batting on Master.playerID=Batting.playerID where Batting.yearID = '2014'")

# commit your changes
db.commit()

# get the number of rows in the resultset
numrows = int(cursor.rowcount)

for y in range(0,numrows):
	row = cursor.fetchone()
	print str(row[0]) + " ---- " + str(row[1]) + " " + str(row[2])
