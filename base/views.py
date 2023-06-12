from django.shortcuts import render
from .models import Activity
# Create your views here.
def homeView(request):
    activity = Activity.objects.all()
    context = {'activity':activity}
    return render(request,'base/home.html',context)
