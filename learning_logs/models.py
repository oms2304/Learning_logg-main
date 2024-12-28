from django.db import models
from django.contrib.auth.models import User


"""Models are pretty much classes"""

# Create your models here.
class Topic(models.Model): # Model so we can create a topic (cannot be edited untill an entry model is made)
    """models.Model inherits from Model (already existing python library) the basic function of a Model"""
    """A topic the user is learning about"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True) #had to manually edit the database (sqlite or smth like that) as the column (date_data) wasn't being added for some reason 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string represenation of the model"""
        return self.text
    

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #if a topic is deleted, all related entries will also get deleted
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True) 

    # allows us to present entries the date
    # and time they were added & place a timestamp next to each entry

    class Meta:
        verbose_name_plural = 'entries' # tells Django to use "Entries" when it needs to refer to more than one entry

    def __str__(self):
        """Return a string represenation of the model"""
        summary = self.text[:50]
        length = len(self.text)

        if (length > 50):
            return summary + "..."
        else:
            return summary
