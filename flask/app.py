from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/Log-in/index.html', methods=['GET'])
def index_login():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('index.html', message="LOGIN To AR Video Visualizer")


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            db.session.add(User(username=request.form['username'], password=request.form['password']))
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return render_template('index.html', message="User Already Exists")
    else:
        return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form['username']
        p = request.form['password']
        data = User.query.filter_by(username=u, password=p).first()
        if data is not None:
            session['logged_in'] = True
            return redirect(url_for('index'))
        return render_template('index.html', message="Incorrect Details")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.secret_key = "ThisIsNotASecret:p"
#     db.create_all()  # Uncomment this line to create tables
#     app.run(debug=True)


@app.route('/')
def index():
    return render_template('index_main.html')
@app.route('/index.html')
def index_html():
    return render_template('index_main.html')

@app.route('/about.html')
def about_html():
    return render_template('about_main.html')

@app.route('/about_main')
def about():
    return render_template('about_main.html')


@app.route('/service.html')
def service():
    return render_template('service_main.html')
@app.route('/service_main')
def service_html():
    return render_template('service_main.html')

@app.route('/why.html')
def why():
    return render_template('why_main.html')
@app.route('/why_main')
def why_html():
    return render_template('why_main.html')


if __name__ == '__main__':
    app.secret_key = "ThisIsNotASecret:p"
    
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)

