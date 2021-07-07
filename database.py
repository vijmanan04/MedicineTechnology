import mysql.connector
import datetime
import itertools

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Apnabuddha04$",
    database="volunteering_check_in"
    )

mycursor = mydb.cursor()
#mycursor.execute("DROP TABLE volunteer")
#mycursor.execute("CREATE TABLE volunteer (id VARCHAR(255), date VARCHAR(255), enter VARCHAR(255), go VARCHAR(255), i VARCHAR(255), time VARCHAR(255))")
#query = "ALTER TABLE volunteeer ADD in VARCHAR(255) AFTER go"

def add(id, date, enter, leave, here, time):
    sqlFormula = "INSERT INTO volunteer (id, date, enter, go, i, time) VALUES (%s, %s, %s, %s, %s, %s)"
    volunteer = (f"{id}", f"{date}", f"{enter}", f"{leave}", f"{here}", time)
    mycursor.execute(sqlFormula, volunteer)
    mydb.commit()

def remove(id, date, leave, here, tdelta):
    sqlFormula2 = f"UPDATE volunteer SET go = '{leave}', i = '0', time = '{tdelta}' WHERE id = '{id}' and i = '{here}' "
    mycursor.execute(sqlFormula2)
    print(id, here)
    mydb.commit()
    
def select(id):
    sqlFormula3 = f"SELECT date, enter, go, time FROM volunteer where id = '{id}'"
    print(sqlFormula3)
    mycursor.execute(sqlFormula3)
    db = mycursor.fetchall()
    return db
def extract_time(id):
    sqlFormula4 = f"SELECT enter FROM volunteer where id = '{id}' and i = '1'"
    mycursor.execute(sqlFormula4)
    row = mycursor.fetchone()
    return (row[0])
def extract_total_time(id):
    sqlFormula5 = f"SELECT time FROM volunteer where id = '{id}'"
    mycursor.execute(sqlFormula5)
    row = mycursor.fetchall()
    l1 = list(itertools.chain(*row))
    l1 = [float(i) for i in l1]
    return round(sum(l1), 2)