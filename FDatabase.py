import sqlite3

class FDatabase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_active(self):
        sql = '''SELECT id, login FROM users WHERE status = 'active' '''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("FAIL")
        return []

    def getlog(self, log):
        try:
            self.__cur.execute("SELECT id, login FROM users WHERE login = " + "'" + log + "'")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Some error while getlog " + str(e))
        return []


    def getid(self, id):
        print(id)
        try:
            self.__cur.execute("SELECT id, login FROM users WHERE id = " + "'" + id + "'")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Some error while getid " + str(e))
        return []
