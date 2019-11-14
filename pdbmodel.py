import psycopg2
import psycopg2.extras
from xmlparser import Xmlparser

class PdbModel :

    def __init__(self, database):
        self.db_settings = Xmlparser.get_db_config(Xmlparser, 'config.xml')
        self.database = database


    def open(self):
        try:
            self.connection = psycopg2.connect(user = self.db_settings.get("user"),
                                    password = self.db_settings.get("password"),
                                    host = self.db_settings.get("host"),
                                    port = self.db_settings.get("port"),
                                    database = self.database)
            self.cursor = self.connection.cursor()
            # Print PostgreSQL Connection properties
            # print ( self.connection.get_dsn_parameters(),"\n")
            # Print PostgreSQL version
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            # print("You are connected to - ", record,"\n")
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)

    def execute(self, sql, option=None):
        self.open()
        if (option == None):
            return self.cursor.execute(sql)
        else:
            return self.cursor.execute(sql, option)

    def exec(self, sql, option = None):
        try:
            # Execute the SQL command
            result = self.execute(sql, option)
            # Commit your changes in the database
            self.connection.commit()
        except Exception as e :
            # Rollback in case there is any error
            print("An error occurred in exec method")
            self.connection.rollback()
            print(e)
            result = None

        finally:
            self.close()
            return result

    def fetchone(self, sql, option = None):
        self.open()
        try:
            # Execute the SQL command
            self.execute(sql, option)
            # Commit your changes in the database
            result = self.cursor.fetchone()

        except Exception as e:
            # Rollback in case there is any error
            print('An error occured in fetch one method')
            print(e)
            result = None

        finally:
            self.close()
            return  result


    def fetchall(self, sql, option = None):
        self.open()
        try:
            # Execute the SQL command
            self.execute(sql, option)
        # Commit your changes in the database
            result = self.cursor.fetchall()

        except Exception as e:
            # Rollback in case there is any error
            print('An error occured in feetchall method')
            print(e)
            result = None

        finally:
            self.close()
            return result

    def close(self):
        if (self.connection):
            self.cursor.close()
            self.connection.close()
            # print("PostgreSQL connection is closed")

    def sortInstrumentId(self, insId):
        sql = "Select secid from instrumentids WHERE instrumentid = '%s'" % (str(insId))
        result = self.fetchone(sql)
        return result

    def sortCropId(self, secId):
        sql = "Select corp_id from securities WHERE sec_id = '%s'" % (str(secId))
        result = self.fetchone(sql)
        return result

    def articleExist(self, link):
        sql = "Select * from scrapedata WHERE url = '%s'" % (link)
        result = self.fetchone(sql)
        return result

    def insertScrapeData(self, data, tags):
        # print(data)
        columns = "("
        values = "("
        params = "("
        for i in data:
            columns += i+","
            values += "'"+self.postgres_escape_string(data[i]) +"',"
            params += "%s" +","

            # columns = "(" + ", ".join(i) + ")"
            # values = "(" + ", ".join(data[i]) + ")"
        columns =  columns.rstrip(',')+")"
        values = values+")"
        params = params.rstrip(',')+")"
        # columns = "(" + ", ".join(data.keys()) + ")"
        # values = "(" + ", ".join(data.values()) + ")"
        # values2 = tuple(data.values())
        print(eval(values))
        sql = "insert into scrapedata "+ columns +" values " +params + " RETURNING id"
        insertid = self.execute(sql, eval(values))
        self.connection.commit()
        print(sql, values)
        if(tags):
            # print(self.getLastInsertID())
            self.insertTagsData(self.getLastInsertID(), tags)
        self.close()

    def postgres_escape_string(self, s):
        if not isinstance(s, str):
            raise TypeError("%r must be a str or unicode" % (s,))
        escaped = repr(s)
        if isinstance(s, bytes):
            assert escaped[:1] == 'u'
            escaped = escaped[1:]
        if escaped[:1] == '"':
            escaped = escaped.replace("'", "\\'")
        elif escaped[:1] != "'":
            raise AssertionError("unexpected repr: %s", escaped)
        return "%s" % (escaped[1:-1],)

    def getLastInsertID(self):
        insertid = self.cursor.fetchone()[0]
        return insertid

    def insertTagsData(self, insertId, tags):
        for tag in tags:
            if tag:
                import time
                secondsSinceEpoch = time.time()
                dateobj = time.localtime(secondsSinceEpoch)
                crop_id = str(self.sortCropId(tag)[0])
                dt= str('%d-%d-%d %d:%d:%d' % (
                    dateobj.tm_year, dateobj.tm_mon, dateobj.tm_mday, dateobj.tm_hour, dateobj.tm_min, dateobj.tm_sec))
                sql = "insert into atsecdata (article_id, sec_id, created_at, crop_id) VALUES (%s, %s, %s, %s)"
                self.exec(sql, (insertId, tag, dt, crop_id))

    def updateFeedback(self, count):
        sql = "Update scrapedata set feedbacks = '"+str(count)+"', ck_feedback = '1'"
        self.exec(sql)

# pd = PdbModel("atscraper")
# pd.insertTagsData(44, [443])
# print(pd.sortInstrumentId(83))
# db_settings = Xmlparser.get_db_config(Xmlparser, 'config.xml')
# print(db_settings.get('user'))
# pd.exec("""
# insert into scrapedata (website, url) VALUES ('crop.com', 'collage')
# """)
# print(pd.fetchone("""insert into instrumentID ()"""))
# pd.close()