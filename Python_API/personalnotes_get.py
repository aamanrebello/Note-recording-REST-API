from flask import Flask, jsonify
from flask_restful import Api
from json import dumps
from ast import literal_eval
from common_functions import common

app = Flask(__name__)
api = Api(app)

class GET():
    @app.route("/list_notes/<UserID>", methods = ['GET'])
    def get(UserID): #lists all the notes
        common_obj = common()
        info = common.get_info(common_obj)
        info_dict = literal_eval(info)  #CONVERT TO DICTIONARY
        base_path = info_dict["base_path"]  #GET BASE PATH FROM config.txt
        DBconfig = info_dict["DBconfig"] #GET INFO TO CONFIGURE DB CONNECTION
        UIDs = common.getusers(common_obj, DBconfig, base_path)
        if UserID not in UIDs:
            return "404: ID not found", 404

        output = {}     #DICTIONARY WILL BE CONVERTED TO JSON OUTPUT
        output['NOTES'] = []
        output['ARCHIVES'] = []
        Notes = common.getnoteswithdate(common_obj, DBconfig, base_path, UserID)
        for index in range(0, len(Notes), 2):
            f = open((base_path + "Storage/" + UserID + "_notes/" + Notes[index]), "r")
            content = (f.read()).replace("\n" , " ")
            f.close()
            note_output = {
                'topic' : Notes[index],
                'datetime' : Notes[index + 1],
                'actual_note' : content
            }
            output['NOTES'].append(note_output)
        Archives = common.getarchives(common_obj, DBconfig, base_path, UserID)
        for entry in Archives:
            output['ARCHIVES'].append(entry)
        return jsonify(output), 200

if __name__ == '__main__':
    app.run(port ='5002', debug = True)
