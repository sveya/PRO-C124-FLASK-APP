from flask import Flask,jsonify,request 
app=Flask(__name__)

contacts=[
    {
        "id":1,
        "name":"Anna",
        "contact":4326789051,
        "done":False
    },
    {
        "id":2,
        "name":"Richard",
        "contact":5427961038,
        "done":False
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    contact={
        "id": contacts[-1]["id"] + 1,
        "name": request.json["Name"],
        "contact": request.json.get("Contact", ""),
        "done": False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"Contact added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":contacts
    })
if (__name__=="__main__"):
    app.run(debug=True)
