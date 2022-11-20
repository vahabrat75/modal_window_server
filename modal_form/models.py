from django.db import models

# Create your models here.


class ModalData(models.Model):

    FORMATS = (
        ('CSV', 'CSV'),
        ('XML', 'XML')
    )
    SCHEDULES = (
        ('No Repeat', 'No Repeat'),
        ('Specific Date', 'Specific Date'),
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly')
    )
    DAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    report_name = models.CharField(max_length=100)
    format = models.CharField(max_length=15, choices=FORMATS)
    email = models.EmailField()
    schedule = models.CharField(max_length=15, choices=SCHEDULES)
    time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    date = models.DateField(null=True)
    day = models.CharField(max_length=15, choices=DAYS, null=True)
    created = models.DateTimeField(auto_now_add=True)
