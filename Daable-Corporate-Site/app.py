from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_mail import Mail, Message
import os

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = ('Daable', os.environ.get('MAIL_USERNAME'))

db = SQLAlchemy(model_class=Base)
db.init_app(app)

mail = Mail(app)

from models import Contact, Page
from forms import ContactForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            name=form.name.data,
            email=form.email.data,
            contact_type=form.contact_type.data,
            contact_method=form.contact_method.data,
            contact_time=form.contact_time.data,
            category=form.category.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(contact)
        db.session.commit()

        msg = Message('新しいお問い合わせ',
                     sender=app.config['MAIL_DEFAULT_SENDER'],
                     recipients=['dazhongcun984@gmail.com'])
        msg.body = f'''
        名前: {form.name.data}
        メール: {form.email.data}
        お問い合わせ種別: {dict(form.contact_type.choices).get(form.contact_type.data)}
        希望する連絡方法: {dict(form.contact_method.choices).get(form.contact_method.data)}
        希望する連絡時間帯: {dict(form.contact_time.choices).get(form.contact_time.data)}
        カテゴリ: {dict(form.category.choices).get(form.category.data)}
        件名: {form.subject.data}
        メッセージ: {form.message.data}
        '''
        mail.send(msg)
        
        flash('お問い合わせありがとうございます。内容を確認次第、ご連絡させていただきます。')
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)

# Plan pages routes
@app.route('/basic-plan')
def basic_plan():
    return render_template('plans/basic-plan.html')

@app.route('/standard-plan')
def standard_plan():
    return render_template('plans/standard-plan.html')

@app.route('/premium-plan')
def premium_plan():
    return render_template('plans/premium-plan.html')

# 採用情報ページのルート
@app.route('/recruit')
def recruit():
    return render_template('recruit/index.html')

@app.route('/recruit/new-graduate')
def recruit_new_graduate():
    return render_template('recruit/new-graduate.html')

@app.route('/recruit/career')
def recruit_career():
    return render_template('recruit/career.html')

@app.route('/recruit/intern')
def recruit_intern():
    return render_template('recruit/intern.html')


@app.route('/entry', methods=['POST'])
def handle_entry():
    # フォームデータの取得
    entry_data = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'position': request.form.get('position'),
        'motivation': request.form.get('motivation')
    }
    
    # メール送信
    msg = Message('新規エントリー',
                 sender=app.config['MAIL_DEFAULT_SENDER'],
                 recipients=['dazhongcun984@gmail.com'])
    msg.body = f'''
    名前: {entry_data['name']}
    メール: {entry_data['email']}
    志望職種: {entry_data['position']}
    志望動機: {entry_data['motivation']}
    '''
    mail.send(msg)
    
    flash('エントリーを受け付けました。内容を確認次第、ご連絡させていただきます。')
    return redirect(url_for('recruit'))
with app.app_context():
    db.create_all()