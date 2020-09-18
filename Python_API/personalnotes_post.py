from flask import Flask, request, jsonify
from flask_restful import Api
from ast import literal_eval
from common_functions import common
from modify_db import New_Entry
import datetime


app = Flask(__name__)
api = Api(app)

class POST_NOTE():

    # USED TO ADD A NEW NOTE FOR A USER.
    @app.route("/<UserID>" , methods = ['POST'])
    def post(UserID):
        note = request.json["content"]
        topic = request.json["topic"] #RECEIVE DATA AS JSON

        common_obj = common()
        info = common.get_info(common_obj)
        info_dict = literal_eval(info) #CONVERT TO DICTIONARY
        base_path = info_dict["base_path"]  #GETTING BASE PATH FROM config.txt
        DBconfig = info_dict["DBconfig"] #GETTING INFO TO CONFIGURE DB CONNECTION
        UIDs = common.getusers(common_obj, DBconfig, base_path)
        if UserID not in UIDs:
            return "404: ID not found", 404

        Notes = common.getnotes(common_obj, DBconfig, base_path, UserID)
        if str(topic + ".txt") in Notes:
            return "404: Note already exists - to edit/delete please use the rewrite/delete functionality.", 404
        Archives = common.getarchives(common_obj, DBconfig, base_path, UserID)
        if str(topic + ".txt") in Archives:
            return "404: Note with same filename exists in archives. Recommended: add \'(n)\' after filename where n is version number.", 404
        new_entry_obj = New_Entry()
        New_Entry.new_note_in_db(new_entry_obj, UserID, str(topic + ".txt"), str(datetime.datetime.now()))
        New_Entry.close_connections(new_entry_obj)

        f = open((base_path + "Storage/" + UserID + "_notes/" + topic + ".txt"), "w") #NEW NOTE FILE
        f.write(note)
        f.close()

        return "201 : posting successful", 201

if __name__ == '__main__':
    app.run(port ='5003', debug = True)
