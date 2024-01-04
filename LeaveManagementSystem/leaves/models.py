from django.db import models
from registration.models import *

class Leaves(models.Model):
    employee_id=models.ForeignKey(Faculty,on_delete=models.CASCADE,null=True,default=None)
    start_date = models.DateField(null=True,blank=False)
    end_date = models.DateField(null=True,blank=False)
    number_of_days=models.SmallIntegerField()
    leave_type = models.CharField(max_length=25,null=True,blank=False)
    reason = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=12)

male_teaching_regular={
    "Casual Leaves" : 8,
    "Special Casual Leaves" : 7,
    "Academic Leaves" : 10,
    "Option Holidays" : 5,
    "Medical Leaves" : 5,
}
male_teaching_contract={
    "Casual Leaves" : 15
}
male_non_teaching_regular={
    "Casual Leaves" : 8,
    "Special Casual Leaves" : 7,
    "Option Holidays" : 5,
    "Medical Leaves" : 5,
}
male_non_teaching_contract={
    "Casual Leaves" : 15,
}
female_teaching_regular={
    "Casual Leaves" : 8,
    "Special Casual Leaves" : 7,
    "Academic Leaves" : 10,
    "Option Holidays" : 5,
    "Medical Leaves" : 5,
}
female_teaching_contract={
    "Casual Leaves" : 15
}
female_non_teaching_regular={
    "Casual Leaves" : 8,
    "Special Casual Leaves" : 7,
    "Option Holidays" : 5,
    "Medical Leaves" : 5,
}
female_non_teaching_contract={
    "Casual Leaves" : 15,
}