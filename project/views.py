from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def section1(request):
    return render(request, '이용정보.html')

def section2(request):
    return render(request, '대여소분포.html')

def section3(request):
    return render(request, '대여현황.html')

def section4(request):
    return render(request, '고장내역.html')

def section5(request):
    return render(request, '이용패턴.html')