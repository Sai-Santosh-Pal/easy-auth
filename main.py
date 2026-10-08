from flask import Flask 

app = Flask(__name__)

@app.route('/')
def all_data():
    with open("data.txt", "r") as file:
        content = file.read()
        # if content != "":
        return eval(content)


@app.route('/auth/signup/<string:email>/<string:password>/<string:username><string:other_details>')
def signup(username, password, email, other_details={}):
    with open("data.txt", "r") as file:
        content = file.read()
        data = eval(content)
    data.append({"username": username, "password": password, "email": email, "other_details": other_details, "data": [{}]})
    # return data
    with open("data.txt", "w") as file:
        file.write(str(data))
    with open("data.txt", "r") as file:
        content = file.read()
        updated = eval(content)
    return updated
    

@app.route('/auth/remove/<string:email>')
def remove(email):
    with open("data.txt", "r") as file:
        content = file.read()
        data = eval(content)
    indexRemove = 0
    for i in data:
        if i['email'] == email:
            break
        else:
            indexRemove +=1
    try:
        data.pop(indexRemove)
    except Exception:
        pass
    with open("data.txt", "w") as file:
        file.write(str(data))
    with open("data.txt", "r") as file:
        content = file.read()
        removed = eval(content)
    return removed
    
@app.route('/auth/edit/<string:current_email>/<string:which>/<string:updated>')
def edit(current_email, which, updated):
    with open("data.txt", "r") as file:
        content = file.read()
        data = eval(content)
    index = 0
    for i in data:
        # print(current_email)
        # print(i['email'])
        # print(i['email'] == current_email)
        if i['email'] == current_email:
            i[which] = updated
            print(i)
            print(data)
            with open("data.txt", "w") as file:
                file.write(str(data))
            return all_data()
            break
        else:
            index +=1 
    return data

@app.route('/auth/login/<string:email>/<string:password>/')
def login(email, password):
    with open("data.txt", "r") as file:
        content = file.read()
        data = eval(content)
    for i in data:
        if i['email'] == email:
            if i['password'] == password:
                return [i['data'], 200]
            else:
                return [{'status': 'retry, passowrd is wrong'}, 404]
    else:
        return [{'status': 'user not found, sign up instead'}, 404]

@app.route('/auth/other_data/<string:email>/<string:toadd>/<string:val>')
def set_otherdata(email, toadd,val):
    content = all_data()
    for i in content:
        if i['email'] == email:
            data = i['other_details']
            data[toadd] = val
            with open("data.txt", "w") as file:
                file.write(str(content))
            with open("data.txt", "r") as file:
                content = file.read()
                added = eval(content)
            return added
    else:
        return [{'status': 'user not found, sign up instead'}, 404]


@app.route('/data/<string:email>')
def userdata(email):
    content = all_data()
    # print(content)
    for i in content:
        if i['email'] == email:
            return [i['data'], 200]
    else:
        return [{'status': 'user not found, sign up instead'}, 404]
    
@app.route('/data/set/<string:email>/<string:toadd>/<string:val>')
def set_userdata(email, toadd,val):
    content = all_data()
    for i in content:
        if i['email'] == email:
            data = i['data']
            data[0][toadd] = val
            with open("data.txt", "w") as file:
                file.write(str(content))
            with open("data.txt", "r") as file:
                content = file.read()
                added = eval(content)
            return added
    else:
        return [{'status': 'user not found, sign up instead'}, 404]


@app.route('/data/reset/<string:email>')
def reset_userdata(email):
    content = all_data()
    for i in content:
        if i['email'] == email:
            i['data'] = [{}]
            with open("data.txt", "w") as file:
                file.write(str(content))
            with open("data.txt", "r") as file:
                content = file.read()
                updated = eval(content)
            return updated
    else:
        return [{'status': 'user not found, sign up instead'}, 404]


if __name__ == "__main__":
    app.run(debug=True, port='5656', host='0.0.0.0')