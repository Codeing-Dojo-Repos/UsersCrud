from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)   

@app.route('/readAll')          
def hello_world():
    users = User.get_all()
    print(users)
    return render_template('read.html', users=users)

@app.route('/user/new')
def create():
    return render_template('create.html')

@app.route('/user/create', methods=['POST'])
def create_user():
    print(request.form)
    data={
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/readAll')

@app.route('/user/read/<int:id>')
def get_one_user(id):
    print('hit get_one_user route')
    data = { 'id': id }
    user = User.get_user_by_id(data)
    return render_template('oneUser.html', user = user[0])

@app.route('/user/edit/<int:id>')
def edit_one_user(id):
    print('hit edit_one_user')
    data = { 'id': id }
    user = User.get_user_by_id(data)
    return render_template('editUser.html', user = user[0])

@app.route('/user/edit2/<int:id>', methods=['POST'])
def edit_one_user2(id):
    print('hit edit_one_user2')
    data = {
        'id':id,
        'first_name':request.form['fname'],
        'last_name':request.form['lname'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect('/readAll')

@app.route('/user/delete/<int:id>')
def delete_user(id):
    print('hit delete user route')
    data = { 'id': id }
    User.delete_user(data)
    return redirect('/readAll')

if __name__=="__main__":  
    app.run(debug=True)

