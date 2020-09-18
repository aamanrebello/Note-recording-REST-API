from flask import Flask
from flask_restful import Api
from ast import literal_eval
from common_functions import common
from modify_db import New_Entry
import os
import shutil
import gzip
import datetime


app = Flask(__name__)
api = Api(app)

class ARCHIVE():

    # USED TO MOVE A GIVEN TEXT FILE TO ARCHIVED STORAGE (CONVERTS TO .gzip format).
    @app.route("/send/<UserID>/<topic>", methods = ['PUT'])
    def move_to_archive(UserID, topic):
        file_to_search = str(topic) + ".txt" #BASE DEFINITIONS
        common_obj = common()
        info = common.get_info(common_obj)
        info_dict = literal_eval(info)
        base_path = info_dict["base_path"] #GETTING BASE PATH FROM config.txt
        DBconfig = info_dict["DBconfig"] #GETTING INFO TO CONFIGURE DB CONNECTION
        UIDs = common.getusers(common_obj, DBconfig, base_path)
        if UserID not in UIDs:
            return "404: ID not found", 404
        Notes = common.getnotes(common_obj, DBconfig, base_path, UserID)
        if file_to_search in Notes:
            new_entry_obj = New_Entry()
            New_Entry.delete_note_in_db(new_entry_obj, UserID, str(topic + ".txt"))
            New_Entry.new_archive_in_db(new_entry_obj, UserID, str(topic + ".txt"), str(datetime.datetime.now()))
            New_Entry.close_connections(new_entry_obj)
            src = base_path + "Storage/" + UserID + "_notes/" + file_to_search
            dst = base_path + "Storage/"+ UserID + "_notes/Archives/" + file_to_search
            shutil.move(src, dst)    #MOVE TEXT FILE INTO ARCHIVE FOLDER
            with open(dst, 'rb') as f_in, gzip.open(dst + '.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)   #COMPRESS TO .gz
            os.remove((base_path + "Storage/" + UserID +"_notes/Archives/" + file_to_search))
            return "200: archiving successful" ,200
        else:
            return "404: file not found", 404


    # USED TO RECALL ARCHIVED FILE TO MAIN STORAGE (CONVERTS FROM .gzip TO .txt)
    @app.route("/recall/<UserID>/<topic>", methods = ['PUT'])
    def recall_archive(UserID, topic):
        file_to_search = str(topic) + ".txt" #BASE DEFINITIONS
        common_obj = common()
        info = common.get_info(common_obj)
        info_dict = literal_eval(info)
        base_path = info_dict["base_path"] #GETTING BASE PATH FROM config.txt
        DBconfig = info_dict["DBconfig"] #GETTING INFO TO CONFIGURE DB CONNECTION
        UIDs = common.getusers(common_obj, DBconfig, base_path)
        if UserID not in UIDs:
            return "404: ID not found", 404
        Archives = common.getarchives(common_obj, DBconfig, base_path, UserID)
        if file_to_search in Archives:
            new_entry_obj = New_Entry()
            New_Entry.delete_archive_in_db(new_entry_obj, UserID, str(topic + ".txt"))
            New_Entry.new_note_in_db(new_entry_obj, UserID, str(topic + ".txt"), str(datetime.datetime.now()))
            New_Entry.close_connections(new_entry_obj)
            src = base_path + "Storage/"+ UserID + "_notes/Archives/" + file_to_search
            with gzip.open(src + ".gz", 'rb') as f_in, open(src, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)   #UNZIP
            os.remove((base_path + "Storage/" + UserID +"_notes/Archives/" + file_to_search + ".gz"))
            dst = base_path + "Storage/" + UserID + "_notes/" + file_to_search
            shutil.move(src, dst)    #MOVE TEXT FILE INTO USER FOLDER
            return "200: unzip successful" ,200
        else:
            return "404: file not found", 404

if __name__ == '__main__':
    app.run(port = '5007', debug = True)
