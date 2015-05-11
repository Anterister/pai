# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context, RequestContext, loader

from django.views.decorators.csrf import csrf_exempt

from demo.models import EmailSubscriber, EmailSubscriberForm

import json

# def email_subscribe_submit(request):
#     if request.method == 'POST':
#         f = EmailSubscriberForm(request.POST)
#         if f.is_valid():
#             return email_subscribe(request, f.email_addr)
#     return index(request)

def email_subscribe(request):
    if request.is_ajax() and request.method == 'GET':
        new_email = request.GET['subscriber_email']
        if new_email:
            if not EmailSubscriber.objects.filter(email_addr=new_email).exists():
                newSubscriber = EmailSubscriber(email_addr=new_email, dog_name="")
                newSubscriber.save()
                return HttpResponse(
                    json.dumps({"subscribe_message": 1}),
                    content_type="application/json")
            else:
                return HttpResponse(
                    json.dumps({"subscribe_message": 0}),
                    content_type="application/json"
                    )

    else:
        print "redirecting!"
        return HttpResponseRedirect('/home/')
# def email_subscribe_result(request, email_addr_in):
#     p = get_object_or_404(EmailSubscriber, pk=email_addr_in)
#     response = "Thank you for subscribing 派星宝盒. 我们已将一封邮件发送至您的邮箱: %s."
#     return HttpResponse(response % email_addr_in)



class HomePageView(TemplateView):
    template_name = 'demo/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'This is a demo of a message.')
        return context

def index(request):
    return HttpResponseRedirect('/home/')


@csrf_exempt
def home(request):

    # if request.method == 'POST':
    #     f = EmailSubscriberForm(request.POST)
    #     if f.is_valid():
    #         f.save()
    #         print f.cleaned_data
    #         email_addr_in = f.cleaned_data['email_addr']
    #         # return HttpResponseRedirect('/thanks/')
    #         return HttpResponseRedirect(reverse('subscribe_result', args=(email_addr_in,)))
    #     else:
    #         return HttpResponseRedirect('subscribe_result')
    
    # t = loader.get_template('demo/home.html')
    # f = EmailSubscriberForm(request.POST)
    # c = Context({'subscribing_form': f,})
    # return HttpResponse(t.render(c))
    return render(request, 'demo/home.html')
    

def FAQ(request):
    return render(request, 'demo/FAQ.html')

def contact(request):
    return render(request, 'demo/contact.html')

def refer(request):
    print "refer gotten!"
    return render(request, 'demo/FAQ.html')


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response