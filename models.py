from . import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    times = db.Column(db.Integer)

    def __repr__(self):
        return f"<Player(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', times={self.times})>"
