from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        passwordConfirm = request.POST['confirmPassword']

        if(password == passwordConfirm):
            user = User.objects.create_user(username= username, first_name=firstName,last_name=lastName,email=email,password=password)
            user.save()
            print('userCreated')
            return redirect('/')
        else:
            print('password not much')
    return render(request,'register.html')