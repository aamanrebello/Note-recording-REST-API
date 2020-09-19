import requests
import json

# TESTS THE USER CREATION FUNCTIONALITY.
# No prerequisites.
# (3 tests in all)

# User 1
new_user1 = {
    'username' : 'Za',
    'userID' : '000088'
}
t = requests.post('http://127.0.0.1:5004/', json = new_user1)
print(t.url)
print(t.text)

# User 2
new_user2 = {
    'username' : 'Abu',
    'userID' : '565800'
}
t = requests.post('http://127.0.0.1:5004/', json = new_user2)
print(t.url)
print(t.text)

# User 3
new_user3 = {
    'username' : 'Johnson',
    'userID' : '345678'
}
t = requests.post('http://127.0.0.1:5004/', json = new_user3)
print(t.url)
print(t.text)


# END
