from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import Poll

# Create your views here.
def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_poll_list' : latest_poll_list,
		})

	#output = ', '.join([p.question for p in latest_poll_list])
	#return HttpResponse(output)
	#return HttpResponse(template.render(context))
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	return render(request, 'polls/detail.html', {'poll':poll})

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s. " % poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)

