import pyodbc

class common(object):

    def get_info(self):
            fi = open("config.txt", "r") #READING config.txt
            info = fi.read()
            fi.close()
            return info


    def getusers(self, DBconfig, base_path):
            conn = pyodbc.connect(DBconfig + 'DefaultDir=' + base_path + 'Storage;DBQ=' + base_path + 'Storage/API_Users.mdb;')
            cursor = conn.cursor()
            cursor.execute("SELECT Users.UID FROM Users")
            UIDs = ()
            for row in cursor.fetchall():
                UIDs = UIDs + tuple(row) # GATHERING ALL User IDs.
            cursor.close()
            conn.close()
            return UIDs

    def getarchives(self, DBconfig, base_path, UserID):
            conn = pyodbc.connect(DBconfig + 'DefaultDir=' + base_path + 'Storage;DBQ=' + base_path + 'Storage/API_Users.mdb;')
            cursor = conn.cursor()
            cursor.execute("SELECT Archives.FileName FROM Archives WHERE Archives.UserID = ?", (UserID))
            Archives = ()
            for row in cursor.fetchall():
                Archives = Archives + tuple(row) # GATHERING ALL Note filenames.
            cursor.close()
            conn.close()
            return Archives

    def getnotes(self, DBconfig, base_path, UserID):
            conn = pyodbc.connect(DBconfig + 'DefaultDir=' + base_path + 'Storage;DBQ=' + base_path + 'Storage/API_Users.mdb;')
            cursor = conn.cursor()
            cursor.execute("SELECT Notes.FileName FROM Notes WHERE Notes.UserID = ?", (UserID))
            Notes = ()
            for row in cursor.fetchall():
                Notes = Notes + tuple(row) # GATHERING ALL Note filenames.
            cursor.close()
            conn.close()
            return Notes

    def getnoteswithdate(self, DBconfig, base_path, UserID):
            conn = pyodbc.connect(DBconfig + 'DefaultDir=' + base_path + 'Storage;DBQ=' + base_path + 'Storage/API_Users.mdb;')
            cursor = conn.cursor()
            cursor.execute("SELECT Notes.FileName, Notes.Creation FROM Notes WHERE Notes.UserID = ?", (UserID))
            Note_details = ()
            for row in cursor.fetchall():
                Note_details = Note_details + tuple(row) # GATHERING ALL Note filenames.
            cursor.close()
            conn.close()
            return Note_details

    def modify_init(self, personal_notes, archived_notes):
            f = open("__init__.py", "w")    #MODIFYING __init__.py
            new_file_content = "personal_notes = " + str(personal_notes) + "\n" + "archived_notes = " + str(archived_notes)
            f.write(new_file_content)
            f.close()
