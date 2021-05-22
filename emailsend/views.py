from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(name,message, email,['satadevlabsofficial@gmail.com'])
        return render(request,'index.html')
    else:
        return render(request,'index.html')
