
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="g1"), 
    path('signup/',views.signup,name="signup"),
    path('login/', views.login_up, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('first/',views.first,name="first"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update"),
]







