from django.urls import path
from . import views
urlpatterns = [
    path('list', views.student_show, name='student_show'),
    path('<int:student_roll_no>', views.details, name='full details'),
    path('<int:student_roll_no>/department/', views.department, name='department')
]