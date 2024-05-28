from model import database as db

'''
Exemplos de uso da classe
    Users.create(Users,"teste@mail.com", "21999999999", "password", "nameteste")
    Users.obtain(Users,"name", "nameteste2")
    Users.obtain(Users,"name", ["nameteste","Snack & Cake"])
    Users.obtain(Users,["name","email"], [["nameteste"],["teste@mail.com"]])
    Users.update(Users,"34","teste2@mail.com", "21999999999", "password2", "nameteste2")
    Users.delete(Users,"34")
'''
class Users(db.PgDatabase):
    def create(self, email, phone, password, name):
        table = str(self().__class__.__name__)
        table_data = (email, phone, password, name)
        columns = "(email, phone, password, name)"
        return super().create(self, table, columns, table_data)

    def obtain(self, column, filter_data):
        table = str(self().__class__.__name__)
        return super().obtain(self, table, column, filter_data)
        
    def update(self, id_, email, phone, password, name):
        table = str(self().__class__.__name__)
        table_data = "email = '"+email+"', phone = '"+phone+"',password = '"+password+"', name = '"+name+"'"
        return super().update(self, table, id_, table_data)

    def delete(self, id_):
        table = str(self().__class__.__name__)
        return super().delete(self, table, id_)
