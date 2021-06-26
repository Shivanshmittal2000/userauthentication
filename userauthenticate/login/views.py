from django.http.response import HttpResponse, HttpResponseRedirect
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
            return show(request,requireduser[0].id)

            # newlist=[]
            # # print(users)
            # for i in users:
            #     newlist.append(i)
            # print(newlist)
            # print(newlist[0])
            # return render(request,'login/show.html',{'userdetail':requireduser[0], 'users':users})
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
        print(users)
        idfilter=User.objects.filter(id=id)
        print(idfilter[0])
        username=request.POST.get('username','')
        userfilter=User.objects.filter(username=username)
        print(len(userfilter))
        email=request.POST['email']
        emailfilter=User.objects.filter(email=email)
        print(len(emailfilter))
    return render(request,'login/show.html',{'users':users,'userdetail':idfilter[0],'ischange':True})

def deletedata(request,id):
    if request.method=="POST":
        users=User.objects.all()
        filterid=User.objects.get(id=id)
        print(filterid)
        filterid.address= ""
        print(filterid.address)
        filterid.save()
        print(filterid.address)
        # print(filterid[0])
        return HttpResponseRedirect('/')

def useredit(request,id):
    print('user',id)
    if request.method=="POST":
        users=User.objects.all()
        print(users)
        iffil=User.objects.filter(id=id)
        idfilter=User.objects.get(id=id)
        print(idfilter)
        username=request.POST.get('updatedinfo','')
        print(username)
        userfilter=User.objects.filter(username=username)
        print(len(userfilter))
        alreadyusername=idfilter.username
        if len(userfilter)>0:
            ischange=True
            if alreadyusername==username:
                ischange="username is same as previous one "
                # print("username is same as previous one ")
                return render(request,'login/show.html',{'users':users,'userdetail':iffil[0],'ischange':ischange})
    
            else :
                print("this name is taken by some other user please chose another username")
                ischange="this name is taken by some other user please chose another username"
                return render(request,'login/show.html',{'users':users,'userdetail':iffil[0],'ischange':ischange})
        else :
            idfilter.username=username
            idfilter.save()
            print(idfilter.username)
            return HttpResponseRedirect('/')

def emailedit(request,id):
    print('email',id)
    if request.method=="POST":
        users=User.objects.all()
        print(users)
        iffil=User.objects.filter(id=id)
        idfilter=User.objects.get(id=id)
        print(idfilter)
        email=request.POST.get('updatedinfo','')
        password=request.POST.get('updatedpassword','')
        passwordfilter=User.objects.filter(password=password)
        emailfilter=User.objects.filter(email=email)
        alreadypassword=idfilter.password
        alreadyemail=idfilter.email
        ischange=True
        if len(emailfilter)>0:
            if alreadyemail==email:
                if alreadypassword==password:
                    ischange ="This password is current password please write different password for change"
                elif password == "":
                    ischange = "Password cannot be blank"
                else :
                    idfilter.email=email
                    idfilter.password=password
                    idfilter.password2=password
                    idfilter.save()
                    print(idfilter.email)
                    print(idfilter.password)
                    return HttpResponseRedirect('/')
                
            else :
                ischange="Email already registered choose another email"
        else :
            if alreadypassword==password:
                ischange ="This password is already taken by you"
            elif password == "":
                ischange = "password cannot be blank"
            else :
                idfilter.email=email
                idfilter.password=password
                idfilter.password2=password
                idfilter.save()
                print(idfilter.email)
                print(idfilter.password)
                return HttpResponseRedirect('/')
        return render(request,'login/show.html',{'users':users,'userdetail':iffil[0],'ischange':ischange})

        





def addressedit(request,id):
    if request.method == "POST":
        print('address',id)
    if request.method=="POST":
        users=User.objects.all()
        print(users)
        idfilter=User.objects.get(id=id)
        print(idfilter)
        address=request.POST.get('updatedinfo','')
        idfilter.address=address
        idfilter.save()
        print(idfilter.address)
        return HttpResponseRedirect('/')
    