from django.shortcuts import render_to_response
from pipeline.forms import DemoForm,ConsultForm

# Create your views here.
def index(request):
	return render_to_response('index.html') # brief introduction, point out lopen's features

def service(request):
	return render_to_response('service_process.html') # the arrow plot page

def demo(request,demotype):
	f_consult = ConsultForm()
	if 'demonstrate' in request.POST:
		f_demo = DemoForm(request.POST)
		text = request.POST['content']
		if f_demo.is_valid():
			if demotype == 'preptreat':
				#import necessary library
				result = 1
			elif demotype == 'liedetect':
				#import necessary library
				result = 2
			elif demotype == 'sarcasm':
				#import necessary library
				result = 3
		return render_to_response('demo.html',locals())
	elif 'consult' in request.POST:
		f_consult = ConsultForm(request.POST)
		if f_consult.is_valid():
			user = f.cleaned_data['user']
			email = f.cleaned_data['email']
			messege = f.cleaned_data['message']
			c = Consult(user=user, email=email, content=content, demotype=demotype)
			c.save()
			f_consult = ConsultForm()
	else:
		if demotype == 'preptreat':
			f_demo= CommentForm(initial={'content':'inital for pretreat'})
		elif demotype == 'liedetect':
			f_demo= CommentForm(initial={'content':'inital for liedetect'})
		elif demotype == 'sarcasm'
			f_demo= CommentForm(initial={'content':'inital for sarcasm'})
		return render_to_response('demo.html',locals())
