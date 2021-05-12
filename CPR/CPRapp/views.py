from django.shortcuts import render,redirect
from CPRapp.forms import UsForm,ImForm,UtupForm
from .models import Contact,ImProfile,Problem,Worker,Member,FloorManager
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
import datetime
from CPR.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(rq):
	data=Problem.objects.all()
	return render(rq,'html/home.html',{'info':data})
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
		email=request.POST.get('email')
		try:
			Member.objects.get(memail=email)
		except ObjectDoesNotExist:
			messages.warning(request,'SORRY !!! ONLY COMMUNITY MEMBERS CAN REGISTER IN THIS....KINDLY CONTACT COMMUNITY HEAD')
			return redirect('/reg')

		if User.objects.filter(email=email).exists():
			messages.warning(request,'Email is already existing')
			return redirect('/reg')
		else:
			p=UsForm(request.POST)
			if p.is_valid():
				p.save() #(commit==false to print name in msg)
				messages.success(request,"Registered Successfully...! Login Here.. ")
				return redirect('/lg')
	p=UsForm()
	return render(request,'html/register.html',{'u':p})
@login_required
def dashboard(request):
	count1=Problem.objects.filter(pstatus="NotSolved").count()
	count2=Problem.objects.filter(pstatus="InProgress").count()
	count3=Problem.objects.filter(pstatus="Completed").count()
	return render(request,'html/dash.html',{'NScount':count1,'IPcount':count2,'Ccount':count3});
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
		doorno=rq.POST.get('doorno')
		now=datetime.datetime.now()
		postdate=now.strftime("%d-%m-%Y")
		postedby=rq.user.username
		useremail=rq.user.email
		problem.ptitle=ptitle
		problem.pdesc=pdesc
		problem.doorno=doorno
		problem.postdate=postdate
		problem.postedby=postedby
		problem.useremail=useremail
		problem.save()
		messages.success(rq,"Problem Reported Successfully..!!")
		return render(rq,'html/addpro.html')

	return render(rq,'html/addpro.html')
@login_required	
def addmem(rq):
	if rq.method=="POST":
		member=Member()
		mname=rq.POST.get('mname')
		memail=rq.POST.get('memail')
		mcno=rq.POST.get('mcno')
		mdoorno=rq.POST.get('mdoorno')
		member.mname=mname
		member.memail=memail
		member.mcno=mcno
		member.mdoorno=mdoorno
		member.save()
		messages.success(rq,'Member is Successfully Added to Community')
		return render(rq,'html/AddMember.html')
	return render(rq,'html/AddMember.html')
@login_required	
def addwork(rq):
	if rq.method=="POST":
		worker=Worker()
		wname=rq.POST.get('wname')
		wdesg=rq.POST.get('wdesg')
		contactno=rq.POST.get('cno')
		location=rq.POST.get('location')
		worker.wname=wname
		worker.wdesg=wdesg
		worker.contactno=contactno
		worker.location=location
		worker.save()
		messages.success(rq,'Worker is Successfully Added for Community....')
		return render(rq,'html/Addworker.html')
	return render(rq,'html/Addworker.html')
@login_required	
def workview(rq):
	data=Worker.objects.all()
	return render(rq,'html/workview.html',{'info':data})
@login_required	
def addfm(rq):
	if rq.method=="POST":
		floormanager=FloorManager()
		fmname=rq.POST.get('fmname')
		floorno=rq.POST.get('floorno')
		fcno=rq.POST.get('fcno')
		floormanager.fmname=fmname
		floormanager.floorno=floorno
		floormanager.fcno=fcno
		floormanager.save()
		messages.success(rq,'Block Manager is Successfully Added to Community')
		return render(rq,'html/Addfloormanager.html')
	return render(rq,'html/Addfloormanager.html')
@login_required	
def fmview(rq):
	data=FloorManager.objects.all()
	return render(rq,'html/fmview.html',{'info':data})
@login_required	
def pns(rq):
	data=Problem.objects.filter(pstatus="NotSolved")
	return render(rq,'html/pns.html',{'info':data})
@login_required	
def pis(rq):
	data=Problem.objects.filter(pstatus="InProgress")
	return render(rq,'html/pis.html',{'info':data})

@login_required	
def ps(rq):
	data=Problem.objects.filter(pstatus="Completed")
	return render(rq,'html/ps.html',{'info':data})
@login_required
def vote(rq,id):
        count=Problem.objects.get(id=id)
        count.vote += 1
        count.save()
        return redirect('/pns') 
@login_required
def vote1(rq,id):
        count=Problem.objects.get(id=id)
        count.vote += 1
        count.save()
        return redirect('/pis') 
@login_required	
def contview(rq):
	data=Contact.objects.all()
	return render(rq,'html/contview.html',{'info':data})
@login_required	
def userview(rq):
	d=User.objects.all()
	return render(rq,'html/userview.html',{'d':d})
@login_required	
def memview(rq):
	d=Member.objects.all()
	return render(rq,'html/memview.html',{'d':d})
@login_required	
def more(rq,id):
	h=ImProfile.objects.get(uid=id)
	return render(rq,'html/more.html',{'yu':h})
@login_required	
def delete(rq,id):
	data=User.objects.get(id=id)
	if rq.method=="POST":
		data.delete()
		return redirect('/uview')
	return render(rq,'html/userdel.html',{'info':data})
@login_required	
def memdlt(rq,id):
	data=Member.objects.get(id=id)
	if rq.method=="POST":
		data.delete()
		return redirect('/mview')
	return render(rq,'html/memdel.html',{'info':data})
@login_required	
def fmdlt(rq,id):
	data=FloorManager.objects.get(id=id)
	if rq.method=="POST":
		data.delete()
		return redirect('/fmview')
	return render(rq,'html/fmdel.html',{'info':data})
@login_required	
def pdlt(rq,id):
	data=Problem.objects.get(id=id)
	if rq.method=="POST":
		data.delete()
		return redirect('/pns')
	return render(rq,'html/problemdel.html',{'info':data})
@login_required
def fmupdate(rq,id):
	data=FloorManager.objects.get(id=id)
	if rq.method == "POST":
		floormanager=FloorManager.objects.get(id=id)
		fmname=rq.POST.get('fmname')
		floorno=rq.POST.get('floorno')
		fcno=rq.POST.get('fcno')
		floormanager.fmname=fmname
		floormanager.floorno=floorno
		floormanager.fcno=fcno
		floormanager.save()
		messages.success(rq,'Block Manager details are Successfully Updated ')
		return redirect('/fmview')	
	return render(rq,'html/UpdateFm.html',{'info':data})
@login_required
def wupdate(rq,id):
	data=Worker.objects.get(id=id)
	if rq.method == "POST":
		worker=Worker.objects.get(id=id)
		wname=rq.POST.get('wname')
		wdesg=rq.POST.get('wdesg')
		contactno=rq.POST.get('contactno')
		location=rq.POST.get('location')
		worker.wname=wname
		worker.wdesg=wdesg
		worker.contactno=contactno
		worker.location=location
		worker.save()
		messages.success(rq,'Worker details are Successfully Updated ')
		return redirect('/workview')	
	return render(rq,'html/UpdateWorker.html',{'info':data})
@login_required	
def wdlt(rq,id):
	data=Worker.objects.get(id=id)
	if rq.method=="POST":
		data.delete()
		messages.success(rq,'Worker is Successfully Deleted ')
		return redirect('/workview')
	return render(rq,'html/workdel.html',{'info':data})
@login_required	
def workon(rq,id):
	data=Problem.objects.get(id=id)
	if rq.method=="POST":
		count=Problem.objects.get(id=id)
		wassigned=rq.POST.get('wname')
		estimatedtime=rq.POST.get('stime')
		count.wassigned=wassigned
		count.estimatedtime=estimatedtime
		count.pstatus="InProgress"
		count.save()
		subject = 'Your Problem is Acknowledged Successfully'
		message = 'Hi '+count.postedby+'... Your Problem '+count.ptitle+' is successfully taken up for consideration with an id no..'+str(count.id)+' and Your Problem will be resolved by '+count.estimatedtime
		recepient = str(count.useremail)
		send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
		return redirect('/pns')
        
	return render(rq,'html/workon.html',{'info':data})
@login_required	
def Upstatus(rq,id):
	data=Problem.objects.get(id=id)
	if rq.method=="POST":
		count=Problem.objects.get(id=id)
		pamount=rq.POST.get('amount')
		cfamount=rq.POST.get('amount1')
		xamount=rq.POST.get('amount2')
		paystatus=rq.POST.get('paystatus')
		count.pamount=pamount
		count.cfamount=cfamount
		count.xamount=xamount
		count.paystatus=paystatus
		count.pstatus="Completed"
		count.save()
		subject = 'Your Problem is Resolved Successfully'
		message = 'Hi '+count.postedby+'... Your Problem '+count.ptitle+' is successfully Resolved and..<br> Total Amount Worker Charged: '+str(count.pamount)+'<br> Amount Used from community fund : '+str(count.cfamount)+' <br> Any Extra Amount to be paid : '+str(count.xamount)+'<br> Payment Status :'+count.paystatus
		recepient = str(count.useremail)
		send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
		return redirect('/pis')
	 
	return render(rq,'html/UpdateStatus.html',{'info':data})
@login_required	
def givefeedback(rq,id):
	data=Problem.objects.get(id=id)
	if rq.method=="POST":
		count=Problem.objects.get(id=id)
		feedback=rq.POST.get('feedback')
		count.feedback=feedback
		count.save()
		return redirect('/ps')
	 
	return render(rq,'html/givefeedback.html',{'info':data})