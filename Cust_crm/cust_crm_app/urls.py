from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('demo',TemplateView.as_view(template_name="bootstrap_base.html"),name='demo'),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('record/<int:pk>', views.user_record, name="record"),
    path('delete_record/<int:pk>', views.del_record, name="del_record"),
    path('add_record/', views.add_record, name="add_record"),
    path('edit_record/<int:pk>', views.edit_record, name="edit_record"),
]