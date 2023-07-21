from django.shortcuts import render

# Create your views here.
def home(request):
    ct = request.session.get('count',0)
    newcount = ct+1
    request.session['count'] = newcount
    if newcount>=10:
        request.session.flush()
        request.session.clear_expired()
    return render(request,'myapp/home.html',{'c':newcount})      