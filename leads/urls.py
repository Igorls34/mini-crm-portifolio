from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.lead_list, name='lead_list'),
    path('pipeline/', views.lead_pipeline, name='lead_pipeline'),
    path('activity-logs/', views.activity_logs, name='activity_logs'),
    path('<int:pk>/update-status/', views.update_lead_status, name='update_lead_status'),
    path('create/', views.lead_create, name='lead_create'),
    path('<int:pk>/', views.lead_detail, name='lead_detail'),
    path('<int:pk>/edit/', views.lead_edit, name='lead_edit'),
    path('<int:pk>/delete/', views.lead_delete, name='lead_delete'),
    path('export/xlsx/', views.export_leads_xlsx, name='export_xlsx'),
    path('export/pdf/', views.export_leads_pdf, name='export_pdf'),
]