from app import db

class Location(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    QingDao_00 = db.Column(db.String(128),index = True,nullable=True) #青岛0~500 元 demo

    def __repr__(self):
        return '<Location %r >' % (self.QingDao_00)