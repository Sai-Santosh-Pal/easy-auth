from flask import Flask 

app = Flask(__name__)

@app.route('/')
def all_data():
    with open("data.txt", "r") as file:
        content = file.read()
        return eval(content)

@app.route('/add/<string:username>/<string:password>/<string:email>/<string:other_details>')
def add_data(username, password, email, other_details={}):
    with open("data.txt", "r") as file:
        content = file.read()
        data = eval(content)
    data.append({"username": username, "password": password, "email": email, "other_details": other_details})
    # return data
    with open("data.txt", "w") as file:
        file.write(str(data))
    with open("data.txt", "r") as file:
        content = file.read()
        updated = content
    return updated
    
if __name__ == "__main__":
    app.run(debug=True)