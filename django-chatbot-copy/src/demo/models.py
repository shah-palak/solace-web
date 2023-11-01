from django.db import models

# Create your models here.
class STI(models.Model):
    #store user input
    input = models.TextField()
    #store chat response
    _output = models.TextField()

    class Meta:
        db_table = "t_STI"

    def __str__(self):
        return self.input