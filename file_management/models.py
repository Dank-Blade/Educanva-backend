from django.db import models
from accounts.models import User

# Create your models here.

    
class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=255)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    published = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'file_management'
    