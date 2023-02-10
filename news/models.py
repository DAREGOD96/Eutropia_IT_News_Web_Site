from django.db import models

# Create your models here.

class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_image = models.ImageField(upload_to='NewsImages')
    news_description = models.TextField(default= 'null')

    def __str__(self):
        return str(self.id)
