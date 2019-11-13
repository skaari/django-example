from django.shortcuts import render

# Create your views here.
def index(request):
    mydict={'text':'Hello World','number':100}
    return render(request,"template_app/index.html",context=mydict)

def other(request):
    return render(request,"template_app/other.html")

def relative(request):
    return render(request,"template_app/relative_urls_templates.html")
