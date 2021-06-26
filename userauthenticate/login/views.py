from django.shortcuts import render
from .models import User
import json
# Create your views here.
def login(request):
    users=[]
    if request.method=="POST":
        users=User.objects.all()
        email=request.POST['email']
        password=request.POST['password']
        requireduser=User.objects.filter(email=email)
        print(requireduser[0].password,password)
        if requireduser[0].password == password:
            newlist=[]
            # print(users)
            for i in users:
                newlist.append(i)
            print(newlist)
            print(newlist[0])
            return render(request,'login/show.html',{'userdetail':requireduser[0], 'users':newlist})
        # print(type(requireduser))
        # print(requireduser[0].id)
        # print(requireduser)
        # print(type(users))
        # print(users[0])
    return render(request,'login/index.html',{'users':users})

def signup(request):
    usermessage=''
    emailmessage=''
    passwordmessage=''
    if request.method == 'POST':
        users=User.objects.all()
        username=request.POST.get('username','')
        userfilter=User.objects.filter(username=username)
        print(len(userfilter))
        email=request.POST['email']
        emailfilter=User.objects.filter(email=email)
        print(len(emailfilter))
        password=request.POST['password']
        password2=request.POST['password2']
        address=request.POST['address']
        print(request)
        print(email,password,address)
        print(username)
        print(password2)
        if password == password2 and len(userfilter)==0 and len(emailfilter)==0:
            user=User(username=username,email=email,password=password,password2=password2,address=address)
            user.save()
        if password !=password2 :
            passwordmessage="Password and Confirm passwpord must be same"
        if len(userfilter)>0:
            usermessage='Username already Taken please use another username'
        if len(emailfilter)>0:
            emailmessage='Email already registered please use another email'
        return render(request,'login/signup.html',{'usermessage':usermessage,'emailmessage':emailmessage , "passwordmessage": passwordmessage})
    return render(request,'login/signup.html',{'usermessage':usermessage,'emailmessage':emailmessage , "passwordmessage": passwordmessage})
def show(request,id):
    print(id)
    if request.method=='POST':
        users=User.objects.all()
        newlist=[]
        print(users)
        for i in users:
            newlist.append(i)
    # print(newlist,hello)
    return render(request,'login/show.html',{'users':newlist})