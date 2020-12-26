from django.db import models

# all users types are considers as Users for simplicity 
# can also overide the Absract user and Base manager classes for custom authentication and various user types
from django.contrib.auth.models import User


QUESTION_CHOICES = [
        ('Problem solving', 'Problem solving'),
        ('Algorithms', 'Algorithms'),
        ('Coding', 'Coding'),
    ]

ASKING_WAYS = [
        (1, 'Direct Questions'),
        (2, 'Problem questions'),
        (3, 'Coding Questions'),
    ]

ASSESSMENT_TYPES= [
        (1, 'Online assessment'),
        (2, 'Offline assessment'),
   
    ]

# job inteview model for company while creating the job company will add respected candidates and interviewers for the job.
# to go through candidate work history we can accesss the profile of candidates and access their work history
class Job(models.Model):
    name = models.CharField(max_length=100)
    qualifications = models.TextField()
    experience = models.IntegerField()
    reporting_to = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # at the time of job inteview creation the company has to add the respected interviwers and the candidates for that job inteview
    add_interviwer = models.ManyToManyField(User,verbose_name="inteviwers_for_this_job_interview", related_name="inteviwers_for_this_job_interview")
    add_candidate = models.ManyToManyField(User, verbose_name= "candidates_for_this_job_interview",related_name="candidates_for_this_job_interview")

    def __str__(self):
        return f"{self.name}"
    
# a job can have multiple questionsets that can be access by the foreign key 
class QuestionSet(models.Model):
    regarded_job =  models.ForeignKey(Job, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    category  = models.CharField( choices= QUESTION_CHOICES ,max_length=250)
    asking_ways = models.IntegerField(choices=ASKING_WAYS,null=True)
    question_set = models.TextField()

    def __str__(self):
        return f"{self.regarded_job}-{self.title}"


# every job has multiple assesments can be accessd using foreignkey
class Assessment(models.Model):
    regarded_job  = models.ForeignKey(Job, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    assessors  = models.ManyToManyField(User, verbose_name=("add assesors for this assessment"))
    typeof_assessment = models.IntegerField(choices=ASSESSMENT_TYPES)
    assessment_brief = models.TextField()

    def __str__(self):
        return f"{self.regarded_job}-{self.title}"

# each assesment has to be marked
class AssesmentMarks(models.Model):
    regarded_assessment  = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    marks  = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.regarded_assessment}"

# each user account has work history after company assigned the user has candidate we can look at the related job candidate
# work history with the foreign key
class WorkHistory(models.Model):
    history_user = models.ForeignKey(User, on_delete=models.CASCADE)
    position  = models.CharField( max_length=150)
    workplace = models.CharField( max_length=150)
    start  = models.DateField(auto_now=False, auto_now_add=False)
    end = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.history_user}"

