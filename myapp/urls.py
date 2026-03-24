from django.urls import path
from .import views
urlpatterns=[
    path('create/',views.create,name='create'),
    path('view/',views.view_employee,name='view_employee'),
    path('edit/<int:id>',views.editemployee,name='editemployee'),
    path('delete/<int:id>',views.deleteemployee,name='deleteemployee')
]