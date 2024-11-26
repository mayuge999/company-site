from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('お名前', validators=[DataRequired(), Length(max=100)])
    email = StringField('メールアドレス', validators=[DataRequired(), Email(), Length(max=120)])
    contact_type = SelectField('お問い合わせ種別', 
        choices=[
            ('general', '一般的なお問い合わせ'),
            ('service', 'サービスについて'),
            ('price', '料金について'),
            ('document', '資料請求'),
            ('other', 'その他')
        ],
        validators=[DataRequired()]
    )
    contact_method = RadioField('希望する連絡方法',
        choices=[
            ('email', 'メール'),
            ('phone', '電話'),
        ],
        validators=[DataRequired()]
    )
    contact_time = SelectField('希望する連絡時間帯',
        choices=[
            ('morning', '午前（9:00-12:00）'),
            ('afternoon', '午後（13:00-17:00）'),
            ('evening', '夕方（17:00-19:00）')
        ],
        validators=[DataRequired()]
    )
    category = SelectField('お問い合わせ内容のカテゴリ',
        choices=[
            ('curriculum', 'カリキュラムについて'),
            ('teacher', '講師について'),
            ('facility', '施設・設備について'),
            ('schedule', 'スケジュールについて'),
            ('other', 'その他')
        ],
        validators=[DataRequired()]
    )
    subject = StringField('件名', validators=[DataRequired(), Length(max=200)])
    message = TextAreaField('メッセージ', validators=[DataRequired()])
    submit = SubmitField('送信')


