import sqlite3
import time
import datetime
import random
import csv

conn = sqlite3.connect('pro1.db')
c = conn.cursor()
print ("Done")

c.execute("CREATE TABLE IF NOT EXISTS project('dist' REAL, 'datestamp' REAL)")

count = 0
    #cursor.execute('INSERT INTO \'daily_new\' (date, cust_bal, cust_credit, fund_stock, fund_hyb, fund_bond ) VALUES({}, {}, {}, {}, {}, {})'.format(row[0], row[1], row[2], row[3], row[4], row[5]))
with open('testfile.csv','r') as infile:
    dr = csv.reader(infile,delimiter=',')
    for x in dr:
        dist = x[0]
        time = count
        print ("Done")
        c.execute("INSERT INTO lolol(dist,datestamp) VALUES(?,?)",(dist,time))
        count = count + 0.5
        conn.commit()

c.close()
conn.close()
