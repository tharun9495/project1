from django.http import HttpResponse

def index(request):
    return HttpResponse("<marquee><h1> Reddy</h1></marquee>")
    