from django.urls import include, path 
from account.views import HelloView,CreateUserView,UserAccountChangeAPIView

urlpatterns = [
    path('hello/', HelloView.as_view(), name ='hello'), 
    path('register/',CreateUserView.as_view(),name='register'),


    path('me/<str:username>', UserAccountChangeAPIView.as_view(), name='changeProfile'),
]
