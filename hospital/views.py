from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
# from .forms import  ContactForm
from service.models import HealthCareStats
from news.models import news
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from appoinment.models import AppointmentRequest
from django.db import IntegrityError
from doctorlogin.models import Doctor
from .forms import UserProfileForm

# from .forms import AppointmentForm  

# from .forms import AppointmentForm


@login_required(login_url='login')

def index(request):
    return render(request, "index.html") 

def about(request):
    stats = HealthCareStats.objects.all().order_by('-category')[0:6]
    return render(request, "about.html", {'stats': stats})

def contact(request):
     
   
    return render(request, "contact.html")
def savedata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        doctor= request.POST.get('doctor')
        date= request.POST.get('date')
        data = AppointmentRequest(name=name, email=email,  phone_number=phone, doctor=doctor, date_and_time=date)
        data.save()
        
        
    return render(request, "contact.html")
    

def forgot(request):
    return render(request, "forgot.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        
        if user is not None:
           auth_login(request, user) 
           return redirect('index') 
        else:
            return render(request, "login.html")
     
    return render(request, "login.html")




def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
          
            My_user = User.objects.create_user(username=username, email=email, password=password)
            print(My_user)
            My_user.save()
            return redirect('login')
        except IntegrityError:
          
            return render(request, "singup.html", {'error_message': 'User with this username or email already exists.'})
        
    return render(request, "singup.html")



def logout(request):
    auth_logout(request)
    return redirect('login')

def comfirm(request):
    appoinmentdata = AppointmentRequest.objects.all()  
    data = {
        'appoinmentdata': appoinmentdata
    }
    return render(request, 'confirm.html', data)
    
    
def doctor(request):
    
 
        
        return render(request, "doctor.html")
     
def doccard(request):
    
    showdoctor = Doctor.objects.all()
    
    return render(request, "doccard.html",{'showdoctor':showdoctor})  


def savedoc(request): 
       if request.method =='POST':
        fullname = request.POST.get('fullname')
        email= request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        specialization = request.POST.get('specialization')
        qualification = request.POST.get('qualification')
                  
        hospital = request.POST.get('hospital')  
        contact_number = request.POST.get('contact_number')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        years_of_experience = request.POST.get('years_of_experience')
        profile_picture = request.POST.get('profile_picture')
        
        doctordata =Doctor( full_name=fullname, email=email, username=username, password=password,specialization=specialization, qualification=qualification, hospital=hospital ,contact_number=contact_number,date_of_birth=date_of_birth,gender=gender,address=address,years_of_experience=years_of_experience,profile_picture= profile_picture)
        doctordata.save()
        return render(request, "doctor.html")  
    
    
