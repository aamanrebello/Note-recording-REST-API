import requests
import json

# TESTS THE POSTING API
entry1 = {
    "topic" : "test1",
    "content" : "I think I'm Ok!"
}
r = requests.post('http://127.0.0.1:5003/000088', json = entry1)
print(r.url)
print(r.text)
#entry2 = {
#    "topic" : "test2",
#    "content" : "B +ve",
#    "userID" : "000088"
#}
#r = requests.post('http://127.0.0.1:5003/add_note', json = entry2)
#print(r.url)
#print(r.text)
#entry3 = {
#    "topic" : "test3",
#    "content" : "how yeh doin bruh?",
#    "userID" : "565800"
#}
#r = requests.post('http://127.0.0.1:5003/add_note', json = entry3)
#print(r.url)
#print(r.text)

#entry4 = {
#    "topic" : "Loveyourself",
#    "content" : "You're Amazing!",
#    "userID" : "345678"
#}
#r = requests.post('http://127.0.0.1:5003/add_note', json = entry4)
#print(r.url)
#print(r.text)

#entry5 = {
#    "topic" : "test5",
#    "content" : "It be like that!!!!",
#    "userID" : "345678"
#}
#r = requests.post('http://127.0.0.1:5003/add_note', json = entry5)
#print(r.url)
#print(r.text)

# TESTS THE UPDATE API
new_entry_or_addition1 = {
    "topic" : "test1",
    "content" : " Take the dog for a walk, "
}
s = requests.put('http://127.0.0.1:5006/000088/prepend', json = new_entry_or_addition1)
print(s.url)
print(s.text)
#new_entry_or_addition2 = {
#    "topic" : "test1",
#    "content" : " Yea, I'm good. "
#}
#s = requests.put('http://127.0.0.1:5006/000088/append', json = new_entry_or_addition2)
#print(s.url)
#print(s.text)
#new_entry_or_addition3 = {
#    "topic" : "test3",
#    "content" : " I have no time.",
#    "userID" : "565800"
#}
#s = requests.put('http://127.0.0.1:5006/update/append', json = new_entry_or_addition3)
#print(s.url)
#print(s.text)
#new_entry_or_addition4 = {
#    "topic" : "test1",
#    "content" : " I hate them."
#}
#s = requests.put('http://127.0.0.1:5006/000088/rewrite', json = new_entry_or_addition4)
#print(s.url)
#print(s.text)
#new_entry_or_addition5 = {
#    "topic" : "test5",
#    "content" : " AWESOME!!!",
#    "userID" : "345678"
#}
#s = requests.put('http://127.0.0.1:5006/update/rewrite', json = new_entry_or_addition5)
#print(s.url)
#print(s.text)


#TESTS THE USER CREATION API.
new_user1 = {
    'username' : 'Za',
    'userID' : '000088'
}
t = requests.post('http://127.0.0.1:5004/', json = new_user1)
print(t.url)
print(t.text)

#new_user2 = {
#    'username' : 'Abu',
#    'userID' : '565800'
#}
#t = requests.post('http://127.0.0.1:5004/user/create', json = new_user2)
#print(t.url)
#print(t.text)

#new_user3 = {
#    'username' : 'Johnson',
#    'userID' : '345678'
#}
#t = requests.post('http://127.0.0.1:5004/user/create', json = new_user3)
#print(t.url)
#print(t.text)
