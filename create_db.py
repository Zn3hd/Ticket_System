import sys
sys.path.insert(0, '.')

from models import db, Ticket
from __init__ import create_app

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created successfully!")