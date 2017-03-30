from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#---------------------------------------------------------------------#


class Path(db.Model):
    """Map marking off already travelled paths"""

    __tablename__ = "paths"

    path_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    destination = db.Column(db.String(30), nullable=False)
    start_lat = db.Column(db.String(15), nullable=False)
    start_long = db.Column(db.String(15), nullable=False)
    end_lat = db.Column(db.String(15), nullable=False)
    end_long = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return "<{} Destination: {}>".format(self.path_id, self.destination)


#---------------------------------------------------------------------#

def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sfmapping'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print "Connected to DB."
