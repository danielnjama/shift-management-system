from django.urls import path
from . import views

urlpatterns = [
    
    # path('',views.index,name='index'),
    path('', views.shift_list, name='shift_list'),
    # path('download-shift-summary-excel/', views.download_shift_summary_excel, name='download_shift_summary_excel'),
 
    
]