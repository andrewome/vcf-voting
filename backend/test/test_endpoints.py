import requests
import json

url = "http://localhost:8080"
session = requests.Session()

#POST to /login
print("POST incorrectly to /login")
data = {"username": "thisiswrong", "password": "obviously"}
r = session.post(url= url + "/login", json = data)
print(r.content, end="\n\n")

#POST to /login
print("POST correctly to /login")
data = {"username": "admin", "password": "password"}
r = session.post(url= url + "/login", json = data)
print(r.content, end="\n\n")

#POST maxVotes = -1 to /admin/ballots
print("POST maxVotes = -1 to /admin/ballots")
data = {
    "position": "Chairman",
    "names": ["Xiao Ming", "Xiao Bai", "Andy Tan"],
    "maxVotes": -1 }
r = session.post(url = url + "/admin/ballots", json = data)
print(r.content, end="\n\n")

#POST names = string to /admin/ballots
print("POST names = string to /admin/ballots")
data = {
    "position": "Chairman",
    "names": "Xiao Ming",
    "maxVotes": 1 }
r = session.post(url = url + "/admin/ballots", json = data)
print(r.content, end="\n\n")

#POST correctly to /admin/ballots
print("POST correctly to /admin/ballots")
data = {
    "position": "Chairman",
    "names": ["Xiao Ming", "Xiao Bai", "Andy Tan"],
    "maxVotes": 1 }
r = session.post(url = url + "/admin/ballots", json = data)
print(r.content, end="\n\n")

#GET from /admin/ballots/id
ballotId = json.loads(r.content)["id"]
print("GET from /admin/ballots/" + ballotId)
r = session.get(url = url + "/admin/ballots/" + ballotId)
print(r.content, end="\n\n")

#GET from /user/ballot
print("GET from /user/ballot")
r = session.get(url = url + "/user/ballot")
print(r.content, end="\n\n")

#POST a string to /user/ballot/id
ballotId = json.loads(r.content)["id"]
print("POST a string to /user/ballot/" + ballotId)
data = {"names": "I am a string!"}
r = session.post(url = url + "/user/ballot/" + ballotId, json = data)
print(r.content, end="\n\n")

#POST wrong names to /user/ballot/id
print("POST wrong names to /user/ballot/" + ballotId)
data = {"names": ["Definitely not inside"]}
r = session.post(url = url + "/user/ballot/" + ballotId, json = data)
print(r.content, end="\n\n")

#POST more names than allowed to /user/ballot/id
print("POST more names than allowed to /user/ballot/" + ballotId)
data = {"names": ["Xiao Ming", "Xiao Bai"]}
r = session.post(url = url + "/user/ballot/" + ballotId, json = data)
print(r.content, end="\n\n")

#POST within allowed limits to /user/ballot/id
print("POST within allowed limits to /user/ballot/" + ballotId)
data = {"names": ["Xiao Ming"]}
r = session.post(url = url + "/user/ballot/" + ballotId, json = data)
print(r.content, end="\n\n")

#POST within allowed limits to /user/ballot/id a 2nd time
print("POST within allowed limits to /user/ballot/{} a 2nd time".format(ballotId))
data = {"names": ["Xiao Ming"]}
r = session.post(url = url + "/user/ballot/" + ballotId, json = data)
print(r.content, end="\n\n")

#POST to /admin/ballots/id to close ballot
print("POST to /admin/ballots/{} to close ballot".format(ballotId))
data = {"id": ballotId}
r = session.post(url = url + "/admin/ballots/" + ballotId, json = data)
print(r.content, end="\n\n")

#GET from /user/ballot, should return with nothing as ballot has been closed
print("GET from /user/ballot, should return with nothing as ballot has been closed")
r = session.get(url = url + "/user/ballot")
print(r.content, end="\n\n")

#POST within allowed limits to /user/ballot/id, should fail because closed has been closed
print("POST within allowed limits to /user/ballot/{}, should fail because ballot has been closed".format(ballotId))
data = {"names": ["Xiao Ming"]}
r = session.post(url = url + "/user/ballot/" + ballotId, json = data)
print(r.content, end="\n\n")

print("Starting a new ballot...")
data = {
    "position": "Chairman",
    "names": ["Xiao Ming", "Xiao Bai", "Andy Tan"],
    "maxVotes": 1 }
r = session.post(url = url + "/admin/ballots", json = data)
ballotId = json.loads(r.content)["id"]

#GET from /admin/ballots, should have 2 in total
print("GET from /admin/ballots, should have 2 in total now")
r = session.get(url = url + "/admin/ballots")
print(r.content, end="\n\n")

#POST within allowed limits to /user/ballot/id
print("POST within allowed limits to /user/ballot/" + ballotId)
data = {"names": ["Xiao Ming"]}
r = session.post(url = url + "/user/ballot/" + ballotId, json = data)
print(r.content, end="\n\n")

#DELETE from /admin/ballots/id to invalidate vote
print("DELETE from /admin/ballots/{} to invalidate vote".format(ballotId))
r = session.delete(url = url + "/admin/ballots/" + ballotId)
print(r.content, end="\n\n")

#GET from /user/ballot, should return with nothing as ballot has been invalidated
print("GET from /user/ballot, should return with nothing as ballot has been invalidated")
r = session.get(url = url + "/user/ballot")
print(r.content, end="\n\n")

#POST within allowed limits to /user/ballot/id, should fail because closed has been invalidated
print("POST within allowed limits to /user/ballot/{}, should fail because ballot has been invalidated".format(ballotId))
data = {"names": ["Xiao Ming"]}
r = session.post(url = url + "/user/ballot/" + ballotId, json = data)
print(r.content, end="\n\n")