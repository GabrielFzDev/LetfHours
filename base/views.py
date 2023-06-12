from django.shortcuts import render
from .models import Activity,CategoryAction,Action,Projects
from django.db.models import Q
# Create your views here.
def homeView(request):
    projects = Projects.objects.all()
    activity = Activity.objects.all()
    category = CategoryAction.objects.all()
    if request.GET.get('queryC') != None:
        qc = request.GET.get('queryC') 
        act = Action.objects.filter(category_id=qc)
    else:
        act = None
    
    context = {'activity':activity,'category':category,'acts':act,'projects':projects}
    return render(request,'base/home.html',context)
