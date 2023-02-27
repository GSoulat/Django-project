from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {"test" : "coco c'est un test"}
    return render(request, 'main/home_page.html', context=context)

def about(request):
    return render(request, 'about.html')