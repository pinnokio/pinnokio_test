from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    jid = models.EmailField(blank=True, null=True)
    skype_id = models.CharField(max_length=50, blank=True, null=True)
    other_contacts = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)
