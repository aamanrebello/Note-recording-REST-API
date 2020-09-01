import pyodbc
from ast import literal_eval
from common_functions import common

class New_Entry(object):

    def __init__(self):
        obj = common()
        info = common.get_info(obj)
        info_dict = literal_eval(info) #CONVERT TO DICTIONARY
        base_path = info_dict["base_path"]  #GET BASE PATH FROM config.txt
        DBconfig = info_dict["DBconfig"] #GET INFO TO CONFIGURE DB CONNECTION
        self.conn = pyodbc.connect(DBconfig + 'DefaultDir=' + base_path + 'Storage;DBQ=' + base_path + 'Storage/API_Users.mdb;')
        self.cursor = self.conn.cursor()

    def new_user(self, Username, UID):
        self.cursor.execute("INSERT INTO Users (User, UID) VALUES(?, ?)" , (Username, UID))
        self.conn.commit()

    def delete_user(self, UID):
        self.cursor.execute("DELETE FROM Users WHERE UID = ?", (UID))
        self.conn.commit()

    def new_note_in_db(self, UID, filename, datetime):
        self.cursor.execute("INSERT INTO Notes (UserID, FileName, Creation) VALUES(?, ?, ?)" , (UID, filename, datetime))
        self.conn.commit()

    def delete_note_in_db(self, UID, filename):
        self.cursor.execute("DELETE FROM Notes WHERE UserID = ? AND FileName = ?", (UID, filename))
        self.conn.commit()

    def new_archive_in_db(self, UID, filename, datetime):
        self.cursor.execute("INSERT INTO Archives (UserID, FileName, Creation) VALUES(?, ?, ?)" , (UID, filename, datetime))
        self.conn.commit()

    def delete_archive_in_db(self, UID, filename):
        self.cursor.execute("DELETE FROM Archives WHERE UserID = ? AND FileName = ?", (UID, filename))
        self.conn.commit()

    def close_connections(self):
        self.cursor.close()
        self.conn.close()
