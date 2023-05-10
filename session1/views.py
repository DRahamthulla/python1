from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('crea/')
def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except  KeyError:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")