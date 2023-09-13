# What is Django URLs?make program to create django urls
"""
=>  URLs are used to map incoming HTTP requests to specific views within your web application.

URL MODULE

        from django.contrib import admin
        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.home, name='home' ),
        ]


VIWE MODULE

        def home(request):
            return render(request,"myapp/index.html")


"""