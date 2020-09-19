import requests
import json

# TESTS THE FUNCTIONALITIES TO RECALL/DELETE USER ARCHIVES.
# Prerequisites: The relevant archives need to have been created - run archive_note_example.py
# (4 examples in all)

# Recall archive of note 1 - see new_note_example.py
r = requests.put('http://127.0.0.1:5007/recall/000088/test1')
print(r.url)
print(r.text)

# Recall archive of note 2 - see new_note_example.py
r = requests.put('http://127.0.0.1:5007/recall/000088/test2')
print(r.url)
print(r.text)

# Delete archive of note 3 - see new_note_example.py
r = requests.delete('http://127.0.0.1:5005/archive/000088/test3')
print(r.url)
print(r.text)

# Delete archive of note 5 - see new_note_example.py
r = requests.delete('http://127.0.0.1:5005/archive/000088/test5')
print(r.url)
print(r.text)

# END
