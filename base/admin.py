from django.contrib import admin

from .models import Action,Activity,CategoryAction,Projects
# Register your models here.

admin.site.register(Action)
admin.site.register(Activity)
admin.site.register(CategoryAction)
admin.site.register(Projects)


