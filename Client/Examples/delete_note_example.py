import requests
import json

# TESTS THE NOTE DELETING FUNCTIONALITY.
# The notes in new_note_example.py need to have been created.
# (5 tests in all)

# Deletes note 1 - See new_note_example.py
t = requests.delete('http://127.0.0.1:5005/note/000088/test1')
print(t.url)
print(t.text)

# Deletes note 2 - See new_note_example.py
t = requests.delete('http://127.0.0.1:5005/note/000088/test2')
print(t.url)
print(t.text)

# Deletes note 3 - See new_note_example.py
t = requests.delete('http://127.0.0.1:5005/note/000088/test3')
print(t.url)
print(t.text)

# Deletes note 4 - See new_note_example.py
t = requests.delete('http://127.0.0.1:5005/note/000088/Loveyourself')
print(t.url)
print(t.text)

# Deletes note 5 - See new_note_example.py
t = requests.delete('http://127.0.0.1:5005/note/000088/test5')
print(t.url)
print(t.text)

# END
