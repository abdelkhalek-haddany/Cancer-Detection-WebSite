from django.shortcuts import render
from joblib import load
model = load('./savedModels/model.joblib')

# Create your views here.
def index(request):
    return render(request, 'Form/home.html')

def login(request):
    return render(request, 'Form/login.html')

def register(request):
    return render(request, 'Form/register.html')

def result(request):
    att1 = request.GET['att1']
    att2 = request.GET['att2']
    att3 = request.GET['att3']
    att4 = request.GET['att4']
    att5 = request.GET['att5']
    att6 = request.GET['att6']
    att7 = request.GET['att7']
    att8 = request.GET['att8']
    att9 = request.GET['att9']
    att10 = request.GET['att10']
    att11 = request.GET['att11']
    att12 = request.GET['att12']
    att13 = request.GET['att13']
    att14 = request.GET['att14']
    att15 = request.GET['att15']
    att16 = request.GET['att16']
    att17 = request.GET['att17']
    att18 = request.GET['att18']
    att19 = request.GET['att19']
    att20 = request.GET['att20']
    att21 = request.GET['att21']
    att22 = request.GET['att22']
    att23 = request.GET['att23']
    
    x=[12,att1,att2,att3,att4,att5,att6,att7,att8,att9,att10,att11,att12,att13,att14,att15,att16,att17,att18,att19,att20,att21, att22,att23]
    
    result =  model.predict([x])
    if result == 0:
       result = 'Low'
    elif result == 1:
        result = 'Medium'
    else:
        result = 'High'

    return render(request, 'Form/result.html', {'result': result})