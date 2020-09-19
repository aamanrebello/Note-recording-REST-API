import requests
import json

# TESTS THE NOTE UPDATING FUNCTIONALITIES - PREPEND, APPEND AND REWRITE TEXT NOTES.
# Prequisite: The relevant text notes must have been created already - run new_notes_example.py
# (5 examples in all)

# ---------------------- PREPEND ---------------------------------------------------------
# Prepends note 1 - see new_notes_example.py
new_entry_or_addition1 = {
    "topic" : "test1",
    "content" : " Take the dog for a walk, "
}
s = requests.put('http://127.0.0.1:5006/000088/prepend', json = new_entry_or_addition1)
print(s.url)
print(s.text)

# Prepends note 4 - see new_notes_example.py
new_entry_or_addition2 = {
    "topic" : "Loveyourself",
    "content" : "You should know this."
}
s = requests.put('http://127.0.0.1:5006/000088/prepend', json = new_entry_or_addition2)
print(s.url)
print(s.text)


#---------------------- APPEND -----------------------------------------------------------

# Appends note 1 - see new_notes_example.py
new_entry_or_addition3 = {
    "topic" : "test1",
    "content" : " Yea, I'm good. "
}
s = requests.put('http://127.0.0.1:5006/000088/append', json = new_entry_or_addition3)
print(s.url)
print(s.text)

# Appends note 3 - see new_notes_example.py
new_entry_or_addition4 = {
    "topic" : "test3",
    "content" : " I have no time."
}
s = requests.put('http://127.0.0.1:5006/000088/append', json = new_entry_or_addition4)
print(s.url)
print(s.text)

#---------------------- REWRITE -----------------------------------------------------------

# Rewrites note 2 from scratch - see new_notes_example.py
new_entry_or_addition5 = {
    "topic" : "test2",
    "content" : " I hate them."
}
s = requests.put('http://127.0.0.1:5006/000088/rewrite', json = new_entry_or_addition5)
print(s.url)
print(s.text)

# Rewrites note 5 from scratch - see new_notes_example.py
new_entry_or_addition6 = {
    "topic" : "test5",
    "content" : " AWESOME!!!"
}
s = requests.put('http://127.0.0.1:5006/000088/rewrite', json = new_entry_or_addition6)
print(s.url)
print(s.text)

# END
