from flask import Flask, jsonify
from flask_restful import Api
from ast import literal_eval
from common_functions import common
from modify_db import New_Entry
import os

app = Flask(__name__)
api = Api(app)

class DELETE():

    # USED TO DELETE PERSONAL TEXT NOTE FOR A USER.
    @app.route("/note/<UserID>/<topic>", methods = ['DELETE'])
    def delete_note(UserID, topic):
        file_to_search = str(topic) + ".txt"
        common_obj = common()
        info = common.get_info(common_obj)
        info_dict = literal_eval(info)  #CONVERT TO DICTIONARY
        base_path = info_dict["base_path"]  #GATHERING BASE PATH FROM config.txt
        DBconfig = info_dict["DBconfig"]
        UIDs = common.getusers(common_obj, DBconfig, base_path)
        if UserID not in UIDs:
            return "404: ID not found", 404
        Notes = common.getnotes(common_obj, DBconfig, base_path, UserID)
        if file_to_search in Notes:
            new_entry_obj = New_Entry()
            New_Entry.delete_note_in_db(new_entry_obj, UserID, file_to_search) #EXECUTING SQL
            New_Entry.close_connections(new_entry_obj)
            os.remove((base_path + "Storage/" + UserID +"_notes/" + file_to_search))
            return "200 : Operation successful", 200
        else:
            return "404 : file could not be found", 404


    # USED TO DELETE ARCHIVED NOTE FOR A USER.
    @app.route("/archive/<UserID>/<topic>", methods = ['DELETE'])
    def delete_archive(UserID, topic):
        file_to_search = str(topic) + ".txt"
        common_obj = common()
        info = common.get_info(common_obj)
        info_dict = literal_eval(info)  #CONVERT TO DICTIONARY
        base_path = info_dict["base_path"]  #GATHERING BASE PATH FROM config.txt
        DBconfig = info_dict["DBconfig"]
        UIDs = common.getusers(common_obj, DBconfig, base_path)
        if UserID not in UIDs:
            return "404: ID not found", 404
        Archives = common.getarchives(common_obj, DBconfig, base_path, UserID)
        if file_to_search in Archives:
            new_entry_obj = New_Entry()
            New_Entry.delete_archive_in_db(new_entry_obj, UserID, file_to_search) #EXECUTING SQL
            New_Entry.close_connections(new_entry_obj)
            os.remove((base_path + "Storage/" + UserID +"_notes/Archives/" + file_to_search + ".gz"))
            return "200 : Operation successful", 200
        else:
            return "404 : file could not be found", 404


if __name__ == '__main__':
    app.run(port ='5005', debug = True)
