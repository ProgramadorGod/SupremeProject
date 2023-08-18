from django.db import models

# Create your models here.


class Services(models.Model):
    Title = models.CharField(max_length=30)
    Content = models.CharField(max_length=30)
    Image = models.ImageField(upload_to='Services')
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='service'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.Title
    