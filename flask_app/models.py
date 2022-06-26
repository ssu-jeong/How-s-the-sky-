from flask_app import db

class Materials(db.Model):
    __tablename__ = "materials"

    id = db.Column(db.Integer, primary_key=True)
    SO2 = db.Column(db.Float, nullable=False)
    NO2 = db.Column(db.Float, nullable=False)
    CO = db.Column(db.Float, nullable=False)
    O3 = db.Column(db.Integer, nullable=False)
    PM10 = db.Column(db.Integer, nullable=False)
    PM2_5 = db.Column(db.Integer, nullable=False)
    
    
