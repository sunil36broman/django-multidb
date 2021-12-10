from django.urls import path
from . views import *

urlpatterns = [
    path('',DBooksListAPIView.as_view(),name='dbooks'),
    path('detail/<str:pk>/',DBooksDetailAPIView.as_view(),name='ddetail'),
    # path('create',CreateTodoAPIView.as_view(),name='create'),
    # path('update/<str:pk>/',UpdateTodoAPIView.as_view(),name='update'),
    # path('approved/<str:pk>/',ApprovedTodoAPIView.as_view(),name='approved'),
    # path('delete/<str:pk>/',DeleteTodoAPIView.as_view(),name='delete'),
]