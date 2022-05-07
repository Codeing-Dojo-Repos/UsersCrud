from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)   

@app.route('/read')          
def hello_world():
    users = User.get_all()
    print(users)
    return render_template('read.html', users=users)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    print(request.form)
    data={
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/read')

@app.route('/oneUser/<int:id>')
def get_one_user(id):
    print('hit get_one_user route')
    data = { 'id': id }
    user = User.get_user_by_id(data)
    return render_template('oneUser.html', user = user[0])

@app.route('/editUser/<int:id>')
def edit_one_user(id):
    print('hit edit_one_user')
    data = { 'id': id }
    user = User.get_user_by_id(data)
    return render_template('editUser.html', user = user[0])

@app.route('/editUser2/<int:id>', methods=['POST'])
def edit_one_user2(id):
    print('hit edit_one_user2')
    data = {
        'id':id,
        'first_name':request.form['fname'],
        'last_name':request.form['lname'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect('/read')

if __name__=="__main__":  
    app.run(debug=True)

