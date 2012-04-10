from django.db import models


class RequestEntry(models.Model):
    """ Model to store request entries """

    path = models.CharField(max_length=255)
    method = models.CharField(default='GET', max_length=10)
    get_data = models.TextField(blank=True, null=True)
    post_data = models.TextField(blank=True, null=True)
    meta_data = models.TextField()
    host = models.CharField(max_length=255)
    user_agent = models.CharField(max_length=150)
    creation_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creation_time']

    def __unicode__(self):
        return u'[%s] %s %s' % (self.creation_time.isoformat(),
                                self.method,
                                self.path)
