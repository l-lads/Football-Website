from . import app, db
from .models import Player

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
