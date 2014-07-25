from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from rango.models import Category, Page


def index(request):
    #request the context of teh request
    #the contet containts information such as the clients machine dtails
    context = RequestContext(request)
    category_list = Category.objects.order_by('-likes')[:5]
    #constructs a diction to pass to the tempate engine as its context 
    #Note the key boldmessage is the same as {{ boldemessage }} in the Template
    context_dict = {'categories' : category_list}
    for category in category_list:
        category.url = category.name.replace(' ', '_')


    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    return HttpResponse("RANGO SAYS: ABOUT!!! wat wat")

def category(request, category_name_url):
    context = RequestContext(request)
    category_name =  category_name_url.replace('_', ' ')

    context_dict = {'category_name': category_name }

    try: 
         category = Category.objects.get(name=category_name)
         pages = Page.objects.filter(category=category)
         context_dict['pages'] = pages
         context_dict['category'] = category
    except Category.DoesNotExist:

        pass

    return render_to_response('rango/category.html', context_dict, context)
