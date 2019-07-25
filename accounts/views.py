from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):

    if(request.method == 'POST'):

        username = request.POST.get('username',False)
        email = request.POST.get('email',False)
        pword = request.POST.get('pword',False)
        pword2 = request.POST.get('pword2',False)

        user = User.objects.create_user(username=username, password=pword, email=email)
        user.save();
        return redirect('/')

    else:

        return render(request,'register.html')
