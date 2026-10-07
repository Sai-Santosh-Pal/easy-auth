from flask import Flask 

app = Flask(__name__)

@app.route('/')
def all_data():
    with open("data.txt", "r") as file:
        content = file.read()
        return eval(content)


if __name__ == "__main__":
    app.run(debug=True)