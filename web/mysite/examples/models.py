from django.db import models

# Dog.objects.filter(name__startswith="B")
# Dog.objects.filter(age__gt=1)

class Owner(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Dog(models.Model):
    SEX_CHOICES = (
        ('M', 'Pies'),
        ('F', 'Suczka'),
        ('X', 'Nieznane')
    )
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    race = models.CharField(max_length=128)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='X')
    rodowod = models.BooleanField()
    owner = models.ForeignKey(Owner, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.race} {self.name}"
