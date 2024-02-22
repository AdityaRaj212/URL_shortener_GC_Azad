from django.urls import path
from . import views

app_name = "url"
urlpatterns = [
    path("",views.index,name = "home"),
    path("u/<str:slugs>",views.urlRedirect,name="redirect")
]