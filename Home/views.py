from django.shortcuts import render, HttpResponse
from .models import Contact

# Create your views here.
def index(request):
      context = {
            "variable1":"harry is great",
            "variable2":"rohan is great"
      }
      return render(request, 'index.html')
     # return HttpResponse("this is home page") 

def about(request):
      return render(request, 'about.html')
      #return HttpResponse("this is about page") 
   
def services(request):
      return render(request, 'services.html') 
      #return HttpResponse("this is services page") 

def contact(request):
      print("Vicky testing the method",request.method)
      if request.method == "POST":
            print("Contact function if hit")
            name = request.POST.get('name')
            email = request.POST.get('email')
            passWord = request.POST.get('password')
            isCheck = request.POST.get('check')
            x = Contact.objects.create(name=name,email=email,password=passWord,checkbox=isCheck)
            x.save()
            return HttpResponse("Your form have been saved")
      else:
            return render(request, 'contact.html')
      # return render(request, 'contact.html')
      #return HttpResponse("this is contact page")  