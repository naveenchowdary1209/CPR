from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Contact(models.Model):
	fname=models.CharField(max_length=200)
	lname=models.CharField(max_length=200)
	email=models.EmailField(max_length=200)
	contactno=models.CharField(max_length=200)
	subject=models.TextField()
	def __str__(self):
		return self.fname
		return self.lname
		return self.email
		return self.contactno
		
class ImProfile(models.Model):
	g = [('M',"Male"),('F','Female')]
	age = models.IntegerField(default=10)
	gender = models.CharField(max_length=10,choices=g)
	aadharno=models.CharField(max_length=16,default='')
	contactno=models.CharField(max_length=10,default='')
	place=models.CharField(max_length=100,default='')
	uid = models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def createpf(sender,instance,created,**kwargs):
	if created:
		ImProfile.objects.create(uid=instance)

class Problem(models.Model):
	ptitle=models.CharField(max_length=200)
	pdesc=models.TextField()
	location=models.CharField(max_length=200)
	def __str__(self):
		return self.ptitle
		return self.pdesc
		return self.location