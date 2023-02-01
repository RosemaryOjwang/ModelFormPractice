from django.db import models

# Create your models here.
class Application(models.Model):

    GENDER_CHOICES = (
        ('F', 'FEMALE'),
        ('M', 'MALE')
    )

    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='files/photos')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

    def __str__(self):
       return self.email
        #return (model.first_name, self.second_name, self.last_name)

    class Meta:
        db_table = "Applications"