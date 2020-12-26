from rest_framework import generics
from jobs.models import Job,WorkHistory
from jobs.serializers import JobsSerializer,WorkHistorySerializer

from jobs.permissions import IsCreatedByOrReadOnly,IsCandidateOrReadOnly


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobsSerializer
    

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    # custom permissin class for only created person can edit others can view
    permission_classes = (IsCreatedByOrReadOnly,)
    queryset = Job.objects.all()
    serializer_class = JobsSerializer

# work history considered as a particular candidate has a work history
# after added a candidate to a job the candidate work history can be accessed by going throug jobs->id->candidates->id->workhistory

class WorkhistoryList(generics.ListCreateAPIView):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer

# candidate work history can be also accessed by going throug jobs->id->candidates->id->workhistory
# or like access here candidate->id as a foreigh key to access their work history


class WorkhistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # custom permisstion class for only candidate edit or delete candidate work history others can view
    permission_classes = (IsCandidateOrReadOnly,)
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer
    
