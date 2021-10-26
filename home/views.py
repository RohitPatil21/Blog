from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Contact
from django.contrib import messages

# messages.add_message(request, messages.INFO, 'Hello world.')


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<3:
            messages.error(request,"Please fill all the form fields correctly ")
            
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"Congrats! Your message has been sent successfully")
    return render(request, 'home/contact.html')



def about(request):
    return render(request, 'home/about.html')

