from django.db import models
import uuid         

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    # In default the null field is False, which means it cannot be empty
    """
    About Blank and Null fields:  

    null=True sets NULL (versus NOT NULL) on the column in your DB. 
    Blank values for Django field types such as DateTimeField or ForeignKey will be stored as NULL in the DB.

    blank determines whether the field will be required in forms. 
    This includes the admin and your custom forms. 
    If blank=True then the field will not be required, whereas if it's False the field cannot be blank.

    The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form, 
    you're going to also need your database to allow NULL values for that field. 

    The exception is CharFields and TextFields, which in Django are never saved as NULL. 
    Blank values are stored in the DB as an empty string ('').
    """
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, blank=True, null=True)
    source_link = models.CharField(max_length=2000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    
    # Django create default id as primary key 
    id = models.UUIDField(unique=True, default=uuid.uuid4, 
                        primary_key=True, editable=False)
    

    def __str__(self): 
        return self.title  


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )

    project = models.ForeignKey(Project, on_delete=models.SET_NULL)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    """
    The difference between uuid and the default id set by Django.
    
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self): 
        return self.value 
    
