#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Description: 
    ~~~~~~
    @Author  : pake
    @Time    : 2021/7/29 16:55
"""

from flask import Flask
from flask_mail import Message, Mail

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = '127.0.0.1',
    MAIL_PORT = 10001,
)


@app.route("/")
def hello_world():
    msg = Message("Hello",
                  sender="from@example.com",
                  recipients=["to@example.com"],
                  mail_options=["X-OPTION\nBad smtp-client command1","X-OPTION2\nbad smtp-command2"])
    mail = Mail(app)
    mail.send(msg)

if __name__=='__main__':
    app.run(debug=True)