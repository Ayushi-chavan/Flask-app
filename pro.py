from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [{
	'id': 1,
	'Name': request.json['Name'],
	'Contact':request.json.get('Contact', ""),
	'done':False

}]


@app.route("/add-data", methods=["POST"])
def add_task():
	if not request.json:
		return jsonify({
			"status": "error",
			"message": "Please provide the data!"
		}, 400)
  contact = {
    'id': contacts[-1]['id'] + 1,
    'title': request.json['title'],
    'description': request.json.get('description', ""),
    'done': False
    }
  contacts.append(contact)
  return jsonify({
    "status":"success",
    "message": "Task added succesfully!"
    })

if(__name__=="__main__"):
    app.run(debug=True)