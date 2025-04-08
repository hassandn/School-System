from django.db import models
from django.contrib.gis.db import models as gis_models


class School(models.Model):
    name = models.CharField(max_length=255)
    location = gis_models.PointField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    teachers = models.ManyToManyField('accounts.CustomUser', on_delete=models.CASCADE, related_name='schools',limit_choices_to={'role': 'teacher'})
    
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    classrooms = models.ManyToManyField('Classroom', on_delete=models.CASCADE, related_name='courses')
    schools = models.ManyToManyField(School, on_delete=models.CASCADE, related_name='courses')
    
    def __str__(self):
        return self.name
    
class Classroom(models.Model):
    name = models.CharField(max_length=255)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classrooms')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    teacher = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='courses')
    students = models.ManyToManyField('accounts.CustomUser', blank=True, related_name='enrolled_courses')    

    def __str__(self):
        return self.name

class New(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='news')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='news') 
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='news', limit_choices_to={'role': 'teacher'})
    viewed_by = models.ManyToManyField('accounts.CustomUser', blank=True, related_name='viewed_news')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='exercises')
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='exercises', limit_choices_to={'role': 'teacher'})
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title 


class Answer(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='answers')
    student = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='answers', limit_choices_to={'role': 'student'})
    content = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.username}'s answer to {self.exercise.title}"
