import os
import psycopg2

''' Conecções ao banco.
    Funções do CRUD herdadas por todos objetos (Cada objeto é uma tabela do banco). '''
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
        
    def close(self, con, cur):
        if cur:
            cur.close()
        if con:
            con.close()
        return True

    def create(self, table, columns, table_data):
        try:
            con = self.connect(self)
            if con:
                cur = con.cursor()
                table_data =str(table_data)
                cur.execute("INSERT INTO "+ table +" "+ columns +" VALUES "+ table_data +";")
                con.commit()
                self.close(self, con, cur)

            return True
        
        except Exception as error:
            # handle the exception
            con.rollback()
            self.close(self, con, cur)
            print("An exception occurred:", error)
            return str(error)

    '''
    _______________________________________________________________
    Se houver apenas uma coluna para o SELECT 
        Por exemplo "nome" apenas adicionará seus respectivos dados 
        em filter_data_fm para WHERE 
    _______________________________________________________________
    Se houverem mais de uma coluna para o SELECT 
        Por exemplo ["nome","datanasc"]
        entrará no laço FOR para adicionar com AND essas colunas e
        seus respectivos dados em filter_data_fm para WHERE 
    _______________________________________________________________
    '''
    def obtain(self, table, column, filter_data):
        try:
            con = self.connect(self)
            if con:
                cur = con.cursor()
                if isinstance(column, list):
                    string_select = "SELECT * FROM "+ table +" WHERE "

                    for i, col in enumerate(column):
                        filter_data_fm =  self.format_data_where_in(self, filter_data[i])
                        string_select += " AND " if i > 0 else " "
                        string_select += " "+ col +" IN ( "+ filter_data_fm +" )"

                    string_select += ";"
                else:
                    filter_data_fm =   self.format_data_where_in(self, filter_data)
                    string_select = "SELECT * FROM "+ table + \
                               " WHERE "+ column +" IN ( "+ filter_data_fm +" );"
                
                cur.execute(string_select)
                        
                items = cur.fetchall()
                con.commit()
                self.close(self,con, cur)
                return items
            return False
        
        except Exception as error:
            # handle the exception
            con.rollback()
            self.close(self, con, cur)
            print("An exception occurred:", error)
            return str(error)

    def update(self, table,  id_, table_data):
        try:
            con = self.connect(self)
            if con:
                cur = con.cursor()
                cur.execute("UPDATE "+ table +" SET "+ table_data +" WHERE id = "+ id_ +";")

                con.commit()
                self.close(self,con, cur)

            return True
        
        except Exception as error:
            # handle the exception
            con.rollback()
            self.close(self, con, cur)
            print("An exception occurred:", error)
            return str(error)

    def delete(self, table, id_):
        try:
            con = self.connect(self)
            if con:
                cur = con.cursor()
                cur.execute("DELETE FROM "+table+" WHERE id = "+id_+";")   
                con.commit()
                self.close(self,con, cur)
                return True
            return False
        
        except Exception as error:
            # handle the exception
            con.rollback()
            self.close(self, con, cur)
            print("An exception occurred:", error)
            return str(error)

    def general_query(self, txt):
        try:
            con = self.connect(self)
            if con:
                cur = con.cursor()
                cur.execute(txt)
                items = cur.fetchall()

                con.commit()
                self.close(self,con, cur)
                return items
            return True
        
        except Exception as error:
            # handle the exception
            con.rollback()
            self.close(self, con, cur)
            print("An exception occurred:", error)
            return str(error)

    def format_data_where_in(self, variable):
        if isinstance(variable, list):
            filter_data_fm =  ", ".join([f"'{item}'" if isinstance(item, str) else f'{item}' for item in variable]) 
        else:
            filter_data_fm = "".join(f"'{variable}'")
        return filter_data_fm
