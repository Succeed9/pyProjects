from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class status_studenta(db.Model):
    gruppa_guid = db.Column(db.Text)
    lichnost_guid = db.Column(db.Text)
    data_nachala = db.Column(db.Date)
    status_studenta_id = db.Column(db.Integer)
    status = db.Column(db.Text)
    tip_osnovaniya_vvoda = db.Column(db.Integer)
    prichina_vvoda_zapisi = db.Column(db.Text)
    prichina_otchisleniya_id = db.Column(db.Integer)
    prichina_otchisleniya = db.Column(db.Text)
    vid_otpuska_id = db.Column(db.Integer)
    vid_otpuska = db.Column(db.Text)
    tip_paragrapha_prikaza = db.Column(db.Integer)
    osnovanie_vvoda = db.Column(db.Text)
    kategoriya_obuchaemogo_id = db.Column(db.Integer)
    kategoriya_obuchaemogo = db.Column(db.Text)
