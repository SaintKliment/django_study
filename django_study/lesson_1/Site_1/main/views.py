from django.shortcuts import render

# Create your views here.

def index(request):         
    return render(request, 'main/index.html')
    
def about(request):         
    return render(request, 'main/about.html')

# def news(request):         
#     return HttpResponse("<h1>Привет, это news!</h1>")

# def part(request):
#     return HttpResponse('<p>ЧАСТЬ!</p>')