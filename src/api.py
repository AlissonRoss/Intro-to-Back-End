from app import *

# This is where you will define all your API endpoints.
#endpoint is created by the programmer (aka me), and I can name it
#whatever I want, so it is now named /api/create-name



@app.route("/api/create-name", methods=["POST"])
def api_createName():
    print("You have called Create")
    name = request.form["create"]
    #Calls User Class from model.py
    user = User(name)
    db.session.add(user)
    db.session.commit()
    return {"Status":"Your good"}, 200

@app.route("/api/lookup-name", methods=["POST"])
def api_lookupName():
    print("You have called Lookup")
    name = request.form["lookup"]
    print("Inputted Name:", name)

    user = User.get_user(name)
    print("FOUND name:",user)
    return {"Status":"User lookup ran"}, 200

#HTML Web forms do not use DELETE method but can use POST and GET
@app.route("/api/delete-name", methods=["POST"])
def api_deleteName():
    name = request.form["delete"]
    user = User.get_user(name)
    db.session.delete(user)
    db.session.commit()
    return{"Status":"You have deleted a user"}, 200