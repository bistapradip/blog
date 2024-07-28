from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import home,post, category, about

urlpatterns = [
  path("",home, name = "home"),
  path("about/", about),
  path('blog/<str:url>', post, name = "post"),
  path('category/<str:url>', category, name = "category")
]  +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
