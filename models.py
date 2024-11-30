from datetime import datetime
from extensions import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_url = db.Column(db.String(200))

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    file_url = db.Column(db.String(200))
    category = db.Column(db.String(100))
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200))
    parent_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'))
    position = db.Column(db.Integer)
    menu_type = db.Column(db.String(50))  # 'main', 'side', 'footer'
    
    children = db.relationship('MenuItem', backref=db.backref('parent', remote_side=[id]))
