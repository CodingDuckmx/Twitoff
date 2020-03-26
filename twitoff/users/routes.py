from flask import Blueprint, render_template, url_for, flash, redirect
from twitoff.users.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f"You've have been logged in!", 'success')
            return redirect(url_for('main.home'))
        else:
            flash(f'Login Unsuccesful. Please check username and password', 'danger')         
    return render_template('login.html', title='Login', form=form)