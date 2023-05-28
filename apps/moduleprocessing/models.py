from django.db import models
from django.contrib.auth.hashers import make_password

class Operator(models.Model):
    op_id = models.CharField(max_length=100)
    op_pw = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.op_pw = make_password(raw_password)

class ShipInfo(models.Model):
    # 선박명(기본 키)
    shipname = models.CharField(max_length=100,primary_key=True)
    # 속도(knot)
    sog = models.FloatField(max_length=100)
    # 방향(북쪽을 0도, 동쪽을 90도, 남쪽을 180도, 서쪽을 270도)
    cog = models.FloatField(max_length=100)
    # 연결상태
    connect = models.BooleanField(max_length=100)
    # 단계
    stage = models.IntegerField()
    # 해역
    gps = models.CharField(max_length=100)
    # ais
    ais = models.BooleanField(max_length=100)
    # ssas
    ssas = models.BooleanField(max_length=100)
    # 기적장치
    speaker = models.BooleanField(max_length=100)
    # Electroblow
    eb = models.BooleanField(max_length=100)
from datetime import datetime
class DangerMessages(models.Model):
    time = models.DateTimeField(default=datetime.now(),max_length=100)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    etc = models.CharField(max_length=100)