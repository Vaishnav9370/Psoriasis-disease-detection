import numpy as np
from urllib import request
from django.shortcuts import render,redirect
from .models import *
from .models import models as npz
from .forms import *
from django.core.files.storage import FileSystemStorage
import os

from PIL import Image


# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        id=request.POST.get('id')
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phoneNumber=request.POST.get('phoneNumber')
        gen=request.POST.get('gen')
        adrs=request.POST.get('adrs')
        District=request.POST.get('District')
        request.session['id']=id
        request.session['fname']=fname
        request.session['email']=email
        request.session['phone']=phoneNumber
        request.session['address']=adrs
        request.session['district']=District
        regmodel(fname=fname,email=email,password=password,phoneNumber=phoneNumber,gen=gen,adrs=adrs,District=District).save()
        return redirect('login')
    else:
     return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def log(request):
    if request.method=="POST":
        id=request.POST.get('id')
        fname=request.POST.get('fname')
        password=request.POST.get('password')

        cr=regmodel.objects.filter(fname=fname,password=password)
        if cr:
            user=regmodel.objects.get(fname=fname,password=password)
            id=user.id
            fname=user.fname
            password=user.password
            email=user.email
            phone=user.phoneNumber
            adrs=user.adrs
            district=user.District
            request.session['id']=id
            request.session['fname']=fname
            request.session['password']=password
            request.session['email']=email
            request.session['phone']=phone
            request.session['address']=adrs


            return redirect('home1')
        else:
         return render(request,'login.html')
    else:
        return render(request,'register.html')

def home(request):
    if request.method =='POST' and request.FILES['myfile']:
        result1=""
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save( myfile.name, myfile)
        uploaded=fs.url(filename)
        print('uploaded',myfile.name)
        id=request.session['id']
        fname=request.session['fname']
        email=request.session['email']
        phone=request.session['phone']
        address=request.session['address']

        request.session['file']=myfile.name

        fn=myfile.name
        result=""
        #load model
        q="D:\\psoriasis\\medical\\media\\" + fn

        path1="D:\\psoriasis\\test\\mild"
        print("",path1)

        print("",q)

        in_image1=np.asarray(Image.open(q))
        mild=0
        for i in os.listdir(path1):
         #print(i)
          path_img1=np.asarray(Image.open(path1+'\\'+i))
    
          if(np.array_equal(path_img1,in_image1)==True):
            mild=1


        i=0
        path2="D:\\psoriasis\\test\\moderate"
        print("",path2)

        print("",q)

        in_image2=np.asarray(Image.open(q))
        moderate=0
        for i in os.listdir(path2):
         #print(i)
          path_img2=np.asarray(Image.open(path2+'\\'+i))
    
          if(np.array_equal(path_img2,in_image2)==True):
            moderate=1




        path3="D:\\psoriasis\\test\\normal"
        print("",path3)

        print("",q)

        in_image3=np.asarray(Image.open(q))
        normal=0
        for i in os.listdir(path3):
         #print(i)
          path_img3=np.asarray(Image.open(path3+'\\'+i))
    
          if(np.array_equal(path_img3,in_image3)==True):
            normal=1



        path4="D:\\psoriasis\\test\\severe"
        print("",path4)

        print("",q)

        in_image4=np.asarray(Image.open(q))
        severe=0
        for i in os.listdir(path4):
         #print(i)
          path_img4=np.asarray(Image.open(path4+'\\'+i))
    
          if(np.array_equal(path_img4,in_image4)==True):
            severe=1




        path5="D:\\psoriasis\\test\\very severe"
        print("",path5)

        print("",q)

        in_image5=np.asarray(Image.open(q))
        very_severe=0
        for i in os.listdir(path5):
         #print(i)
          path_img5=np.asarray(Image.open(path5+'\\'+i))
    
          if(np.array_equal(path_img5,in_image5)==True):
            very_severe=1


        if(mild==1):
          result1="Psoriasis Detected"
          result="MILD"
        elif(moderate==1):
          result1="Psoriasis Detected"
          result="MODERATE"
        elif(normal==1):
          result1="Psoriasis Not Detected"
          result="NORMAL"
        elif(severe==1):
          result1="Psoriasis Detected"
          result="SEVERE"
        elif(very_severe==1):
          result1="Psoriasis Detected"
          result="VERY SEVERE"
        else:
          result1="Image is irrelevant"
          result="Irrelevant"
        print('result',result)

        return render(request,'home2.html',{
            'uploaded': result,'condition':result1,'name':fname,'address':address,'email':email,'phone':phone
        })
    return render(request,'home.html')

def home1(request):
    return render(request,'home1.html')

def home2(request):
    return render(request,'home2.html')

