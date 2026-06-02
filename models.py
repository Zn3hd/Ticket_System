from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(200), nullable=True)

    status_dict = { 
        0: 'Reported', 
        1: 'In Progress', 
        2: 'Resolved', 
        3: 'Unresolved' 
    }
    def status_string(self):
        return self.status_dict.get(self.status)
    
    def to_json(self):
        """
        Return the JSON serializable format
        """
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status_string(),
            'url': self.url
        }
