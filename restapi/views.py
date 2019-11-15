# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from .models import *


def index(request):
    return HttpResponse("Hello, world. You're at Rest.")


def add_quiz(request):
    obj = quiz()
    try:
        qid = quiz.objects.latest('id')
        qid = qid.id + 1
    except(quiz.DoesNotExist):
        qid = 1
    if request.method == 'POST':
        qname = request.POST.get('qname')
        qdesc = request.POST.get('qdescription')
        if quiz.objects.all().filter(name=qname).exists():
            return render(request, 'addquiz.html', context={'quizid': qid})
        else:
            obj=quiz(id=qid,name=qname,description=qdesc)
            obj.save()
            return render(request, 'addquiz.html', context={'quizid': qid+1})
    return render(request,'addquiz.html',context={'quizid': qid})

def addquestion(request):
    obj=questions()
    try:
        quid=questions.objects.latest('id')
        quid=quid.id+1
    except(questions.DoesNotExist):
        quid=1
    ob1 = quiz.objects.all()
    if request.method=='POST':
        quizname=request.POST.get('selectquiz')
        qname=request.POST.get("qname")
        opti1=request.POST.get('opt1')
        opti2=request.POST.get('opt2')
        opti3=request.POST.get('opt3')
        opti4=request.POST.get('opt4')
        correc=request.POST.get('correctans')
        anspo=request.POST.get('anspoint')
        if questions.objects.all().filter(name=quizname).exists():
            return render(request, 'addquestion.html', context={'data': ob1, 'quesid': quid})
        else:
            obj.id=quid
            obj.name=qname
            obj.correct_option=correc
            s=opti1+","+opti2+","+opti3+","+opti4
            obj.options=s
            obj.points=anspo
            obj.quiz=quizname
            obj.save()
            return render(request, 'addquestion.html',context={'data':ob1,'quesid':quid+1})
    return render(request, 'addquestion.html',context={'data':ob1,'quesid':quid})


def view_answer(request):
    return render(request, 'view_answer.html')


def view_quiz(request):
    data1=quiz.objects.all()
    if request.method=='POST':
        selected_item = get_object_or_404(quiz, name=request.POST.get('selectquiz'))
        obj=questions.objects.all().filter(quiz=selected_item.name)
        return render(request, 'view_quiz.html', context={'selectedval': selected_item, 'data': obj,'data1':data1})
    return render(request,'view_quiz.html',context={'data1':data1})

def score(request):
    return render(request, 'score.html')


def log(request):
    if request.method=="POST":
        un=request.POST["u"]
        ps=request.POST["p"]

        if registration.objects.all().filter(uname=un).filter(pswd1=ps).exists():
            obj=registration.objects.get(uname=un)
            return redirect('/viewquestion')
        else:
            return render(request, 'log.html', {'msg': 'Incorrect username or password'})
    return render(request, 'log.html')


def regis(request):
    if request.method=="POST":
        uuname=request.POST.get("name")
        ppswd1=request.POST.get("pswda")
        ppswd2=request.POST.get("pswdb")

        if ppswd1==ppswd2:
            if registration.objects.all().filter(uname=uuname).exists():
                return render(request,'regis.html',{'e':'User already exists'})
            else:
                registration.objects.get_or_create(uname=uuname,pswd1=ppswd1,pswd2=ppswd2)
                return redirect('/login',{'e':'Successfuly registered'})
        else:
            return render(request,'regis.html',{'e':'Password mismatch'})

    return render(request, 'regis.html')
