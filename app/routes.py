from flask import render_template, redirect, url_for, flash, request, jsonify
from app import db
from flask import current_app as app
from app.models import User, JournalEntry, Message
from app.forms import SettingsForm, LoginForm, RegisterForm, JournalForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

@app.before_request
def check_login_required():
    if request.endpoint in ['messages', 'journal', 'settings', 'grounding', 'cognitive', 'safe_space', 'crisis_plan'] and not current_user.is_authenticated:
        if request.is_xhr:  # If the request is an AJAX request, return a specific response
            return jsonify({'login_required': True}), 401
        else:
            flash('You need to log in to access this page.', 'warning')
            return redirect(url_for('dashboard'))

@app.route('/')
def dashboard():
    login_form = LoginForm()  # Initialize the login form
    register_form = RegisterForm()  # Initialize the register form
    return render_template('dashboard.html', login_form=login_form, register_form=register_form)

@app.route('/reality_testing')
@login_required
def reality_testing():
    return render_template('reality_testing.html')

@app.route('/grounding')
@login_required
def grounding():
    return render_template('grounding.html')

@app.route('/cognitive')
@login_required
def cognitive():
    return render_template('cognitive.html')

@app.route('/safe_space')
@login_required
def safe_space():
    return render_template('safe_space.html')

@app.route('/messages')
@login_required
def messages():
    user_messages = Message.query.filter_by(user_id=current_user.id).all()
    return render_template('messages.html', messages=user_messages)

@app.route('/crisis_plan')
@login_required
def crisis_plan():
    return render_template('crisis_plan.html')

@app.route('/journal', methods=['GET', 'POST'])
@login_required
def journal():
    form = JournalForm()
    if form.validate_on_submit():
        new_entry = JournalEntry(content=form.content.data, user_id=current_user.id)
        db.session.add(new_entry)
        db.session.commit()
        flash('Journal entry added.', 'success')
        return redirect(url_for('journal'))
    
    user_entries = JournalEntry.query.filter_by(user_id=current_user.id).order_by(JournalEntry.timestamp.desc()).all()
    return render_template('journal.html', form=form, entries=user_entries)

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = SettingsForm(obj=current_user)
    if form.validate_on_submit():
        current_user.notifications = form.notifications.data
        current_user.theme = form.theme.data
        db.session.commit()
        flash('Your settings have been updated.', 'success')
        return redirect(url_for('settings'))
    return render_template('settings.html', form=form)

@app.route('/set_theme', methods=['POST'])
@login_required
def set_theme():
    data = request.get_json()
    theme = data.get('theme')
    if theme in ['light', 'dark']:
        current_user.theme = theme
        db.session.commit()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'}), 400

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()  # Initialize the form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    
    return render_template('login.html', form=form)  # Pass the form to the template

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You can now log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('An account with this email already exists.', 'danger')
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('dashboard'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', login_form=LoginForm(), register_form=RegisterForm()), 404
