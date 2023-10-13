from flask import Flask
from flask_mail import Message
from config import Configuration
from app import create_app, mail

app = create_app(Configuration)


@app.route('/')
def index():
    sender = 'practicesession3@gmail.com'
    recipients = ['practicesession3@gmail.com']
    msg = Message(subject="Test Send",
                  recipients=recipients,
                  sender=sender,
                  body='testing')

    mail.send(msg)


if __name__ == '__main__':
    app.run()
