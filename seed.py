import sys
sys.path.insert(0, '.')

from models import db, Ticket
from __init__ import create_app

app = create_app()

with app.app_context():
    tickets = [
        Ticket(name='Fix login bug', status=0, url='http://example.com/issue/1'),
        Ticket(name='Update homepage', status=1, url='http://example.com/issue/2'),
        Ticket(name='Database backup', status=2, url='http://example.com/issue/3'),
        Ticket(name='API timeout error', status=3, url='http://example.com/issue/4'),
    ]

    for ticket in tickets:
        db.session.add(ticket)

    db.session.commit()
    print("Test tickets added successfully!")