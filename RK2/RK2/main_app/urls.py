from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('processor', views.processor_list),
    path('processor/create', views.ProcessorCreate.as_view()),
    path('processor/<int:id>/update', views.ProcessorUpdate.as_view(), name='processor_update'),
    path('processor/<int:id>/delete', views.ProcessorDelete.as_view(), name='processor_delete'),
    path('PC', views.PC_list),
    path('PC/create', views.PCCreate.as_view()),
    path('PC/<int:id>/update', views.PCUpdate.as_view(), name='PC_update'),
    path('PC/<int:id>/delete', views.PCDelete.as_view(), name='PC_delete'),
    path('report', views.report)
]