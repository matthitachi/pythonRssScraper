import MySQLdb

host = 'localhost'
username = 'root'
password = ''
database = 'atscraper'
db = MySQLdb.connect(host, username, password, database)
cursor = db.cursor()

def exec(sql):
    global db
    global cursor
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    finally:
        db.close()

def fetchone(sql):
    global db
    global cursor
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        result = cursor.fetchone()

    except:
        # Rollback in case there is any error
        print('An error occured')
        result = None

    finally:
        db.close()
        return  result

def fetchall(sql):
    global db
    global cursor
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        result = cursor.fetchall()

    except:
        # Rollback in case there is any error
        print('An error occured')
        result = None

    finally:
        db.close()
        return  result

print(fetchall('Select * from scrapedata'))

