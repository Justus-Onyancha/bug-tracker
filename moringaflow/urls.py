


from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def bugs(request):
    return HttpResponse("This is a bug page")

def bug(request):
    return HttpResponse("single bug")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bugs/',bugs, name="bugs"),
    path('bug/',bugs, name="bug")
]
