from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from multiprocessing import connection
from .models import Employee

# Create your views here.
def GiveMeRagisterPage(request):
    return render(request,'register.html')

def Ragister(request):
    ename = request.GET['ename']
    email = request.GET['email']
    mobno = request.GET['mobno']
    salary=request.GET['salary']

    Employee.objects.create(ename = ename, email = email , mobno = mobno,salary=salary)
    return render(request,'login.html',{'message': 'user ragister successfully'})


def GiveMeLoginPage(request):
    return render(request,'login.html')



def Login(request):
    ename = request.GET['ename']
    email = request.GET['email']

    udata = Employee.objects.get(ename = ename)
    if (udata.email == email):
        return render(request,'home.html',{'message':'welcome '+ename})
    else :
        return render(request,'login.html',{'message':'invalid password'})
    




def GiveMeUserCurdPage(request):
    return render(request, "usercurd.html")


def AddUser(request):
    ename = request.GET['ename']
    email = request.GET['email']
    mobno = request.GET['mobno']
    salary=request.GET['salary']

    Employee.objects.create(ename = ename, email = email , mobno = mobno,salary=salary)
    return render(request,'usercurd.html',{'message': 'user ragister successfully'})


def ShowUser(request):
    ename = request.GET.get("ename")
    if ename:
        try:
            emp = Employee.objects.get(ename=ename)
            return HttpResponse(f"{emp.ename} | {emp.email} | {emp.mobno} | {emp.salary}")
        except Employee.DoesNotExist:
            return HttpResponse("Employee not found.")
    else:
        all_emp = Employee.objects.all()
        return render(request, "show_user.html", {"employees": all_emp})
    



def DeleteUser(request):
    ename = request.GET.get("ename")
    message = ""

    if ename:
        try:
            emp = Employee.objects.get(ename=ename)
            emp.delete()
            message = f"Employee {ename} deleted successfully!"
        except Employee.DoesNotExist:
            message = "Employee not found."
    else:
        message = "Please provide an ename to delete."

    return render(request, "usercurd.html", {"message": message})
   

def UpdateUser(request):
    ename = request.GET.get("ename")
    new_salary = request.GET.get("salary")
    message = ""

    if ename and new_salary:
        try:
            emp = Employee.objects.get(ename=ename)
            emp.salary = new_salary
            emp.save()
            message = f"Employee {ename} salary updated to {new_salary}"
        except Employee.DoesNotExist:
            message = "Employee not found."
    else:
        message = "Please provide ename and salary to update."

    return render(request, "usercurd.html", {"message": message})


def ShowAllEmployees(request):
    # Fetch all employees from the database
    all_employees = Employee.objects.all()
    
    # Pass the list to the template
    return render(request, "shoe_user.html", {"employees": all_employees})