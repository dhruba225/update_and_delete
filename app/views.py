from django.shortcuts import render
from app.models import *

# Create your views here.

def insert_topic(request):
    topic_name=input('enter topic_name: ')
    TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
    TO.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def insert_webpage(request):
    tn=input('enter topic_name: ')
    na=input('enter name: ')
    ur=input('enter url: ')

    TO=Topic.objects.get(topic_name=tn)

    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    WO.save()

    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)



def display_topic(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO=Topic.object.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def update_webpage(request):
    
    #Webpage.objects.filter(topic_name='Foot Ball').update(name='Ronaldo')
    #Webpage.objects.filter(name='virat').update(url='https://kohli.com')
    #Webpage.objects.filter(name='Python').update(url='https://kohli.com')
    #Webpage.objects.filter(name='virat').update(topic_name='Chess')
    #QSWO=Webpage.objects.filter(name='virat').update(topic_name='Boxing')
    
    #Webpage.objects.update_or_create(topic_name='Foot Ball',defaults={'name':'NeyMar'})
    #Webpage.objects.update_or_create(topic_name='Volley Ball',defaults={'name':'NeyMar'})
    
    #RO=Topic.objects.get(topic_name='Rugby')
    #Webpage.objects.update_or_create(name='dileep',defaults={'topic_name':RO})
    
    #Webpage.objects.update_or_create(name='Hardhik',defaults={'url':'https://Hardhik.com'})
    CTO=Topic.objects.get(topic_name='Cricket')
    Webpage.objects.update_or_create(name='Hardhik',defaults={'topic_name':CTO,'url':'https://Hardhik.com'})
    
    QSWO=Webpage.objects.all()

    d={'QSWO':QSWO}

    return render(request,'display_webpage.html',d)
