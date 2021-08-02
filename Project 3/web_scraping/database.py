import dbconfig
import mysql.connector
import json

mydb = mysql.connector.connect(**dbconfig.config)
mycursor = mydb.cursor()
    
def get_data(username):
    mycursor.execute("SELECT * FROM user where username = {}".format(username))
    myresult = mycursor.fetchall()
    return myresult

def add_data(name, work, city, username):
    if len(work)==0 :
        sql = "UPDATE user SET name = %s, city = %s WHERE username = %s"
        val = (name,city,username)
    else :
        sql = "UPDATE user SET name = %s, work = %s, city = %s WHERE username = %s"
        val = (name, json.dumps(work),city,username)
    mycursor.execute(sql, val)
    mydb.commit()

def get_whole_data():
    mycursor.execute("SELECT username FROM user")
    myresult = mycursor.fetchall()
    return myresult