from flask import render_template, url_for, flash, redirect
from flask_blog.forms import LoginForm, RegistrationForm
from flask_blog import app
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for("home"))
    return render_template('register.html', title="register", form=form)


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "a@a.com" and form.password.data == 'password':
            flash('you have been logged in', 'success')
            return redirect(url_for("home"))
        else:
            flash("Login unsuceesful", 'danger')



    return render_template('login.html', title="login", form=form)
