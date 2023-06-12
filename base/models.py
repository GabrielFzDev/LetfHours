from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Starting with the creation of small tables
class CategoryAction(models.Model):
    nameCategory = models.CharField(max_length=200, null=True)
    
    def __str__(self) -> str:
        return self.nameCategory

class Action(models.Model):
    nameAction = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(CategoryAction, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return self.nameAction

class Projects(models.Model):
    name = models.CharField(max_length=200)
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    projectBegin = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    id = models.BigAutoField(primary_key=True)
    
    def __str__(self):
        return self.name

class Activity(models.Model):
    idproject = models.ForeignKey(Projects,on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.ForeignKey(Action,on_delete=models.SET_NULL, null=True)
    categoryAction = models.ForeignKey(CategoryAction,on_delete=models.SET_NULL, null=True)
    workedHours = models.DecimalField(decimal_places=2,max_digits=5)
    description = models.TextField()
    initialDate = models.DateField()
    terminalDate = models.DateField()
    snapshot = models.DateTimeField(auto_now=True)
    