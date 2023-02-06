from django.shortcuts import render,redirect
from .models import Students
from .form import StudentsForm
from django.contrib import messages

def list_notes(request):
    students=Students.objects.filter(name__contains=request.GET.get('search',"")).order_by('curse')
    context={"students":students}
    return render(request, "notes.html",context)

def view(request,id):
    student=Students.objects.get(id=id)
    context={"student":student}
    return render(request, "detail.html",context)    

def edit(request,id):
    student=Students.objects.get(id=id)
    if (request.method=="GET"):        
        form=StudentsForm(instance=student)
        context={"form":form,
        "id":id}
        return render(request, "edit.html",context)
    if (request.method=="POST"):
        form=StudentsForm(request.POST,instance=student) 
        if form.is_valid():
            form.save()
        context={"form":form,
        "id":id}            
        messages.success(request, 'Student updated.')
        return render(request, "edit.html",context)
def create(request):
    if request.method=="GET": 
        form=StudentsForm()
        context={"form":form}
        return render(request,"create.html",context)
    if request.method=="POST":
        form=StudentsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("notes")    

def delete(request,id):
    student=Students.objects.get(id=id)
    student.delete()    
    return redirect("notes")