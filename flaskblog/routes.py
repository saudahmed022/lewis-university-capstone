from flaskblog import app
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = "Home")

@app.route("/about")
def about():
    return render_template('about.html', title ="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)