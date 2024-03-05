from django.urls import path

from .views import home_view, redirect_url_view, view_all_urls

appname = "shortener"

urlpatterns = [
    path("", home_view, name="home"),
    path('<str:shortened_part>', redirect_url_view, name="redirect"),
    path('all-urls/', view_all_urls, name='all_urls'),
]