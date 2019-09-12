from app import db

class Qingdao_0(db.Model):

    loc = db.Column(db.String(128),index = True,nullable=True,primary_key=True) #青岛0~500 元 demo
class Qingdao_1(db.Model):
    loc = db.Column(db.String(128),index = True,nullable=True,primary_key=True) #青岛0~500 元 demo
class Qingdao_2(db.Model):
    loc = db.Column(db.String(128),index = True,nullable=True,primary_key=True) #青岛0~500 元 demo

    def __repr__(self):
        return '<Location %r >' % (self.QingDao_00)