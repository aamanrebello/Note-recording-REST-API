import requests
import json

# TESTS THE FUNCTIONALITY TO ARCHIVE A USER'S NOTES.
# Prerequisites: The relevant notes need to have been created - run new_note_example.py
# (4 examples in all)

# Archive note 1 - see new_note_example.py
r = requests.put('http://127.0.0.1:5007/send/000088/test1', data = {})
print(r.url)
print(r.text)

# Archive note 2 - see new_note_example.py
r = requests.put('http://127.0.0.1:5007/send/000088/test2', data = {})
print(r.url)
print(r.text)

# Archive note 3 - see new_note_example.py
r = requests.put('http://127.0.0.1:5007/send/000088/test3', data = {})
print(r.url)
print(r.text)

# Archive note 5 - see new_note_example.py
r = requests.put('http://127.0.0.1:5007/send/000088/test5', data = {})
print(r.url)
print(r.text)

# END
