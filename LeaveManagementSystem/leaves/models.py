from django.db import models
from registration.models import *

class Leaves(models.Model):
    applied_date=models.DateTimeField(auto_now=True,null=True,blank=False)
    employee_id=models.ForeignKey(Faculty,on_delete=models.CASCADE,null=True,default=None)
    start_date = models.DateField(null=True,blank=False)
    end_date = models.DateField(null=True,blank=False)
    number_of_days=models.SmallIntegerField()
    leave_type = models.CharField(max_length=25,null=True,blank=False)
    reason = models.CharField(max_length=255,null=True,blank=True)
    status = models.JSONField()

#different types of faculty and their default leave balances
male_teaching_regular={
    "Casual Leaves" : 8,
    "Special Casual Leaves" : 7,
    "Academic Leaves" : 10,
    "Optional Holidays" : 5,
    "Medical Leaves" : 5,
}
male_teaching_contract={
    "Casual Leaves" : 15
}
male_non_teaching_regular={
    "Casual Leaves" : 8,
    "Special Casual Leaves" : 7,
    "Optional Holidays" : 5,
    "Medical Leaves" : 5,
}
male_non_teaching_contract={
    "Casual Leaves" : 15,
}
female_teaching_regular={
    "Casual Leaves" : 8,
    "Special Casual Leaves" : 7,
    "Academic Leaves" : 10,
    "Optional Holidays" : 5,
    "Medical Leaves" : 5,
}
female_teaching_contract={
    "Casual Leaves" : 15
}
female_non_teaching_regular={
    "Casual Leaves" : 8,
    "Special Casual Leaves" : 7,
    "Optional Holidays" : 5,
    "Medical Leaves" : 5,
}
female_non_teaching_contract={
    "Casual Leaves" : 15,
}

#different values of leave status
status_values=['pending','accepted','rejected']

#default value of status_json
status_default={
    "hod" : status_values[0],
    "principal" : status_values[0]
}
