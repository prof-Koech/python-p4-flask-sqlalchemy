#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite://app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
