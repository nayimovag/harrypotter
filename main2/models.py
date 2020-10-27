from django.db import models


# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=50)
    group_number = models.IntegerField()
    bio = models.TextField()
    dob = models.DateField()
    level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.full_name}' + f'{self.pk}'

    class Meta:
        verbose_name = 'Talabalar'
        verbose_name_plural = 'Talaba'
