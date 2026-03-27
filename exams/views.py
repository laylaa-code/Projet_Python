from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam
from django.contrib import messages

def exams_list(request):
    exams = Exam.objects.all()
    return render(request, 'exams/exams.html', {'exams': exams})

def add_exam(request):
    if request.method == 'POST':
        Exam.objects.create(
            name=request.POST['name'],
            subject=request.POST['subject'],
            date=request.POST['date'],
            max_marks=request.POST['max_marks']
        )
        messages.success(request, "Exam added!")
        return redirect('exams_home')  # <-- corrigé
    return render(request, 'exams/add-exam.html')

def edit_exam(request, id):
    exam = get_object_or_404(Exam, id=id)
    if request.method == 'POST':
        exam.name = request.POST['name']
        exam.subject = request.POST['subject']
        exam.date = request.POST['date']
        exam.max_marks = request.POST['max_marks']
        exam.save()
        messages.success(request, "Exam updated!")
        return redirect('exams_home')  # <-- corrigé
    return render(request, 'exams/edit-exam.html', {'exam': exam})

def delete_exam(request, id):
    exam = get_object_or_404(Exam, id=id)
    exam.delete()
    messages.success(request, "Exam deleted!")
    return redirect('exams_home')  # <-- corrigé