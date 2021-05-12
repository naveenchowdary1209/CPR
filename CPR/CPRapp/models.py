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
		return self.fname+" "+self.lname+" "+self.email+" "+self.contactno+" "+self.subject
class ImProfile(models.Model):
	g = [('M',"Male"),('F','Female')]
	age = models.IntegerField(default=10)
	gender = models.CharField(max_length=10,choices=g)
	aadharno=models.CharField(max_length=16,default='')
	contactno=models.CharField(max_length=10,default='')
	doorno=models.CharField(max_length=100,default='')
	uid = models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def createpf(sender,instance,created,**kwargs):
	if created:
		ImProfile.objects.create(uid=instance)

class Problem(models.Model):
	ptitle=models.CharField(max_length=200)
	pdesc=models.TextField()
	doorno=models.CharField(max_length=200)
	postdate=models.TextField(max_length=200,default='')
	postedby=models.CharField(max_length=200,default='')
	useremail=models.EmailField(max_length=200,default='')
	vote= models.IntegerField(default=0)
	pstatus=models.TextField(max_length=200,default='NotSolved')
	wassigned=models.CharField(max_length=200,default='')
	pamount=models.IntegerField(default=0)
	cfamount=models.IntegerField(default=0)
	xamount=models.IntegerField(default=0)
	estimatedtime=models.TextField(max_length=200,default='')
	paystatus=models.TextField(default=0)
	feedback=models.CharField(max_length=200,default='')
	def __str__(self):
		return self.ptitle+""+self.pdesc+" "+self.doorno+""+self.postdate+""+self.postedby+""+self.vote+""+self.pamount+""+self.paystatus
class Worker(models.Model):
	wname=models.CharField(max_length=200)
	wdesg=models.TextField()
	contactno=models.CharField(max_length=10,default='')
	location=models.CharField(max_length=200)
	
	def __str__(self):
		return self.wname+""+self.wdesg+" "+self.contactno+""+self.location
class Member(models.Model):
	mname=models.CharField(max_length=200)
	memail=models.EmailField(max_length=200)
	mcno=models.CharField(max_length=10,default='')
	mdoorno=models.CharField(max_length=200)
	
	def __str__(self):
		return self.mname+""+self.memail+" "+self.mcno+""+self.mdoorno
class FloorManager(models.Model):
	fmname=models.CharField(max_length=200)
	floorno=models.CharField(max_length=200)
	fcno=models.CharField(max_length=10,default='')
	def __str__(self):
		return self.fmname+""+self.floorno+" "+self.fcno
		
		