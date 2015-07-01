from django.db import models


class Contact(models.Model):
    '''
    Some attributes might not be in the provided csv, but I consider
    them of importance.
    '''

    name = models.CharField(max_length=100, help_text="Contact's full name.")
    email = models.EmailField(blank=True)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=35, blank=True)
    state = models.CharField(max_length=20, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.phone_number)
