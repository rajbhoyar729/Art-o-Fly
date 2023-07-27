from djongo import models
from djongo.models.fields import forms

class Event(models.Model): 
    Event_name = models.CharField(max_length=100)    
    organizer  = models.CharField(max_length=100)    
    class Meta:        abstract = True
    
class participants(forms.ModelForm): 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone  = models.IntegerField((""))