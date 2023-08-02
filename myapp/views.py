from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import profile_data, UserHistory
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . import flipkart, amazon
from datetime import datetime
from django.shortcuts import render
from django.core.mail import send_mail




def index(request):
    user=request.user
    return render(request, 'index.html',{'user':user})


def History(request):
    user=request.user
    user_history=UserHistory.objects.all().filter(Username=user)
    print(user_history)
    return render(request, 'History.html',{'history':user_history})


def About(request):
    return render(request, 'About.html')


def Contact(request):
    return render(request, 'Contact.html')

def Profile(request):
    us=request.user
    print(us)
    user=profile_data.objects.get(Email=us)
    print(user.Username)
    return render(request, 'Profile.html',{'user':user})
    
def Profile_edit(request):
    us=request.user
    user=profile_data.objects.get(Email=us)
    if request.method =='POST':
        name = request.POST['Name']
        email = request.POST['Email']
        age = request.POST['Age']
        phoneno = request.POST['Mobile']
        address = request.POST['Address']
        pass0 = request.POST['Password']
        pass1 = request.POST['CPassword']
        if pass0 ==pass1:
            user.Username=name
            user.Email=email
            user.Age=age
            user.Mobile=phoneno
            user.Address=address
            user.Password=pass0
            user.save()

            us.username=email
            us.email=email
            us.set_password(pass0)
            us.save()
            return render(request, 'Profile.html',{'user':user})
           
        else:
            messages.info(request, 'Password does not Match')
            return redirect('Profile_edit')
    return render(request, 'Profile.html',{'user':user})    


def Login(request):
    if request.method == 'POST':
       
        email = request.POST['email']
        pass0 = request.POST['password']
        user = authenticate( username=email, password=pass0)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('Login')
    return render(request, 'Login.html')


def Registration(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        age = request.POST['Age']
        phoneno = request.POST['Phone']
        address = request.POST['Address']
        pass0 = request.POST['Password']
        pass1 = request.POST['CPassword']

        if pass0 == pass1:
            if User.objects.filter(email=email).exists() and profile_data.objects.filter(Email=email).exists() :
                messages.info(request, 'Email already exits')
                return redirect('Registration')
            elif User.objects.filter(first_name=name).exists() and profile_data.objects.filter(Username=name).exists():
                messages.info(request, 'Username already exits')
                return redirect('Registration')
            else:
                user_profile = profile_data(Username=name, Email=email, Age=age, Mobile=phoneno, Address=address, Password=pass0)
                user_profile.save()
                user_User=User(username=email,first_name=name, email=email, password=pass0)
                user_User.set_password(pass0)
                user_User.save()
                return redirect('Login')
        else:
            messages.info(request, 'Password does not Match')
            return redirect('Registration')

    else:
        return render(request, 'Registration.html')


def Logout(request):
    logout(request)
    return render(request, 'index.html')


@login_required
def Search_product(request):
    if request.method =='POST':
        print("Serching Started.................................................................")
        
        product_name=request.POST['search']
        
        flipkart_list=flipkart.main(product_name)
        amazon_list=amazon.main(product_name)

        if flipkart_list is not None:
            flist=flipkart_list[0:6]
        if amazon_list is not None:
            alist=amazon_list[0:6]
       
        if len(flist)>0  or len(alist)>0 :
            user=request.user
            now = datetime.now()
            user_history = UserHistory(Email=user, Username=user, Product_name=product_name, DateTime=now)
            user_history.save() 

        print("Rending on website..............................................................................................")
        # print(flist)
        # print("******************")
        # print(alist)

        return render(request, 'index.html',{'flist':flist,'alist':alist })
        
        
    return redirect('/')


def buy_now(request):
    data = request.GET.get('data')  # Retrieve the 'data' parameter from the URL query string
    if data:
        link=data
        print(link)
        return HttpResponseRedirect(link)
    return redirect('/')

@login_required
def Check_Again(request):
    data = request.GET.get('data')  # Retrieve the 'data' parameter from the URL query string
    if data:
        name=data
        print(name)
        print("Serching Started.................................................................")
        
        product_name=name
        
        flipkart_list=flipkart.main(product_name)
        amazon_list=amazon.main(product_name)

        if flipkart_list is not None:
            flist=flipkart_list[0:6]
        if amazon_list is not None:
            alist=amazon_list[0:6]
       
        if len(flist)>0  or len(alist)>0 :
            user=request.user
            now = datetime.now()
            user_history = UserHistory(Email=user, Username=user, Product_name=product_name, DateTime=now)
            user_history.save() 

        print("******************")
        print(flist)
        print("******************")
        print(alist)

        return render(request, 'index.html',{'flist':flist,'alist':alist })
       
    return redirect('/')


def Contact_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send the email
        subject = f"Contact Form Submission from {name}"
        admin_email = 'pariendy.golu@gmail.com'  # Replace this with your admin's email address
        message_content = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        send_mail(subject=subject,message= message_content,from_email= admin_email,recipient_list=[email])

        # Optionally, you can add a success message to display on the page after the email is sent
        success_message = "Thank you for contacting us! We will get back to you soon."
        return render(request, 'Contact.html', {'success_message': success_message})

    return render(request, 'Contact.html')

