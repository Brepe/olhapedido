import os
from flask import Flask
import psycopg2

class PgDatabase(object):

    def connect(self):
        try:
            pg_host = os.getenv("SQL_HOST")
            pg_user = os.getenv("POSTGRES_USER")
            pg_pass = os.getenv("POSTGRES_PASSWORD")
            pg_db = os.getenv("POSTGRES_DB")

            con = psycopg2.connect(dbname=pg_db,
                                    user=pg_user,
                                    host=pg_host,
                                    password=pg_pass)
            
            return con
        except Exception as error:
            print("An exception occurred:", error)
            return False
    

    def exec(self, txt):
        try:
            con = self.connect()
            if con:
                cur = con.cursor()
                cur.execute(txt)
                con.commit()
                self.close(con, cur)

            return True
        
        except Exception as error:
            # handle the exception
            print("An exception occurred:", error)
            return error


    def select(self, txt):
        try:
            con = self.connect()
            if con:
                cur = con.cursor()
                cur.execute(txt)
                items = cur.fetchall()
                con.commit()
                self.close(con, cur)
                return items
            
            return False
        
        except Exception as error:
            # handle the exception
            print("An exception occurred:", error)
            return error


    def close(self, con, cur):
        if cur:
            cur.close()
        if con:
            con.close()
        return True
