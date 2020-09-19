import requests
import json

# DOCUMENTATION : This is a basic program that manipulates the API according to user provided input.

#------------------------------------------------------------------------------------------------------

# Since listing notes is so ubiquitously used - we define it as a separate function used below.
def list_notes():
    user_id = input("Please provide user ID number: ")
    get_url = "http://127.0.0.1:5002/" + user_id
    r = requests.get(get_url)
    print("HERE ARE YOUR CURRENT NOTES LISTED:\n")
    print(r.text)
    print()
    # No need to ask user to provide ID after calling this function.
    return user_id

#------------------------------------------------------------------------------------------------------

# Keep iterating as long as the user wants to perform operations.
while True:
    # Initial prompt to find out which action the user wants to do.
    print("1: Create new user,\t 2: Delete user,\t 3: Post new note,\t 4: Edit existing note")
    print("5: Archive existing note\t 6: Recall an archive\t 7: Delete note/archive\t 8: List notes\n")
    print("Entering any other character will terminate the program.\n")
    code = input("ENTER THE NUMBER OF THE OPERATION YOU WANT: ")

    #--------------------------------------------------------------------------------------
    if code == "1":
        user_name = input("Please provide username: ")
        user_id = input("Please provide user ID number: ")
        # Marshalling user details.
        new_user = {
            'username' : user_name,
            'userID' : user_id
        }
        # Post new user.
        t = requests.post('http://127.0.0.1:5004/', json = new_user)
        print(t.text)
        print()

    #----------------------------------------------------------------------------------------

    elif code == "2":
        user_id = input("Please provide user ID number: ")
        # Preparing url to send delete request
        url = "http://127.0.0.1:5004/" + user_id
        # send delete request.
        t = requests.delete(url)
        print(t.text)
        print()

    #-----------------------------------------------------------------------------------------

    elif code == "3":
        # List notes first.
        user_id = list_notes()
        # Preparing url to send post request
        post_url = "http://127.0.0.1:5003/" + user_id
        # Obtaining user provided information.
        topic = input("Please provide topic of the new personal note (must be unique): ")
        content = input("Now you can enter the text content of your note: ")
        entry = {
            "topic" : topic,
            "content" : content
        }
        # Post note
        r = requests.post(post_url, json = entry)
        print(r.text)
        print()

    #-----------------------------------------------------------------------------------------


    elif code == "4":
        print("1: Prepend existing note,\t 2: Append existing note,\t 3: Rewrite existing note.\n")
        sub_code = input("ENTER THE OPERATION YOU WANT TO PERFORM. Any other code will skip this operation. ")
        # List notes first.
        user_id = list_notes()
        # # Preparing url and information to send put request based on sub_code
        if sub_code == "1":
            # Take in user information.
            topic = input("Please provide topic of the existing personal note: ")
            content = input("Now you can enter the prepend content of your note: ")
            entry = {
                "topic" : topic,
                "content" : content
            }
            put_url = "http://127.0.0.1:5006/" + user_id + "/prepend"

        elif sub_code == "2":
            # Take in user information.
            topic = input("Please provide topic of the existing personal note: ")
            content = input("Now you can enter the append content of your note: ")
            entry = {
                "topic" : topic,
                "content" : content
            }
            put_url = "http://127.0.0.1:5006/" + user_id + "/append"

        elif sub_code == "3":
            # Take in user information.
            topic = input("Please provide topic of the existing personal note: ")
            content = input("Now you can enter the new content of your note: ")
            entry = {
                "topic" : topic,
                "content" : content
            }
            put_url = "http://127.0.0.1:5006/" + user_id + "/rewrite"
        else:
            continue
        s = requests.put(put_url, json = entry)
        print(s.text)
        print()

    #--------------------------------------------------------------------------------------------

    elif code == "5":
        # List notes first.
        user_id = list_notes()
        topic = input("Please provide topic of the personal note to be archived: ")
        # Prepare URL to send put request
        put_url = "http://127.0.0.1:5007/send/" + user_id + "/" + topic
        # Send post request.
        r = requests.put(put_url, data = {})
        print(r.text)
        print()

    #----------------------------------------------------------------------------------------------

    elif code == "6":
        # List notes first.
        user_id = list_notes()
        topic = input("Please provide topic of the archived note to be recalled: ")
        # Prepare URL to send put request
        put_url = "http://127.0.0.1:5007/recall/" + user_id + "/" + topic
        # Send put request.
        r = requests.put(put_url, data = {})
        print(r.text)
        print()

    #-------------------------------------------------------------------------------------

    elif code == "7":
        # List notes first.
        user_id = list_notes()
        print("1: Delete note, 2: Delete archive.\n")
        sub_code = input("ENTER THE NUMBER OF THE OPERATION YOU WANT (Any other code will skip this operation). ")
        # Prepare URL differently based on sub code.
        if sub_code == "1":
            topic = input("Please provide topic of the note to be deleted: ")
            # Prepare URL for delete request.
            del_url = "http://127.0.0.1:5005/note/" + user_id + "/" + topic

        elif sub_code == "2":
            topic = input("Please provide topic of the archive to be deleted: ")
            # Prepare URL for delete request.
            del_url = "http://127.0.0.1:5005/archive/" + user_id + "/" + topic

        else:
            continue
        # send delete request.
        t = requests.delete(del_url)
        print(t.text)
        print()

    #---------------------------------------------------------------------------------------------------

    elif code == "8":
        list_notes()

    #--------------------------------------------------------------------------------------------------

    else:
        break

    #--------------------------------------------------------------------------------------------------
    #END
