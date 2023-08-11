from django.shortcuts import render,HttpResponse
from .models import all_tasks

def index(request):
    template_data = all_tasks.objects.all()
    return render(request,"index.html",{"template_data":template_data})


def delete(request): # deleting a task or category
    id_param = request.GET.get("id")
    if id_param==None:
        return HttpResponse("Please Mention Id As Query Parameter",status=400)
    else:
        data = all_tasks.objects.filter(id=id_param)
        if not data:
            return HttpResponse("Item Not Found",status=204)
        else:
            data.delete()
            return HttpResponse("Item Deleted Successfully",status=200)
          

    
def add(request): # adding a task or category
    body = request.body.decode("utf-8")
    print(body)
          

    