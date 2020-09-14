from django.db import models

from datetime import datetime 

class Department(models.Model):
    name = models.CharField(max_length=64)   
    head = models.CharField(max_length=64)
    stuff = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} run by {self.head} ({self.stuff} members)" #{self.id}: 

class Task(models.Model):
    starting_point = models.ForeignKey(Department, on_delete = models.CASCADE, related_name="task_at_hand")
    goal = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="requested_task")
    days_to_complete = models.IntegerField()
    name_task = models.CharField(max_length=265, blank=True)

    def __str__(self):
        return f"{self.starting_point} request for {self.goal}" #{self.id}: 

    # def is_deadline(request, task_id):
    #     time_to_go = datetime.now() > self.days_to_complete
    #     return time_to_go

class TeamMember(models.Model):
    f_name = models.CharField(max_length=24)
    l_name = models.CharField(max_length=24)
    task = models.ManyToManyField(Task, blank=True, related_name="member") #the Team Member May be involved in a couple of projects or 0
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"