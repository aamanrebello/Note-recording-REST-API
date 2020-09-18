from flask import Flask, request, jsonify
from flask_restful import Api
from ast import literal_eval
from common_functions import common
from modify_db import New_Entry
import os
import shutil

app = Flask(__name__)
api = Api(app)

class THE_USER():

    # ADDS A NEW USER TO DB AND STORAGE.
    @app.route("/" , methods = ['POST'])
    def create_user():
        Uname = request.json["username"]
        Identification = request.json["userID"]
        common_obj = common()
        info = common.get_info(common_obj)
        info_dict = literal_eval(info)
        base_path = info_dict["base_path"]  #GATHERING BASE PATH FROM config.txt
        DBconfig = info_dict["DBconfig"]    #GETTING INFO TO CONFIGURE DB CONNECTION
        UIDs = common.getusers(common_obj, DBconfig, base_path)
        if Identification in UIDs:
            return "403: ID already exists, provide different ID", 403
        else:
            new_entry_obj = New_Entry()
            New_Entry.new_user(new_entry_obj, Uname, Identification) #EXECUTING SQL
            New_Entry.close_connections(new_entry_obj)
            if not os.path.exists((base_path + "Storage/" + Identification + "_notes/Archives")):
                os.makedirs((base_path + "Storage/" + Identification + "_notes/Archives")) #CREATE USER STORAGE
                return "201: User Created", 201
            else:
                return "403: ID already exists, provide different ID", 403


    # REMOVES USER FROM DB AND STORAGE.
    @app.route("/<UserID>" , methods = ['DELETE'])
    def remove_user(UserID):
        common_obj = common()
        info = common.get_info(common_obj)
        info_dict = literal_eval(info)
        base_path = info_dict["base_path"]  #GATHERING BASE PATH FROM config.txt
        DBconfig = info_dict["DBconfig"]    #GETTING INFO TO CONFIGURE DB CONNECTION
        UIDs = common.getusers(common_obj, DBconfig, base_path)
        if UserID not in UIDs:
            return "404: ID does not exist", 404
        new_entry_obj = New_Entry()
        New_Entry.delete_user(new_entry_obj, UserID) #EXECUTING SQL
        New_Entry.close_connections(new_entry_obj)
        shutil.rmtree((base_path + "Storage/" + UserID + "_notes"))
        return "201: User Deleted", 201

if __name__ == '__main__':
    app.run(port ='5004', debug = True)
