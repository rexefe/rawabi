from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    num_profiles = models.IntegerField()
    country_logo = models.ImageField(upload_to='images/',default='/images/man_2.jpg')
    


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%i/country" % self.id

class Profile(models.Model):
    LEVEL = [
        ('undergraduate', 'Under Graduate'),
        ('graduate', 'Graduate'),
    ]
    SEX = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    profile_url = models.ImageField(upload_to='images/',default='/images/test1.jpg')
    gender = models.CharField(
        max_length=20,
        choices=SEX,
        default='male',
    			)        
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    level_edu = models.CharField(
        max_length=20,
        choices=LEVEL,
        default='graduate',
    			)          
    prof = models.CharField(max_length=100)
    bio  = models.TextField(max_length=100)
    is_reserved = models.BooleanField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%i/profile" % self.id







