from django.db import models

from django.db import models

class Profile(models.Model):
   name = models.CharField(max_length = 50)
   file = models.FileField(upload_to = 'files')

   class Meta:
      db_table = "profile"
