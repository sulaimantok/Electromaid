from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self,password):
        return check_password_hash(self.password, password)

class Post(db.Document):
    judul = db.StringField(required=True)
    gambar = db.StringField(required=True)
    tanggal = db.DateTimeField(default=datetime.utcnow)
    berita = db.StringField(required=True)
    url = db.StringField(required=True)
    penulis = db.StringField(required=True)

class Sensor(db.Document):
    master_id = db.StringField(required=True)
    watt_total = db.StringField(required=True)
    device = db.ListField()
    date = db.DateTimeField(default=datetime.today)

class Notifikasi(db.Document):
    title = db.StringField(required=True)
    notifikasi = db.StringField(required=True)
    waktu = db.StringField(required=True)
