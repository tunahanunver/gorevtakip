from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Gorevtakip
# Create your views here.

def index(request):
    gorevtakips = Gorevtakip.objects.all()
    return render(request,"index.html", {"gorevtakips": gorevtakips})

def addGorev(request):
    if request.method == "GET":
        return redirect("/")
    else:
        title = request.POST.get("title")
        newGorev = Gorevtakip(title = title,completed = False)

        newGorev.save()
        return redirect("/")
    
def update(request, id):
    gorev = get_object_or_404(Gorevtakip,id = id)

    gorev.completed = not gorev.completed
    gorev.save()
    return redirect("/")

def delete(request, id):
    gorev = get_object_or_404(Gorevtakip,id = id)

    gorev.delete()
    return redirect("/")