from django.urls import path
from .views import  places, create_place, place,\
    edit_place, delete_place,FeedBackView,FeedBackDatailView

urlpatterns=[
    path('', places, name='places-list'),
    path('create/', create_place, name='create-place'),
    path('<int:id>/', place, name='place'),
    path('<int:id>/edit/', edit_place, name='edit-place'),
    path('<int:id>/delete/', delete_place, name='delete-place'),
    path('feedback/', FeedBackView.as_view(), name='feedback'),
    path('feedback/<int:pk>/', FeedBackDatailView.as_view(),name='feedback'),
    path('feedback/<int:pk>/', FeedBackDatailView.as_view(), name='feedback-detail')
]