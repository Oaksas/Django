from django.shortcuts import render
from .models import contactInfo
def home(request):
    info = contactInfo()
    info.tel ='+0937358326'
    info.email = 'aman.getnet2@gmail.com'
    info.phone ='+0937358326'
    info.address ='Addis Ababa, Ethiopia'
    return render(request,'index.html',{'info':info})