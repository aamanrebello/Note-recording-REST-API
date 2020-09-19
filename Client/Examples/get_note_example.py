import requests
import json

# TESTS THE NOTE LISTING FUNCTIONALITY THAT GETS A USER'S NOTES.
# Prerequisites: User accounts need to have been created - run new_user_example.py
# (3 examples in all)

# User 1 - see new_user_example.py
r = requests.get('http://127.0.0.1:5002/000088')
print(r.url)
print(r.text)

print()

# User 2 - see new_user_example.py
r = requests.get('http://127.0.0.1:5002/565800')
print(r.url)
print(r.text)

print()

# User 3 - see new_user_example.py
r = requests.get('http://127.0.0.1:5002/345678')
print(r.url)
print(r.text)

# END
