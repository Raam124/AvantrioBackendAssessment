from django.urls import include, path 
from jobs.views import JobList,JobDetail,WorkhistoryList,WorkhistoryDetail



urlpatterns = [
    path('', JobList.as_view()),
    path('<int:pk>/',JobDetail.as_view()),
    path('workhistory/', WorkhistoryList.as_view()),
    path('workhistory/<int:pk>/',WorkhistoryDetail.as_view()),
]
