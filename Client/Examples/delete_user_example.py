import requests
import json

# TESTS THE USER DELETING FUNCTIONALITY.
# No prerequisites.
# (3 tests in all)

# Deletes User 1 - See new_user_example.py
t = requests.delete('http://127.0.0.1:5004/000088')
print(t.url)
print(t.text)

# Deletes User 2 - See new_user_example.py
t = requests.delete('http://127.0.0.1:5004/565800')
print(t.url)
print(t.text)

# Deletes User 3 - See new_user_example.py
t = requests.delete('http://127.0.0.1:5004/345678')
print(t.url)
print(t.text)

# END
