from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Tool

def index(request):
    tools_list = Tool.objects.all()
    template = loader.get_template('hello/index.html')
    context = RequestContext(request, {
        'tools_list': tools_list,
    })
    return HttpResponse(template.render(context))
