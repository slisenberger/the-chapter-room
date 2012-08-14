from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Guestlist(models.Model):
    """
    brother_bids configures the amount of bids each individual brother gets,
    while pledge_bids configures the amount of bids each pledge gets
    """
    brother_bids = models.IntegerField()
    pledge_bids = models.IntegerField()
    close_date = models.DateTimeField('when the guestlist closes')
    
    def __unicode__(self):
        return str(self.close_date)

class Guest(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    guestlist = models.ForeignKey(Guestlist)
    inviter = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.firstname + " " + self.lastname