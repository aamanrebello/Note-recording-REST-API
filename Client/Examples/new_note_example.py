import requests
import json

# TESTS THE NOTE POSTING FUNCTIONALITY THAT CREATES A NEW NOTE.
# Prequisite - User with ID '000088' must have been previously created.
# (5 examples in all)

# Note 1
entry1 = {
    "topic" : "test1",
    "content" : "I think I'm Ok!"
}
r = requests.post('http://127.0.0.1:5003/000088', json = entry1)
print(r.url)
print(r.text)

# Note 2
entry2 = {
    "topic" : "test2",
    "content" : "B +ve",
}
r = requests.post('http://127.0.0.1:5003/000088', json = entry2)
print(r.url)
print(r.text)

# Note 3
entry3 = {
    "topic" : "test3",
    "content" : "how yeh doin bruh?",
}
r = requests.post('http://127.0.0.1:5003/000088', json = entry3)
print(r.url)
print(r.text)

# Note 4
entry4 = {
    "topic" : "Loveyourself",
    "content" : "You're Amazing!",
}
r = requests.post('http://127.0.0.1:5003/000088', json = entry4)
print(r.url)
print(r.text)

# Note 5
entry5 = {
    "topic" : "test5",
    "content" : "It be like that!!!!",
}
r = requests.post('http://127.0.0.1:5003/000088', json = entry5)
print(r.url)
print(r.text)


# END
