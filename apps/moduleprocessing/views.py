from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from apps.moduleprocessing.models import Operator,ShipInfo,DangerMessages
from django.contrib import messages

import requests

# 로그인 페이지
def login(request):
    if request.method == 'POST':
        op_id:str = str(request.POST['ID'])
        op_pw:str = str(request.POST['PW'])
        try:
            info = Operator.objects.get(op_id=op_id) # 깂이 읽어와지면 아이디는 통과
            if check_password(op_pw,info.op_pw): # 비밀번호 체킹
                messages.success(request,"로그인 성공")
                shiplist = shiplist = ShipInfo.objects.values("shipname","sog","cog","connect","stage","gps")
                context = {"shiplist":shiplist}
                return render(request,'shiplist.html',context)
            else : 
                messages.warning(request,"비밀번호를 확인해주세요")
        except Operator.DoesNotExist:
            messages.error(request,"아이디를 확인해주세요")
    return render(request,'login.html')

# 선박 리스트 페이지
def listPage(request):
    shiplist = ShipInfo.objects.values("shipname","sog","cog","connect","stage","gps")
    context = {"shiplist":shiplist}
    return render(request,"shiplist.html",context)

# 메인 페이지
def mainPage(request):
    if request.method == "POST":
        # 관제할 선박 이름
        name = list(request.POST.keys())[1]
        # mysql에서 현재 상태 가져오기
        data = ShipInfo.objects.get(shipname=name)
        testvalue = [(1,'Brazil','2023-02-28','Boarded'),(2,'Brazil','2023-02-28','Boarded')]
        context={"pirate":testvalue,
                 "name":name,
                 "status": "정상" if data.connect else "연결끊킴",
                 "speed":data.sog,
                 "cog":data.cog,
                 "location":data.gps,
                 "mode":data.stage,
                 "ais":data.ais,
                 "ssas":data.ssas,
                 "sound":data.speaker,
                 "EB":data.eb}
    return render(request,"main.html",context)

# 수동 단계 변경
def changeLevel(request):
    # 기본 정보
    testvalue = [(1,'Brazil','2023-02-28','Boarded'),(2,'Brazil','2023-02-28','Boarded')]
    if request.method == "POST":
        # 선박정보 가져오기
        name = list(request.POST.keys())[1]
        data = ShipInfo.objects.get(shipname=name)
        if data.stage == 0: # 0단계
            data.stage = 1
            data.ssas = 0
            data.speaker = 0
            data.eb = 0
            data.ais = 0
            data.save()
        elif data.stage == 1: # 1단계
            data.stage = 2
            data.ssas = 1
            data.speaker = 1
            data.eb = 1
            data.ais = 0
            data.save()
        else : # 2단계
            data.stage = 0
            data.ssas = 0
            data.speaker = 0
            data.eb = 0
            data.ais = 1
            data.save()
    context={"pirate":testvalue,
                 "name":name,
                 "status": "정상" if data.connect else "연결끊킴",
                 "speed":data.sog,
                 "cog":data.cog,
                 "location":data.gps,
                 "mode":data.stage,
                 "ais":data.ais,
                 "ssas":data.ssas,
                 "sound":data.speaker,
                 "EB":data.eb}
    return render(request,"main.html",context)

# 해적 정보 갱신(크롤링 모듈 적용 필요)
def getPirateData(request):
    testvalue = [(1,'Brazil','2023-02-28','Boarded'),(2,'Brazil','2023-02-28','Boarded'),(3,'Brazil','2023-03-01','Boarded')]
    if request.method == 'POST':
        name = list(request.POST.keys())[1]
        data = ShipInfo.objects.get(shipname=name)
        context={'pirate':testvalue,
                 "name":name,
                 "status": "정상" if data.connect else "연결끊킴",
                 "speed":data.sog,
                 "cog":data.cog,
                 "location":data.gps,
                 "mode":data.stage,
                 "ais":data.ais,
                 "ssas":data.ssas,
                 "sound":data.speaker,
                 'EB':data.eb}
        return render(request, "main.html",context)

# 테러 대응 수동 제어
def manualControl(request):
    if request.method == "POST":
        sn,target =list(request.POST.keys())[1].split(" ")
        # 제어 신호(추후 구현)
        # DB 업데이트
        data = ShipInfo.objects.get(shipname=sn)
        if target == "ssas": # ON 시 수동 신고
            if data.ssas == True:
                data.ssas = 0
                data.save()
            else :
                data.ssas = 1
                """---------------------------"""
                """--post로 해양수산부에 수동 신고--"""
                # 선박의 식별 정보(선박 이름, IMO 번호 등)
                # 선박의 위치 정보(GPS 좌표, 위치명 등)
                # 긴급 상황의 종류(해적, 납치, 기타 긴급 상황 등)
                # 상황에 대한 추가 정보(상황 설명, 현재 상태 등)
                # sendData = {'name':sn,"location":data.gps,"kind":"pirate","etc":"위험"}
                emergencyMSG = DangerMessages(name=sn,location=data.gps,kind="해적 공격",etc="위험")
                emergencyMSG.save()
                """---------------------------"""
                data.save()
        elif target == "speaker":
            if data.speaker == True:
                data.speaker = 0
                data.save()
            else :
                data.speaker = 1
                data.save()
        elif target == "eb":
            if data.eb == True:
                data.eb = 0
                data.save()
            else :
                data.eb = 1
                data.save()
        elif target == "ais":
            if data.ais == True:
                data.ais = 0
                data.save()
            else :
                data.ais = 1
                data.save()
    testvalue = [(1,'Brazil','2023-02-28','Boarded'),(2,'Brazil','2023-02-28','Boarded'),(3,'Brazil','2023-03-01','Boarded')]
    context={'pirate':testvalue,
                 "name":sn,
                 "status": "정상" if data.connect else "연결끊킴",
                 "speed":data.sog,
                 "cog":data.cog,
                 "location":data.gps,
                 "mode":data.stage,
                 "ais":data.ais,
                 "ssas":data.ssas,
                 "sound":data.speaker,
                 'EB':data.eb}
    return render(request, "main.html",context)


def tmp(request):
    return render(request,"ssasserver.html",{})