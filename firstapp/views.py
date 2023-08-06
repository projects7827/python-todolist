from django.shortcuts import render,HttpResponse
from .models import all_tasks

def index(request):
    template_data = all_tasks.objects.all()
    return render(request,"index.html",{"template_data":template_data})


def delete_record(request):
    print(request.id)
    id = request.id
    data = all_tasks.objects.get(id=10)
    data.delete()
    return HttpResponse("done")
    
