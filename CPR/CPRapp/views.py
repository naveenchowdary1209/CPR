from django.shortcuts import render,redirect
from CPRapp.forms import UsForm,ImForm,UtupForm
from .models import Contact,ImProfile,Problem
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(rq):
	return render(rq,'html/home.html')
def about(rq):
	return render(rq,'html/about.html')
def contact(rq):
	if rq.method=="POST":
		contact=Contact()
		fname=rq.POST.get('fname')
		lname=rq.POST.get('lname')
		email=rq.POST.get('email')
		contactno=rq.POST.get('contactno')
		subject=rq.POST.get('subject')
		contact.fname=fname
		contact.lname=lname
		contact.email=email
		contact.contactno=contactno
		contact.subject=subject
		contact.save()
		return HttpResponse("<h1>Thanks for Contacting us</h1>")

	return render(rq,'html/contact.html')
def register(request):
	if request.method=="POST":
		p=UsForm(request.POST)
		if p.is_valid():
			p.save() #(commit==false to print name in msg)
			messages.success(request,"Registered Successfully")
			
			return redirect('/lg')
	p=UsForm()
	return render(request,'html/register.html',{'u':p})
@login_required
def dashboard(request):
	return render(request,'html/dash.html');
@login_required	
def profile(req):
	d=ImForm()
	return render(req,'html/profile.html',{'d':d})
@login_required
def updpf(request):
	if request.method == "POST":
		u=UtupForm(request.POST,instance=request.user)
		i=ImForm(request.POST,request.FILES,instance=request.user.improfile)
		if u.is_valid() and i.is_valid():
			u.save()
			i.save()
			return redirect('/dash')
	u=UtupForm(instance=request.user)
	i=ImForm(instance=request.user.improfile)
	return render(request,'html/updateprofile.html',{'us':u,"imp":i})
@login_required	
def addpro(rq):
	if rq.method=="POST":
		problem=Problem()
		ptitle=rq.POST.get('ptitle')
		pdesc=rq.POST.get('pdesc')
		location=rq.POST.get('location')
		problem.ptitle=ptitle
		problem.pdesc=pdesc
		problem.location=location
		problem.save()
		return render(rq,'html/addpro.html')

	return render(rq,'html/addpro.html')
@login_required	
def pns(rq):
	data=Problem.objects.all()
	return render(rq,'html/pns.html',{'info':data})
@login_required	
def contview(rq):
	data=Contact.objects.all()
	return render(rq,'html/contview.html',{'info':data})
@login_required	
def userview(rq):
	d=User.objects.all()
	return render(rq,'html/userview.html',{'d':d})
@login_required	
def more(rq,id):
	h=ImProfile.objects.get(uid=id)
	return render(rq,'html/more.html',{'yu':h})
@login_required	
def dlt(rq,id):
	data=User.objects.get(id=id)
	if rq.method=="POST":
		data.delete()
		return redirect('/uview')
	return render(rq,'html/userdel.html',{'info':data})