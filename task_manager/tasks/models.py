from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
    ('To do','To do'),
    ('In progress','In progress'),
    ('Done','Done'),
    ]
    
    PRIORITY_CHOICES = [
        ('High','High'),
        ('Medium','Medium'),
        ('Low','Low'),
    ]

    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    assigned_to = models.CharField()
    date_created = models.DateField(editable=False, auto_now_add=True)
    due_date = models.DateField()
    owner = models.ForeignKey('auth.user', related_name='tasks', on_delete=models.CASCADE)


    def __str__(self):
        return self.title
