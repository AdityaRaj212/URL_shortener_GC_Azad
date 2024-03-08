from django.urls import path

from .views import home_view, redirect_url_view, view_all_urls, user_login, user_signup, user_logout
from . import views
# from .views import home_view, redirect_url_view, view_all_urls

appname = "shortener"

urlpatterns = [
    path("", home_view, name="home"),
    path('<str:shortened_part>', redirect_url_view, name="redirect"),
    path('all-urls/', view_all_urls, name='all_urls'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name="signup"),
    path('logout/',views.user_logout, name="logout"),
]