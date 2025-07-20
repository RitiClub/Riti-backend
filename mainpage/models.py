from django.db import models

# Create your models here.
class Riti (models.Model):
     batch=models.IntegerField(primary_key=True)
class Members (models.Model)   :
     batch=models.ForeignKey(Riti,on_delete=models.CASCADE)
     name=models.IntegerField()
     role=models.CharField(max_length=400)

class Carsol(models.Model):
    image=models.TextField()
    caption=models.TextField()

class Logo (models.Model):
     image=models.TextField()

class Recruitment(models.Model):
     stage=models.IntegerField(primary_key=True )
     name=models.CharField(max_length=400)
     description=models.TextField()
     link=models.URLField()

class Team(models.Model):
     batch=models.IntegerField(primary_key=True)
     link=models.URLField()
     description=models.TextField()

class TeamImages(models.Model):
     batch=models.ForeignKey(Team,on_delete=models.CASCADE)
     image=models.TextField()

class Magzine(models.Model):
     mag_id=models.IntegerField(primary_key=True)

class MagImages(models.Model):
     mag_id=models.ForeignKey(Magzine,on_delete=models.CASCADE)
     image=models.TextField()

