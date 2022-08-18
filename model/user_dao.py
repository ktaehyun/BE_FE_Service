import json
import pymysql

class UserDao:

    def __init__(self, database):
        self.db = database

    def get_CarPlate(self):
        cursor = self.db.cursor()
        sql = """
                SELECT * FROM CarPlate
                """
        # cursor.execute(sql, (user['user']))
        cursor.execute(sql)
        self.db.commit()
        self.db.close()