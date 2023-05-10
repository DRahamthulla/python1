from django.shortcuts import render
from . import froms

def reform(request):
    form =froms.SingUp()
    if request.method=='POST':
        form =froms.SingUp(request.POST)
        html='we have recieved from again'
    else:
        html='welcome for first time'
    return render(request,'signup.html',{'html':html, 'form':form })

