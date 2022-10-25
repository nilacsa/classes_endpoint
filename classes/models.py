from django.db import models

# Create your models here.

class Course (models.Model):
    course_name = models.CharField(max_length = 100)
    credit = models.CharField (max_length = 25)
    amount = models.CharField (max_length = 100)

    def __str__ (self):
        return self.course_name + ' ' + self.credit + ' ' + self.amount 

