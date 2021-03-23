from django.shortcuts import render
from .models import gallerySource
def home(request):
    images = gallerySource.objects.all()
    # info.tel ='+0937358326'
    # info.email = 'aman.getnet2@gmail.com'
    # info.phone ='+0937358326'
    # info.address ='Addis Ababa, Ethiopia'
    return render(request,'index.html',{'images':images})