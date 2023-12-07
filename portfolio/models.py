from django.db import models

class Meta(models.Model):
    name = models.CharField(max_length=16,blank=False)
    description = models.TextField(max_length=2500, blank=False)
    icon = models.ImageField(upload_to='icon')

    def __str__(self):
        return self.name

class Me(models.Model):
    name = models.CharField(max_length=16,blank=False)
    photo = models.ImageField(upload_to='images')
    intro = models.TextField(max_length=2500, blank=False)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name = models.CharField(max_length=16,blank=False)
    icon = models.ImageField(upload_to='icone')
    skill = models.TextField(max_length=200, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=16,blank=False)
    number = models.IntegerField(blank=False)
    img = models.ImageField(upload_to='project')

    def __str__(self):
        return self.name
    
class Video(models.Model):
    name = models.CharField(max_length=16,blank=False)
    video = models.FileField(upload_to='video', blank=False)

    def __str__(self):
        return self.name
      
class Message(models.Model):
    name = models.CharField(max_length=16,null=True)
    email = models.EmailField(max_length=256, null=False, blank=False)
    message = models.TextField(max_length=2500, null=False, blank=False)

    def __str__(self):
        return self.name

class Link(models.Model):
    owner = models.CharField(max_length=16)
    facebook = models.URLField(max_length=200, blank=False)
    github = models.URLField(max_length=200,blank=False)
    telgram = models.URLField(max_length=200,blank=False)

    def __str__(self):
        return self.owner