from flask import Flask, jsonify, request
from flask_restful import Api
from ast import literal_eval
from common_functions import common
import datetime


app = Flask(__name__)
api = Api(app)

class UPDATE():

    # USED TO REWRITE AN EXISTING NOTE OF A USER.
    @app.route('/<UserID>/rewrite', methods = ['PUT'])
    def rewrite_file(UserID):
        new_note = request.json["content"]
        topic = request.json["topic"]

        index = 0
        file_found = False
        file_to_search = str(topic) + ".txt"
        common_obj = common()
        info = common.get_info(common_obj)
        info_dict = literal_eval(info)  #CONVERT TO DICTIONARY
        base_path = info_dict["base_path"]  #GATHERING BASE PATH FROM config.txt
        DBconfig = info_dict["DBconfig"] #GETTING INFO TO CONFIGURE DB CONNECTION
        UIDs = common.getusers(common_obj, DBconfig, base_path)
        if UserID not in UIDs:
            return "404: ID not found", 404
        Notes = common.getnotes(common_obj, DBconfig, base_path, UserID)
        if file_to_search in Notes:
            f = open((base_path + "Storage/" + UserID + "_notes/" + file_to_search), "w+")
            f.write(new_note)
            f.close()
            return "201: file updated", 201
        else:
            return "404: file not found", 404


    # USED TO APPEND TEXT TO AN EXISTING NOTE OF A USER.
    @app.route('/<UserID>/append', methods = ['PUT'])
    def append(UserID):
        addition = request.json["content"]
        topic = request.json["topic"]

        index = 0
        file_found = False
        file_to_search = str(topic) + ".txt"
        common_obj = common()
        info = common.get_info(common_obj)
        info_dict = literal_eval(info)  #CONVERT TO DICTIONARY
        base_path = info_dict["base_path"]  #GATHERING BASE PATH FROM config.txt
        DBconfig = info_dict["DBconfig"] #GETTING INFO TO CONFIGURE DB CONNECTION
        UIDs = common.getusers(common_obj, DBconfig, base_path)
        if UserID not in UIDs:
            return "404: ID not found", 404
        Notes = common.getnotes(common_obj, DBconfig, base_path, UserID)
        if file_to_search in Notes:
            f = open((base_path + "Storage/" + UserID + "_notes/" + file_to_search), "a+")
            f.write(addition)
            f.close()
            return "201: file updated", 201
        else:
            return "404: file not found", 404


    # USED TO PREPEND TEXT TO AN EXISTING NOTE OF A USER.
    @app.route('/<UserID>/prepend', methods = ['PUT'])
    def prepend(UserID):
        addition = request.json["content"]
        topic = request.json["topic"]

        index = 0
        file_found = False
        file_to_search = str(topic) + ".txt"
        common_obj = common()
        info = common.get_info(common_obj)
        info_dict = literal_eval(info)  #CONVERT TO DICTIONARY
        base_path = info_dict["base_path"]  #GATHERING BASE PATH FROM config.txt
        DBconfig = info_dict["DBconfig"] #GETTING INFO TO CONFIGURE DB CONNECTION
        UIDs = common.getusers(common_obj, DBconfig, base_path)
        if UserID not in UIDs:
            return "404: ID not found", 404
        Notes = common.getnotes(common_obj, DBconfig, base_path, UserID)
        if file_to_search in Notes:
            f = open((base_path + "Storage/" + UserID + "_notes/" + file_to_search), "r+")
            old = f.read()
            f.seek(0)
            f.write(addition + " " + old)
            f.close()
            return "201: file updated", 201
        else:
            return "404: file not found", 404


if __name__ == '__main__':
    app.run(port ='5006', debug = True)
