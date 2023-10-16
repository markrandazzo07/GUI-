# What port do you use. 

from flask import Flask, render_template, request, url_for, flash, redirect
import database


app = Flask(__name__)
app.secret_key = 'Random-Key:1122'


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = database.hash_passwords(request.form['password'])

        if database.create_user(first_name, last_name, username, password):
            flash('Account successfully created!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Account already exists!', 'Error')
            return redirect('register.html'), 400

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = database.get_user(username)

        if user == None:
            flash('Invalid username!', 'Error')
            return render_template('login.html'), 400

        if user and not database.check_password(password, user[4]):
            flash('Invalid password!', 'Error')
            return render_template('login.html'), 400

        flash('Logged in successfully!', 'success')

    return render_template('login.html')

@app.route('/api/move', methods=['POST'])
def move():
    direction = request.json.get('direction')

    # TODO: Implement action for each direction
    if direction == 'FORWARD':
        pass
    elif direction == 'BACKWARD':
        pass
    elif direction == 'RIGHT':
        pass
    elif direction == 'LEFT':
        pass
    elif direction == 'STOP':
        pass

    return "", 200  # Return an empty response with a status code of 200


if __name__ == '__main__':
    database.setup_database()
    app.run(host='0.0.0.0', port=8080)
    #app.run(debug=True)  # This will start the app in debug mode