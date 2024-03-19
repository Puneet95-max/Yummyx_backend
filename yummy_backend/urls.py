from django.contrib import admin
from django.urls import path
from yummy_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chef/' , chef),
    path('testimonial/' , testimonial),
    path('login/', login),
    path('signup/', signup),
    path('test/' , test)
]
