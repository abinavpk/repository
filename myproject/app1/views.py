from django.shortcuts import render, HttpResponse
from .models import Staff, product, Course, Language
from django.core.mail import send_mail,EmailMessage
from django.core.paginator import Paginator
def home(request):
    obj = Staff.objects.filter(email='arun@gmail.com')
    obj.update(email='aravind@gmail.com')
    obj = Staff.objects.all()
    obj1 = product.objects.all()
    obj2 = Course.objects.all()
    return render(request, 'html.html', {'Staff':obj, 'products':obj1, 'Courses':obj2})



def index(request):
    return render(request, 'html.html')
#1sender 1receiver
def email(request):
    send_mail('nothing',
              'hi',
              'abhinavpk55@gmail.com',
              ['anandhuparthan1818@gmail.com'],
              fail_silently=False)
    return render(request,'email.html')
#multiple receivers
def email1(request):
    EmailMessage('nothing',
              'hello',
              'abhinavpk55@gmail.com',
              to=['abhinavpk55@gmail.com','athenaerudition1@gmail.com']).send()
    return render(request,'email.html')
def compose(request):

        subject=request.POST.get('subject')
        mail=request.POST.get('email')
        message=request.POST.get('message')
        email= EmailMessage(subject,message,'abhinavpk55@gmail.com',to=[mail])
        email.content_subtype='html'
        file=open("Resume.pdf","r")
        email.attach("Resume.pdf",file.read(),'text/plain')
        email.send()
        return render(request,'composemail.html')

def myfunction(request):
    obj=Language.objects.values("description")
    return render(request,'page.html',{"pages":obj})

# all,filter,get,exclude,values - retrieve
