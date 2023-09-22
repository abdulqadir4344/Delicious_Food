from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Book_Table

# Create your views here.


def home(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            number = request.POST.get('number')
            email = request.POST.get('email')
            date = request.POST.get('date')
            person = request.POST.get('person')

            if name !='' and number !='' and email !='' and date !='' and person !='':
                data = Book_Table(Name=name,Number=number,Email=email,Date=date,Person=person)
                data.save()
        return render(request,'home.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def book_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        date = request.POST.get('date')
        person = request.POST.get('person')

        if name !='' and number !='' and email !='' and date !='' and person !='':
            data = Book_Table(Name=name,Number=number,Email=email,Date=date,Person=person)
            data.save()


    return render(request,'book_table.html')

def order(request):
    return render(request,'order.html')






