from django.db import models
from accounts.models import User
from module.models import Module
# Create your models here.


def get_upload_path(instance, filename):
    """
    Returns the upload path for a content file based on the module name.
    """
    module_code = instance.module.module_code
    return f"content/{module_code}/{filename}"

class File(models.Model):
    file = models.FileField(upload_to=get_upload_path)
    name = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'file_management'

    