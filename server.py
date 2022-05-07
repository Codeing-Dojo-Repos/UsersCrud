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
    

if __name__=="__main__":  
    app.run(debug=True)

