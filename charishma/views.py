from django.shortcuts import render

# Create your views here.

def if_condition(request):
    d={'a':22,'b':20}
    return render(request,'if_condition.html',context=d)
def if_else(request):
    d={'a':22,'b':25}
    return render(request,'if_else.html',context=d)
def if_elif_else(request):
    c={'a':100,'b':200,'c':500}
    return render(request,'if_elif_else.html',context=c)
def nested_if(request):
    c={'a':200,'b':500,'c':700}
    return render(request,'nested_if.html',context=c)  
def loop(request):
    c={'name':'CHARISHMA'}
    return render(request,'loop.html',context=c)