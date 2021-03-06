from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author              = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title               = models.CharField(max_length=200)
    content             = models.TextField()
    # attachment          = models.FileField(upload_to='uploads/%Y/%m/%d/', max_length=200)
    created_date        = models.DateTimeField(default=timezone.now)
    published_date      = models.DateTimeField(blank=True, null=True)
    last_edited_date    = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def edit(self):
        # Placeholder method
        return
    
    def share(self):
        # Placeholder method
        return

    def __str__(self):
        return self.title + " - " + str(self.created_date.date())