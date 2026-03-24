from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from myapp.forms import Employeeform
from .models import Employee
from .tables import Employeetable
from django.db.models import Q
from django_tables2 import RequestConfig
# Create your views here.
def create(request):
    if request.method=='POST':
        form=Employeeform(request.POST)
        if form.is_valid():
             form.save()
             return redirect('view_employee')    
    else:
         form=Employeeform()
    return render(request,'create.html',{'form':form,'title':"ADD EMPLOYEE"})
def view_employee(request):
     employees=Employee.objects.all()
     query=request.GET.get('q')
     if query:
          if query.isdigit():
                
                employees=employees.filter(id=int(query))
          else:
                
                employees=employees.filter(name__icontains=query)
     table=Employeetable(employees)
     RequestConfig(request,paginate={"per_page":20}).configure(table)

     return render(request,'view.html',{'employeetable':table,'title':"view employees"})

def editemployee(request,id):
    employee=get_object_or_404(Employee,id=id)
    if request.method=='POST':
         form=Employeeform(request.POST,instance=employee)
         if form.is_valid():
              form.save()
              return redirect('view_employee')
    else:  
             
           form=Employeeform(instance=employee)
    return render(request,'edit.html',{'form':form,'title':'Editemployee'})
def deleteemployee(request,id):
     employee=get_object_or_404(Employee,id=id)
     if request.method=='POST':
           employee.delete()

           return redirect('view_employee')
     return render(request,'delete.html',{'employee':employee})