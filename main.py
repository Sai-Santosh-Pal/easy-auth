from flask import Flask 

app = Flask(__name__)

@app.route("/new_project/<project>")
def new_project(project):
    try:
        with open(project+".txt", "x") as file:
            file.write('[]')
            return "[]"
    except Exception as e:
        return f"Project already exists, rename it! - {e}"

@app.route('/<project>')
def all_data(project):
    try:
        with open(project+".txt", "r") as file:
            content = file.read()
            # if content != "":
            return eval(content)
    except Exception as e:
        return f"Project has not been created yet! - {e}"

@app.route('/<project>/auth/signup/<string:email>/<string:password>/<string:username><string:other_details>')
def signup(project, username, password, email, other_details={}):
    data = all_data(project)
    data.append({"username": username, "password": password, "email": email, "other_details": other_details, "data": [{}]})
    # return data
    with open("data.txt", "w") as file:
        file.write(str(data))
    with open("data.txt", "r") as file:
        content = file.read()
        updated = eval(content)
    return updated
    
@app.route('/<project>/auth/remove/<string:email>')
def remove(email):
    data = all_data(project)

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
    
@app.route('/<project>/auth/edit/<string:current_email>/<string:which>/<string:updated>')
def edit(project, current_email, which, updated):
    data = all_data(project)

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

@app.route('/<project>/auth/login/<string:email>/<string:password>/')
def login(email, password, project):
    data = all_data(project)
    for i in data:
        if i['email'] == email:
            if i['password'] == password:
                return [i['data'], 200]
            else:
                return [{'status': 'retry, passowrd is wrong'}, 404]
    else:
        return [{'status': 'user not found, sign up instead'}, 404]

@app.route('/<project>/auth/other_data/<string:email>/<string:toadd>/<string:val>')
def set_otherdata(project,email, toadd,val):
    content = all_data(project)
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


@app.route('/<project>/data/<string:email>')
def userdata(email, project):
    content = all_data(project)
    # print(content)
    for i in content:
        if i['email'] == email:
            return [i['data'], 200]
    else:
        return [{'status': 'user not found, sign up instead'}, 404]
    
@app.route('/<project>/data/set/<string:email>/<string:toadd>/<string:val>')
def set_userdata(email, project,toadd,val):
    content = all_data(project)
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


@app.route('/<project>/data/reset/<string:email>')
def reset_userdata(email, password):
    content = all_data(project)
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